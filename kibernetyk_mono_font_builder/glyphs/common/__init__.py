"""Shared punctuation, symbol, separator, and mark glyph groups."""

from kibernetyk_mono_font_builder.core import GlyphGroup

from .marks import GROUPS as MARK_GROUPS
from .punctuation import BUILDERS as PUNCTUATION_BUILDERS
from .separators import BUILDERS as SEPARATOR_BUILDERS
from .symbols import BUILDERS as SYMBOL_BUILDERS

GROUPS = (
    *MARK_GROUPS,
    GlyphGroup("common.punctuation", PUNCTUATION_BUILDERS),
    GlyphGroup("common.symbols", SYMBOL_BUILDERS),
    GlyphGroup("common.separators", SEPARATOR_BUILDERS),
)

__all__ = [
    "GROUPS",
    "MARK_GROUPS",
    "PUNCTUATION_BUILDERS",
    "SEPARATOR_BUILDERS",
    "SYMBOL_BUILDERS",
]

