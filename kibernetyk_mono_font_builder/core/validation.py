"""Cross-glyph validation shared by preview and compiler stages."""

from __future__ import annotations

from collections.abc import Sequence
import math
import unicodedata

from .config import ADVANCE_WIDTH
from .model import GlyphDefinition


def validate_glyphs(glyphs: Sequence[GlyphDefinition]) -> None:
    names: set[str] = set()
    codepoints: set[int] = set()

    for glyph in glyphs:
        if glyph.name in names:
            raise ValueError(f"Duplicate glyph name: {glyph.name}")
        names.add(glyph.name)

        if glyph.codepoint is not None:
            if glyph.codepoint in codepoints:
                raise ValueError(f"Duplicate Unicode codepoint: U+{glyph.codepoint:04X}")
            codepoints.add(glyph.codepoint)

        if glyph.name == "space" and glyph.codepoint != 0x20:
            raise ValueError("The 'space' glyph must use Unicode codepoint U+0020")
        if glyph.codepoint == 0x20 and glyph.name != "space":
            raise ValueError("Unicode codepoint U+0020 must use the glyph name 'space'")

        is_mark = (
            glyph.codepoint is not None
            and unicodedata.category(chr(glyph.codepoint)).startswith("M")
        )
        is_nonspacing_support = (
            glyph.codepoint is None
            and glyph.name in {
                "caroncomb.alt",
                "periodcentered.loclCAT",
                "periodcentered.loclCAT.case",
            }
        )
        expected_advance = (
            0 if is_mark or is_nonspacing_support else ADVANCE_WIDTH
        )
        if glyph.advance_width != expected_advance:
            raise ValueError(
                f"Glyph {glyph.name!r} has advance {glyph.advance_width}; "
                f"expected {expected_advance}"
            )

        for anchor_name, point in glyph.anchors.items():
            if not anchor_name or anchor_name.startswith("_"):
                raise ValueError(
                    f"Invalid base anchor name on {glyph.name!r}: {anchor_name!r}"
                )
            if len(point) != 2 or not all(math.isfinite(value) for value in point):
                raise ValueError(f"Invalid anchor {anchor_name!r} on {glyph.name!r}")

        if (glyph.mark_class is None) != (glyph.mark_anchor is None):
            raise ValueError(
                f"Glyph {glyph.name!r} must define both mark_class and mark_anchor"
            )
        if glyph.mark_class is not None:
            if not glyph.mark_class or glyph.mark_class.startswith("_"):
                raise ValueError(f"Invalid mark class on {glyph.name!r}")
            if not is_mark:
                raise ValueError(f"Glyph {glyph.name!r} is not a Unicode mark")
            if len(glyph.mark_anchor) != 2 or not all(
                math.isfinite(value) for value in glyph.mark_anchor
            ):
                raise ValueError(f"Invalid mark anchor on {glyph.name!r}")
