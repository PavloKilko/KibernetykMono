"""Export the seven shipped TTFs as one editable Glyphs source file."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
import uuid
from collections import defaultdict
from collections.abc import Sequence
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import glyphsLib
from fontTools.ttLib import TTFont
from glyphsLib import GSInstance
from ufoLib2 import Font
from ufoLib2.objects.anchor import Anchor

from kibernetyk_mono_font_builder.core.compiler import _layout_feature_text
from kibernetyk_mono_font_builder.core.config import (
    VERSION,
    WEIGHT_CLASSES,
    WEIGHT_STYLE_NAMES,
    WEIGHT_WIDTHS,
)
from kibernetyk_mono_font_builder.glyphs import GLYPH_REGISTRY


def _arguments(arguments: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export Kibernetyk Mono as a seven-master Glyphs source."
    )
    parser.add_argument(
        "--font-dir",
        type=Path,
        default=ROOT / "fonts" / "ttf",
        help="directory containing the seven canonical TTFs",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "sources" / "KibernetykMono.glyphs",
        help="destination .glyphs file",
    )
    return parser.parse_args(arguments)


def _copy_name(ttf: TTFont, ufo: Font, attribute: str, name_id: int) -> None:
    value = ttf["name"].getDebugName(name_id)
    if value:
        setattr(ufo.info, attribute, value)


def _export_ufo(
    ttf_path: Path,
    ufo_path: Path,
    weight: str,
) -> None:
    ttf = TTFont(ttf_path)
    try:
        style_name = WEIGHT_STYLE_NAMES[weight]
        definitions = GLYPH_REGISTRY.build(WEIGHT_WIDTHS[weight])
        definition_by_name = {
            definition.name: definition for definition in definitions
        }

        ufo = Font()
        ufo.info.familyName = "Kibernetyk Mono"
        ufo.info.styleName = style_name
        ufo.info.unitsPerEm = ttf["head"].unitsPerEm
        ufo.info.ascender = ttf["hhea"].ascent
        ufo.info.descender = ttf["hhea"].descent
        ufo.info.capHeight = ttf["OS/2"].sCapHeight
        ufo.info.xHeight = ttf["OS/2"].sxHeight
        ufo.info.openTypeHheaLineGap = ttf["hhea"].lineGap
        ufo.info.openTypeOS2TypoAscender = ttf["OS/2"].sTypoAscender
        ufo.info.openTypeOS2TypoDescender = ttf["OS/2"].sTypoDescender
        ufo.info.openTypeOS2TypoLineGap = ttf["OS/2"].sTypoLineGap
        ufo.info.openTypeOS2WeightClass = WEIGHT_CLASSES[weight]
        ufo.info.openTypeOS2WidthClass = ttf["OS/2"].usWidthClass
        ufo.info.postscriptFontName = f"KibernetykMono-{style_name}"
        ufo.info.postscriptIsFixedPitch = True
        ufo.info.openTypeNamePreferredFamilyName = "Kibernetyk Mono"
        ufo.info.openTypeNamePreferredSubfamilyName = style_name

        for attribute, name_id in (
            ("copyright", 0),
            ("openTypeNameUniqueID", 3),
            ("openTypeNameVersion", 5),
            ("trademark", 7),
            ("openTypeNameManufacturer", 8),
            ("openTypeNameDesigner", 9),
            ("openTypeNameManufacturerURL", 11),
            ("openTypeNameDesignerURL", 12),
            ("openTypeNameLicense", 13),
            ("openTypeNameLicenseURL", 14),
        ):
            _copy_name(ttf, ufo, attribute, name_id)

        glyph_order = ttf.getGlyphOrder()
        ufo.lib["public.glyphOrder"] = glyph_order
        unicode_by_glyph: dict[str, list[int]] = defaultdict(list)
        for codepoint, glyph_name in ttf.getBestCmap().items():
            unicode_by_glyph[glyph_name].append(codepoint)

        glyph_set = ttf.getGlyphSet()
        for glyph_name in glyph_order:
            source_glyph = glyph_set[glyph_name]
            target_glyph = ufo.newGlyph(glyph_name)
            target_glyph.width = ttf["hmtx"].metrics[glyph_name][0]
            target_glyph.unicodes = unicode_by_glyph[glyph_name]
            source_glyph.draw(target_glyph.getPen())

        open_type_categories: dict[str, str] = {}
        for glyph in ufo:
            definition = definition_by_name.get(glyph.name)
            if definition is None:
                continue
            for anchor_name, (x, y) in definition.render_anchors().items():
                glyph.appendAnchor(Anchor(x=x, y=y, name=anchor_name))
            if definition.mark_class and definition.mark_anchor:
                x, y = definition.mark_anchor
                glyph.appendAnchor(
                    Anchor(x=x, y=y, name=f"_{definition.mark_class}")
                )
                open_type_categories[glyph.name] = "mark"

        if open_type_categories:
            ufo.lib["public.openTypeCategories"] = open_type_categories
        ufo.features.text = _layout_feature_text(definitions) or ""
        ufo.save(ufo_path, overwrite=True)
    finally:
        ttf.close()


def _add_instances(source_path: Path) -> None:
    source = glyphsLib.load(source_path)
    version_major, version_minor = VERSION.split(".", maxsplit=1)
    source.versionMajor = int(version_major)
    source.versionMinor = int(version_minor)
    source.instances = []

    master_ids: dict[str, str] = {}
    for master in source.masters:
        stable_id = str(
            uuid.uuid5(
                uuid.NAMESPACE_URL,
                f"https://github.com/PavloKilko/KibernetykMono/master/{master.name}",
            )
        ).upper()
        master_ids[master.id] = stable_id
        master.id = stable_id

    for glyph in source.glyphs:
        for layer in glyph.layers:
            layer.layerId = master_ids.get(layer.layerId, layer.layerId)
            layer.associatedMasterId = master_ids.get(
                layer.associatedMasterId,
                layer.associatedMasterId,
            )

    for master in source.masters:
        instance = GSInstance()
        instance.name = master.name
        instance.axes = list(master.axes)
        instance.weight = master.name
        instance.weightValue = master.axes[0]
        instance.customParameters["preferredFamilyName"] = "Kibernetyk Mono"
        instance.customParameters["preferredSubfamilyName"] = master.name
        instance.customParameters["weightClass"] = int(master.axes[0])
        instance.customParameters["widthClass"] = 5
        if master.name == "Bold":
            instance.isBold = True
            instance.linkStyle = "Regular"
        source.instances.append(instance)

    source.save(source_path)


def main(arguments: Sequence[str] | None = None) -> int:
    options = _arguments(arguments)
    options.output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="kibernetyk-sources-") as directory:
        temporary_directory = Path(directory)
        ufo_paths: list[Path] = []
        for weight in WEIGHT_WIDTHS:
            style_name = WEIGHT_STYLE_NAMES[weight]
            ttf_path = options.font_dir / f"KibernetykMono-{style_name}.ttf"
            if not ttf_path.is_file():
                raise FileNotFoundError(f"Missing canonical font: {ttf_path}")
            ufo_path = temporary_directory / f"KibernetykMono-{style_name}.ufo"
            _export_ufo(ttf_path, ufo_path, weight)
            ufo_paths.append(ufo_path)

        subprocess.run(
            [
                sys.executable,
                "-m",
                "glyphsLib",
                "ufo2glyphs",
                "--output-path",
                str(options.output),
                *(str(path) for path in ufo_paths),
            ],
            check=True,
        )

    _add_instances(options.output)
    print(f"Glyphs source: {options.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
