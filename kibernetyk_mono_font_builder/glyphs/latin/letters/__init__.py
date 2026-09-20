"""Non-ASCII Latin Core letter glyph groups."""

from kibernetyk_mono_font_builder.core import GlyphGroup

from .lowercase import BUILDERS as LOWERCASE_BUILDERS
from .other import BUILDERS as OTHER_BUILDERS
from .uppercase import BUILDERS as UPPERCASE_BUILDERS

GROUPS = (
    GlyphGroup("latin.letters.uppercase", UPPERCASE_BUILDERS),
    GlyphGroup("latin.letters.lowercase", LOWERCASE_BUILDERS),
    GlyphGroup("latin.letters.other", OTHER_BUILDERS),
)

__all__ = [
    "GROUPS",
    "LOWERCASE_BUILDERS",
    "OTHER_BUILDERS",
    "UPPERCASE_BUILDERS",
]

