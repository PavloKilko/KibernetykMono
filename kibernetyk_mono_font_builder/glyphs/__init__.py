"""Composition point for every glyph family included in the font."""

from kibernetyk_mono_font_builder.core import GlyphRegistry

from .ascii import GROUPS as ASCII_GROUPS
from .common import GROUPS as COMMON_GROUPS
from .cyrillic import GROUPS as CYRILLIC_GROUPS
from .latin import GROUPS as LATIN_GROUPS

ALL_GROUPS = (
    *ASCII_GROUPS,
    *COMMON_GROUPS,
    *LATIN_GROUPS,
    *CYRILLIC_GROUPS,
)

GLYPH_REGISTRY = GlyphRegistry(ALL_GROUPS)
GLYPH_BUILDERS = GLYPH_REGISTRY.builders

__all__ = [
    "ALL_GROUPS",
    "ASCII_GROUPS",
    "COMMON_GROUPS",
    "CYRILLIC_GROUPS",
    "GLYPH_BUILDERS",
    "GLYPH_REGISTRY",
    "LATIN_GROUPS",
]
