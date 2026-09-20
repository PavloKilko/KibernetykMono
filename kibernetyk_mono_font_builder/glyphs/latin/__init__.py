"""Latin Core additions beyond printable ASCII."""

from kibernetyk_mono_font_builder.core import GlyphGroup

from .letters import GROUPS as LETTER_GROUPS
from .support import BUILDERS as SUPPORT_BUILDERS

GROUPS = (
    *LETTER_GROUPS,
    GlyphGroup("latin.support", SUPPORT_BUILDERS),
)

__all__ = ["GROUPS", "LETTER_GROUPS", "SUPPORT_BUILDERS"]

