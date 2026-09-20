"""Compilation of procedural glyph outlines into a monospaced TrueType font."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
import re
import unicodedata

from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from fontTools.fontBuilder import FontBuilder
from fontTools.misc.roundTools import otRound
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import newTable
from fontTools.ttLib.removeOverlaps import removeOverlaps

from .config import (
    ADVANCE_WIDTH,
    ASCENDER,
    CAP_HEIGHT,
    DESCENDER,
    FAMILY_NAME,
    FONT_METADATA,
    LINE_GAP,
    ROUNDED_FAMILY_NAME,
    UNITS_PER_EM,
    VERSION,
    VERTICAL_BOX_BOTTOM,
    VERTICAL_BOX_TOP,
    WEIGHT_CLASSES,
    WEIGHT_STYLE_NAMES,
    X_HEIGHT,
)
from .model import GlyphDefinition
from .validation import validate_glyphs


def _empty_glyph():
    return TTGlyphPen(None).glyph()


def _glyph_outline(glyph: GlyphDefinition, rounded: bool):
    pen = TTGlyphPen(None)
    for polygon in glyph.render(rounded=rounded):
        if len(polygon) < 3:
            continue
        pen.moveTo((polygon[0].x, polygon[0].y))
        for point in polygon[1:]:
            pen.lineTo((point.x, point.y))
        pen.closePath()
    return pen.glyph()


def _glyph_lsb(glyph: GlyphDefinition, rounded: bool) -> int:
    points = [
        point
        for polygon in glyph.render(rounded=rounded)
        for point in polygon
    ]
    # Use the same integer rounding as TTGlyphPen for half-unit translations.
    return otRound(min((point.x for point in points), default=0))


def _resolve_rounded(
    glyphs: Sequence[GlyphDefinition],
    rounded: bool | None,
) -> bool:
    if rounded is not None:
        if not isinstance(rounded, bool):
            raise TypeError("rounded must be a boolean")
        return rounded

    if any(not isinstance(glyph.rounded, bool) for glyph in glyphs):
        raise TypeError("glyph.rounded must be a boolean")
    variants = {glyph.rounded for glyph in glyphs}
    if len(variants) > 1:
        raise ValueError("Cannot combine angular and rounded glyphs in one font")
    return variants.pop() if variants else False


def _feature_class_name(mark_class: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9_.]", "_", mark_class)
    if not normalized or normalized[0].isdigit():
        normalized = f"_{normalized}"
    return f"MC_{normalized}"


def _anchor_literal(point: tuple[float, float]) -> str:
    return f"<anchor {otRound(point[0])} {otRound(point[1])}>"


def _layout_feature_text(
    glyphs: Sequence[GlyphDefinition],
    rounded: bool | None = None,
) -> str | None:
    glyphs_by_name = {glyph.name: glyph for glyph in glyphs}
    language_systems: list[str] = []
    locl_rules: list[str] = []

    catalan_glyphs = {
        "L",
        "l",
        "periodcentered",
        "periodcentered.loclCAT",
        "periodcentered.loclCAT.case",
    }
    if catalan_glyphs <= glyphs_by_name.keys():
        language_systems.append("languagesystem latn CAT;")
        locl_rules.extend(
            (
                "  script latn;",
                "  language CAT;",
                "  sub l periodcentered' l by periodcentered.loclCAT;",
                "  sub L periodcentered' L by periodcentered.loclCAT.case;",
            )
        )

    if {"i", "idotaccent"} <= glyphs_by_name.keys():
        turkic_languages = ("AZE", "CRT", "KAZ", "TAT", "TRK")
        language_systems.extend(
            f"languagesystem latn {language};"
            for language in turkic_languages
        )
        if locl_rules:
            locl_rules.append("")
        locl_rules.append("  script latn;")
        for language in turkic_languages:
            locl_rules.extend(
                (
                    f"  language {language};",
                    "  sub i by idotaccent;",
                )
            )

    if language_systems:
        # Features without an explicit script/language block (ccmp and mark)
        # must remain available to ordinary Latin, Cyrillic, and script-neutral
        # shaping after language-specific locl systems are declared.
        language_systems[:0] = [
            "languagesystem DFLT dflt;",
            "languagesystem latn dflt;",
            "languagesystem cyrl dflt;",
        ]

    mark_groups: dict[str, list[GlyphDefinition]] = {}
    for glyph in glyphs:
        if glyph.mark_class is not None and glyph.mark_anchor is not None:
            mark_groups.setdefault(glyph.mark_class, []).append(glyph)

    sections: list[str] = []
    if language_systems:
        sections.append("\n".join(language_systems))
    if locl_rules:
        sections.append("\n".join(("feature locl {", *locl_rules, "} locl;")))
    if not mark_groups:
        return "\n".join(sections) or None

    feature_classes: dict[str, str] = {}
    used_feature_classes: dict[str, str] = {}
    for mark_class in mark_groups:
        feature_class = _feature_class_name(mark_class)
        previous = used_feature_classes.get(feature_class)
        if previous is not None and previous != mark_class:
            raise ValueError(
                f"Mark classes {previous!r} and {mark_class!r} compile to the "
                f"same feature class @{feature_class}"
            )
        feature_classes[mark_class] = feature_class
        used_feature_classes[feature_class] = mark_class

    glyphs_by_codepoint = {
        glyph.codepoint: glyph
        for glyph in glyphs
        if glyph.codepoint is not None
    }
    dotless_bases: dict[int, GlyphDefinition] = {}
    for dotted_codepoint, dotless_codepoint in ((0x0069, 0x0131), (0x006A, 0x0237)):
        dotted = glyphs_by_codepoint.get(dotted_codepoint)
        dotless = glyphs_by_codepoint.get(dotless_codepoint)
        if (
            dotted is not None
            and dotted.objects
            and dotless is not None
            and dotless.objects
            and "top" in dotless.anchors
        ):
            dotless_bases[dotted_codepoint] = dotless

    ccmp_rules: list[str] = []
    caron_alternate_glyphs = {
        "L",
        "d",
        "l",
        "t",
        "caroncomb",
        "caroncomb.alt",
    }
    if caron_alternate_glyphs <= glyphs_by_name.keys():
        # Czech and Slovak use an apostrophe-like caron beside tall letters.
        # The alternate is already drawn at its final zero-width position, so
        # substitute it before mark positioning instead of attaching it above.
        ccmp_rules.append(
            "  sub [L d l t] caroncomb' by caroncomb.alt;"
        )
    for glyph in glyphs:
        if glyph.codepoint is None or glyph.objects:
            continue
        characters = unicodedata.normalize("NFD", chr(glyph.codepoint))
        if len(characters) != 2:
            continue
        base = glyphs_by_codepoint.get(ord(characters[0]))
        mark = glyphs_by_codepoint.get(ord(characters[1]))
        if (
            base is None
            or mark is None
            or not base.objects
            or not mark.objects
            or mark.mark_class is None
            or mark.mark_anchor is None
            or mark.mark_class not in base.anchors
        ):
            continue
        if mark.mark_class == "top":
            base = dotless_bases.get(base.codepoint, base)
        ccmp_rules.append(
            f"  sub {glyph.name} by {base.name} {mark.name};"
        )

    # Also handle typed combining sequences, including a bottom mark before
    # the top accent. Plain i/j and bottom-only accents keep their dots.
    top_marks = [mark.name for mark in mark_groups.get("top", ()) if mark.objects]
    if top_marks and dotless_bases:
        sections.append(f"@DOTLESS_TOP_MARKS = [{' '.join(top_marks)}];")
        ccmp_rules.extend((
            "  lookup DotlessBeforeTopMark {",
            "    lookupflag UseMarkFilteringSet @DOTLESS_TOP_MARKS;",
        ))
        for codepoint, dotless in dotless_bases.items():
            dotted = glyphs_by_codepoint[codepoint]
            ccmp_rules.append(
                f"    sub {dotted.name}' @DOTLESS_TOP_MARKS by {dotless.name};"
            )
        ccmp_rules.append("  } DotlessBeforeTopMark;")
    if ccmp_rules:
        sections.append("\n".join(("feature ccmp {", *ccmp_rules, "} ccmp;")))

    mark_lines: list[str] = []
    for mark_class, marks in mark_groups.items():
        feature_class = feature_classes[mark_class]
        for mark in marks:
            mark_lines.append(
                f"markClass {mark.name} {_anchor_literal(mark.mark_anchor)} "
                f"@{feature_class};"
            )

    positioning: list[str] = []
    for glyph in glyphs:
        if glyph.mark_class is not None:
            continue
        anchors = glyph.render_anchors(rounded)
        for mark_class, feature_class in feature_classes.items():
            anchor = anchors.get(mark_class)
            if anchor is not None:
                positioning.append(
                    f"  pos base {glyph.name} {_anchor_literal(anchor)} "
                    f"mark @{feature_class};"
                )
    if not positioning:
        return "\n".join(sections) or None

    mark_lines.extend(("feature mark {", *positioning, "} mark;"))
    sections.append("\n".join(mark_lines))
    return "\n".join(sections)


def _static_font_names(
    family_name: str,
    style_name: str,
    weight_class: int,
) -> tuple[dict[str, str], int, int]:
    """Return Google Fonts-compatible names and style bits for a static font."""

    postscript_name = f"{family_name.replace(' ', '')}-{style_name}"
    full_name = f"{family_name} {style_name}"
    names = {
        "familyName": family_name,
        "styleName": style_name,
        "uniqueFontIdentifier": f"{VERSION};NONE;{postscript_name}",
        "fullName": full_name,
        "psName": postscript_name,
        "version": f"Version {VERSION}",
    }
    names.update(
        {
            name_id: value
            for name_id, value in FONT_METADATA.items()
            if value
        }
    )

    if weight_class == 700:
        return names, 0x20, 0x01
    if weight_class == 400:
        return names, 0x40, 0

    # Thin, ExtraLight, Light, Medium, and SemiBold are not legacy RIBBI
    # styles. Keep their style in typographic names (IDs 16/17), while IDs
    # 1/2 describe a standalone Regular face for older software.
    names.update(
        {
            "familyName": full_name,
            "styleName": "Regular",
            "typographicFamily": family_name,
            "typographicSubfamily": style_name,
        }
    )
    return names, 0x40, 0


def build_ttf(
    glyphs: Sequence[GlyphDefinition],
    output: Path,
    weight: str,
    rounded: bool | None = None,
) -> Path:
    """Compile glyph polygons into a monospaced TrueType-flavored TTF."""

    validate_glyphs(glyphs)
    if weight not in WEIGHT_CLASSES:
        raise ValueError(f"Unknown weight: {weight!r}")

    use_rounded = _resolve_rounded(glyphs, rounded)
    family_name = ROUNDED_FAMILY_NAME if use_rounded else FAMILY_NAME
    style_name = WEIGHT_STYLE_NAMES[weight]
    weight_class = WEIGHT_CLASSES[weight]
    name_table, fs_selection, mac_style = _static_font_names(
        family_name,
        style_name,
        weight_class,
    )
    notdef_glyph = next(
        (glyph for glyph in glyphs if glyph.name == ".notdef"),
        None,
    )
    space_glyph = next((glyph for glyph in glyphs if glyph.name == "space"), None)
    drawn_glyphs = [
        glyph for glyph in glyphs if glyph.name not in {".notdef", "space"}
    ]
    glyph_order = [".notdef", "space", *(glyph.name for glyph in drawn_glyphs)]
    character_map = {32: "space"}
    character_map.update(
        {
            glyph.codepoint: glyph.name
            for glyph in glyphs
            if glyph.codepoint is not None
        }
    )

    glyph_outlines = {
        ".notdef": (
            _glyph_outline(notdef_glyph, use_rounded)
            if notdef_glyph is not None
            else _empty_glyph()
        ),
        "space": (
            _glyph_outline(space_glyph, use_rounded)
            if space_glyph is not None
            else _empty_glyph()
        ),
    }
    glyph_outlines.update(
        {
            glyph.name: _glyph_outline(glyph, use_rounded)
            for glyph in drawn_glyphs
        }
    )

    horizontal_metrics = {
        ".notdef": (
            (
                notdef_glyph.advance_width,
                _glyph_lsb(notdef_glyph, use_rounded),
            )
            if notdef_glyph is not None
            else (ADVANCE_WIDTH, 0)
        ),
        "space": (
            (space_glyph.advance_width, _glyph_lsb(space_glyph, use_rounded))
            if space_glyph is not None
            else (ADVANCE_WIDTH, 0)
        ),
    }
    horizontal_metrics.update(
        {
            glyph.name: (
                glyph.advance_width,
                _glyph_lsb(glyph, use_rounded),
            )
            for glyph in drawn_glyphs
        }
    )

    font = FontBuilder(UNITS_PER_EM, isTTF=True)
    font.font["head"].fontRevision = float(VERSION)
    font.font["head"].macStyle = mac_style
    font.setupGlyphOrder(glyph_order)
    font.setupCharacterMap(character_map)
    font.setupGlyf(glyph_outlines)
    font.setupHorizontalMetrics(horizontal_metrics)
    font.setupHorizontalHeader(
        ascent=ASCENDER,
        descent=DESCENDER,
        lineGap=LINE_GAP,
    )
    font.setupNameTable(name_table)
    font.setupOS2(
        version=3,
        usWeightClass=weight_class,
        usWidthClass=5,
        fsType=0,
        fsSelection=fs_selection,
        achVendID="NONE",
        sTypoAscender=ASCENDER,
        sTypoDescender=DESCENDER,
        sTypoLineGap=LINE_GAP,
        usWinAscent=VERTICAL_BOX_TOP,
        usWinDescent=abs(VERTICAL_BOX_BOTTOM),
        sxHeight=X_HEIGHT,
        sCapHeight=CAP_HEIGHT,
    )
    font.font["OS/2"].panose.bFamilyType = 2
    font.font["OS/2"].panose.bProportion = 9
    font.setupPost(
        italicAngle=0,
        underlinePosition=-100,
        underlineThickness=50,
        isFixedPitch=1,
    )

    layout_features = _layout_feature_text(glyphs, use_rounded)
    if layout_features is not None:
        addOpenTypeFeaturesFromString(font.font, layout_features)

    # Google Fonts identifies this 0x000A range as the expected GASP behavior
    # for an unhinted TrueType font: grayscale and symmetric smoothing, without
    # grid fitting, at every PPEM size.
    gasp = newTable("gasp")
    gasp.version = 1
    gasp.gaspRange = {0xFFFF: 0x000A}
    font.font["gasp"] = gasp

    removeOverlaps(
        font.font,
        glyphNames=[glyph.name for glyph in glyphs if glyph.objects],
        removeHinting=True,
        ignoreErrors=False,
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    font.save(output)
    return output
