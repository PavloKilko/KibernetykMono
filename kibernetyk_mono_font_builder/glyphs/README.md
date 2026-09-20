# Glyph groups

Glyph implementations are kept separate from the renderer and TTF compiler.
Each leaf module contains builder functions plus one `BUILDERS` mapping:

```python
from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition
from kibernetyk_mono_font_builder.core import init_glyph, line


def build_A_cyrillic(width: float) -> GlyphDefinition:
    glyph = init_glyph("Acyrillic", "А")
    glyph.add(line(width, (100, 100), (500, 700)))
    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    "А": build_A_cyrillic,
}
```

Use the actual character as the selector and a unique OpenType glyph name.
The selector, glyph name, and Unicode codepoint must remain unique across the
complete font.

## Adding a new family

The current basic Cyrillic layout is:

```text
glyphs/
└── cyrillic/
    ├── __init__.py
    └── letters/
        ├── __init__.py
        ├── uppercase.py
        └── lowercase.py
```

The letter package composes its leaf modules into named groups:

```python
from kibernetyk_mono_font_builder.core import GlyphGroup

from .lowercase import BUILDERS as LOWERCASE_BUILDERS
from .uppercase import BUILDERS as UPPERCASE_BUILDERS

GROUPS = (
    GlyphGroup("cyrillic.letters.uppercase", UPPERCASE_BUILDERS),
    GlyphGroup("cyrillic.letters.lowercase", LOWERCASE_BUILDERS),
)
```

Those groups are included by `glyphs/cyrillic/__init__.py` and registered in
`glyphs/__init__.py` alongside the ASCII groups.

The Google Fonts Core additions are scaffolded as explicit blank functions.
Add primitives directly inside each function; do not replace the explicit
functions with a generated default-builder table. Blank glyphs do not produce
SVG previews, but remain selectable by character or group while being designed.

Additional Cyrillic letter repertoires live under
`glyphs/cyrillic/letters/` and are included by its `__init__.py`:

```python
from .extended import GROUPS as EXTENDED_GROUPS

GROUPS = (
    *LETTER_GROUPS,
    *EXTENDED_GROUPS,
)
```

The Latin Core additions follow the same pattern under `glyphs/latin/`.
Shared construction helpers specific to one writing system can live beside its
glyph modules; only reusable font-wide behavior belongs in `core/`.

The scaffold is divided into focused groups:

```text
common.marks.spacing
common.marks.combining
common.punctuation
common.symbols
common.separators
latin.letters.uppercase
latin.letters.lowercase
latin.letters.other
latin.support
cyrillic.letters.extended.uppercase
cyrillic.letters.extended.lowercase
```

The compiler creates `.notdef` itself. The `latin.support` group contains
the four required unencoded glyphs: `periodcentered.loclCAT`,
`periodcentered.loclCAT.case`, `caroncomb.alt`, and `idotaccent`.
