"""Complete printable-ASCII glyph groups."""

from kibernetyk_mono_font_builder.core import GlyphGroup

from .letters import GROUPS as LETTER_GROUPS
from .numbers import BUILDERS as NUMBER_BUILDERS
from .punctuation import BUILDERS as PUNCTUATION_BUILDERS

GROUPS = (
    *LETTER_GROUPS,
    GlyphGroup("ascii.numbers", NUMBER_BUILDERS),
    GlyphGroup("ascii.punctuation", PUNCTUATION_BUILDERS),
)

__all__ = [
    "GROUPS",
    "LETTER_GROUPS",
    "NUMBER_BUILDERS",
    "PUNCTUATION_BUILDERS",
]

