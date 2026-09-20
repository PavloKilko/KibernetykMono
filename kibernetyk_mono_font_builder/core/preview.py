"""SVG preview naming and rendering."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from .model import GlyphDefinition
from .renderer import write_svg
from .validation import validate_glyphs


def preview_filename(glyph: GlyphDefinition) -> str:
    """Return a readable, case-insensitively unique preview filename."""

    readable_name = "".join(
        character
        if character.isascii() and (character.isalnum() or character in "-_")
        else f"_U{ord(character):04X}_"
        for character in glyph.name
    )

    if glyph.codepoint is not None:
        return f"{readable_name}_U{glyph.codepoint:04X}.svg"

    encoded_name = glyph.name.encode("utf-8").hex().upper()
    return f"{readable_name}_N{encoded_name}.svg"


def render_previews(
    glyphs: Sequence[GlyphDefinition],
    output_directory: Path,
    margin: float = 50,
    rounded: bool | None = None,
) -> list[Path]:
    """Write one SVG preview per non-empty glyph."""

    validate_glyphs(glyphs)
    output_directory.mkdir(parents=True, exist_ok=True)

    outputs: list[Path] = []
    output_names: dict[str, str] = {}
    for glyph in glyphs:
        filename = preview_filename(glyph)
        registry_key = filename.casefold()
        previous = output_names.get(registry_key)
        if previous is not None:
            raise ValueError(
                f"Preview filename collision: {previous!r} and {filename!r}"
            )
        output_names[registry_key] = filename

        polygons = glyph.render(rounded=rounded)
        if not polygons:
            continue
        output = output_directory / filename
        write_svg(polygons, output, margin, advance_width=glyph.advance_width)
        outputs.append(output)

    return outputs
