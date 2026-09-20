"""ASCII letter glyph groups."""

from kibernetyk_mono_font_builder.core import GlyphGroup

from .lowercase import BUILDERS as LOWERCASE_BUILDERS
from .uppercase import BUILDERS as UPPERCASE_BUILDERS

GROUPS = (
    GlyphGroup("ascii.letters.uppercase", UPPERCASE_BUILDERS),
    GlyphGroup("ascii.letters.lowercase", LOWERCASE_BUILDERS),
)

__all__ = ["GROUPS", "LOWERCASE_BUILDERS", "UPPERCASE_BUILDERS"]

