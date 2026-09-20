"""Modular Kibernetyk Mono font-builder API."""

from __future__ import annotations

from collections.abc import Sequence

from .core import (
    ADVANCE_WIDTH,
    ASCENDER,
    CAP_HEIGHT,
    CORNER_CURVE_STEPS,
    CORNER_RADIUS_RATIO,
    DESCENDER,
    FAMILY_NAME,
    FONT_FILE_STEM,
    GLYPH_CENTER_X,
    LINE_GAP,
    ROUNDED_FAMILY_NAME,
    UNITS_PER_EM,
    VERSION,
    VERTICAL_BOX_BOTTOM,
    VERTICAL_BOX_TOP,
    WEIGHT_CLASSES,
    WEIGHT_STYLE_NAMES,
    WEIGHT_WIDTHS,
    X_HEIGHT,
    GlyphBuilder,
    GlyphDefinition,
    GlyphGroup,
    GlyphPolygon,
    GlyphRegistry,
    build_ttf,
    dot,
    init_glyph,
    line,
    polygon,
    polyline,
    preview_filename,
    render_previews,
    validate_glyphs,
)
from .glyphs import GLYPH_BUILDERS, GLYPH_REGISTRY


def render_glyphs(
    width: float,
    names: Sequence[str] | None = None,
    groups: Sequence[str] | None = None,
    rounded: bool = False,
) -> list[GlyphDefinition]:
    if not isinstance(rounded, bool):
        raise TypeError("rounded must be a boolean")

    glyphs = GLYPH_REGISTRY.build(width, names=names, group_names=groups)
    for glyph in glyphs:
        glyph.rounded = rounded
    return glyphs


__all__ = [
    "ADVANCE_WIDTH",
    "ASCENDER",
    "CAP_HEIGHT",
    "CORNER_CURVE_STEPS",
    "CORNER_RADIUS_RATIO",
    "DESCENDER",
    "FAMILY_NAME",
    "FONT_FILE_STEM",
    "GLYPH_CENTER_X",
    "GLYPH_BUILDERS",
    "GLYPH_REGISTRY",
    "GlyphBuilder",
    "GlyphDefinition",
    "GlyphGroup",
    "GlyphPolygon",
    "GlyphRegistry",
    "LINE_GAP",
    "ROUNDED_FAMILY_NAME",
    "UNITS_PER_EM",
    "VERSION",
    "VERTICAL_BOX_BOTTOM",
    "VERTICAL_BOX_TOP",
    "WEIGHT_CLASSES",
    "WEIGHT_STYLE_NAMES",
    "WEIGHT_WIDTHS",
    "X_HEIGHT",
    "build_ttf",
    "dot",
    "init_glyph",
    "line",
    "polygon",
    "polyline",
    "preview_filename",
    "render_glyphs",
    "render_previews",
    "validate_glyphs",
]
