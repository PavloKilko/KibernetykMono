"""Basic uppercase and lowercase Cyrillic letter groups."""

from kibernetyk_mono_font_builder.core import GlyphGroup

from .extended import GROUPS as EXTENDED_GROUPS
from .lowercase import BUILDERS as LOWERCASE_BUILDERS
from .uppercase import BUILDERS as UPPERCASE_BUILDERS

GROUPS = (
    GlyphGroup("cyrillic.letters.uppercase", UPPERCASE_BUILDERS),
    GlyphGroup("cyrillic.letters.lowercase", LOWERCASE_BUILDERS),
    *EXTENDED_GROUPS,
)

__all__ = [
    "EXTENDED_GROUPS",
    "GROUPS",
    "LOWERCASE_BUILDERS",
    "UPPERCASE_BUILDERS",
]
