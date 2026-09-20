"""Public core API used by glyph group modules."""

from .compiler import build_ttf
from .config import (
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
)
from .model import GlyphDefinition, GlyphPolygon
from .preview import preview_filename, render_previews
from .primitives import dot, init_glyph, line, polygon, polyline
from .registry import GlyphBuilder, GlyphGroup, GlyphRegistry
from .validation import validate_glyphs

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
    "render_previews",
    "validate_glyphs",
]
