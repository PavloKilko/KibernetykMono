"""Blank builders for uncased Latin Core letters."""

from __future__ import annotations

import math

from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition, dot, init_glyph, line, polygon, polyline


def build_ordfeminine(width: float) -> GlyphDefinition:
    ordinal_width = width * 0.5
    radius = ordinal_width / 2

    center_x = 300
    center_y = 650

    # Original design box is 300 × 300:
    # x: 150..450
    # y: 500..800
    scale = (150 - radius) / 150

    def compensate(point):
        x, y = point
        return (
            center_x + (x - center_x) * scale,
            center_y + (y - center_y) * scale,
        )

    glyph = init_glyph("ordfeminine", 0x00AA)

    glyph.add(
        polyline(
            ordinal_width,
            [
                compensate((150, 750)),
                compensate((200, 800)),
                compensate((400, 800)),
                compensate((450, 750)),
                compensate((450, 500)),
            ],
        )
    )

    glyph.add(
        polyline(
            ordinal_width,
            [
                compensate((450, 600)),
                compensate((350, 500)),
                compensate((200, 500)),
                compensate((150, 550)),
                compensate((150, 600)),
                compensate((200, 650)),
                compensate((450, 650)),
            ],
        )
    )

    # glyph.add(
    #     line(
    #         ordinal_width,
    #         compensate((150, 350)),
    #         compensate((450, 350)),
    #     )
    # )

    return glyph


def build_ordmasculine(width: float) -> GlyphDefinition:
    ordinal_width = width * 0.5
    radius = ordinal_width / 2

    center_x = 300
    center_y = 700

    # Preserve the original 300 × 200 proportions uniformly.
    # Horizontal design radius is 150.
    scale = (150 - radius) / 150

    def compensate(point):
        x, y = point
        return (
            center_x + (x - center_x) * scale,
            center_y + (y - center_y) * scale,
        )

    glyph = init_glyph("ordmasculine", 0x00BA)

    glyph.add(
        polyline(
            ordinal_width,
            [
                compensate((450, 650)),
                compensate((450, 550)),
                compensate((400, 500)),
                compensate((200, 500)),
                compensate((150, 550)),
                compensate((150, 750)),
                compensate((200, 800)),
                compensate((400, 800)),
                compensate((450, 750)),
                compensate((450, 650))
            ],
        )
    )

    # glyph.add(
    #     line(
    #         ordinal_width,
    #         compensate((150, 350)),
    #         compensate((450, 350)),
    #     )
    # )

    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    "\u00AA": build_ordfeminine,
    "\u00BA": build_ordmasculine,
}


__all__ = [
    "BUILDERS",
    "build_ordfeminine",
    "build_ordmasculine",
]
