"""Spacing and combining mark glyph groups."""

from kibernetyk_mono_font_builder.core import GlyphGroup

from .combining import BUILDERS as COMBINING_BUILDERS
from .spacing import BUILDERS as SPACING_BUILDERS

GROUPS = (
    GlyphGroup("common.marks.spacing", SPACING_BUILDERS),
    GlyphGroup("common.marks.combining", COMBINING_BUILDERS),
)

__all__ = ["COMBINING_BUILDERS", "GROUPS", "SPACING_BUILDERS"]

