"""Blank builders for non-ASCII separators."""

from __future__ import annotations

from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition, init_glyph


def build_nbspace(width: float) -> GlyphDefinition:
    glyph = init_glyph("nbspace", 0x00A0)
    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    "\u00A0": build_nbspace,
}


__all__ = [
    "BUILDERS",
    "build_nbspace",
]
