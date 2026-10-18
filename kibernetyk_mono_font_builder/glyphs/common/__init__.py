"""Shared punctuation, symbol, separator, and mark glyph groups."""

from kibernetyk_mono_font_builder.core import GlyphGroup

from .block_elements import BUILDERS as BLOCK_ELEMENT_BUILDERS
from .box_drawing import BUILDERS as BOX_DRAWING_BUILDERS
from .marks import GROUPS as MARK_GROUPS
from .punctuation import BUILDERS as PUNCTUATION_BUILDERS
from .separators import BUILDERS as SEPARATOR_BUILDERS
from .symbols import BUILDERS as SYMBOL_BUILDERS

GROUPS = (
    *MARK_GROUPS,
    GlyphGroup("common.punctuation", PUNCTUATION_BUILDERS),
    GlyphGroup("common.symbols", SYMBOL_BUILDERS),
    GlyphGroup("common.separators", SEPARATOR_BUILDERS),
    GlyphGroup("common.box_drawing", BOX_DRAWING_BUILDERS),
    GlyphGroup("common.block_elements", BLOCK_ELEMENT_BUILDERS),
)

__all__ = [
    "BLOCK_ELEMENT_BUILDERS",
    "BOX_DRAWING_BUILDERS",
    "GROUPS",
    "MARK_GROUPS",
    "PUNCTUATION_BUILDERS",
    "SEPARATOR_BUILDERS",
    "SYMBOL_BUILDERS",
]
