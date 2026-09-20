"""Procedural builders extracted from the legacy monolithic script."""

from __future__ import annotations

import math

from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition, init_glyph, line, polyline


def build_0(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    slash_y_offset = radius / 2

    glyph = init_glyph("0", "0")
    glyph.add(
        polyline(
            width,
            [
                (radius, 400),
                (radius, 650 - diagonal_offset),
                (150 + diagonal_offset, 800 - radius),
                (450 - diagonal_offset, 800 - radius),
                (600 - radius, 650 - diagonal_offset),
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),
                (150 + diagonal_offset, radius),
                (radius, 150 + diagonal_offset),
                (radius, 400),
            ],
        )
    )
    glyph.add(
        line(
            width,
            (radius, 200 + slash_y_offset),
            (600 - radius, 600 - slash_y_offset),
        )
    )
    return glyph

def build_1(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("1", "1")
    # glyph.add(
    #     polyline(
    #         width,
    #         [
    #             (radius, 600 - radius),
    #             (150, 600 - radius),
    #             (300, 750 - radius),
    #             (300, 800 - radius),
    #         ],
    #     )
    # )
    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (300, 800 - radius),
                (300, radius)
            ]
        )
    )
    # glyph.add(
    #     line(
    #         width,
    #         (300, 800 - radius),
    #         (300, radius),
    #     )
    # )
    glyph.add(
        line(
            width,
            (radius, radius),
            (600 - radius, radius),
        )
    )
    return glyph

def build_2(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("2", "2")
    glyph.add(
        polyline(
            width,
            [
                (radius, 650 - diagonal_offset),
                (150 + diagonal_offset, 800 - radius),
                (450 - diagonal_offset, 800 - radius),
                (600 - radius, 650 - diagonal_offset),
                (600 - radius, 500 - radius + diagonal_offset),
                (500 - diagonal_offset, 400),
                (150 + diagonal_offset, 400),
                (radius, 250 + radius - diagonal_offset),
                (radius, radius),
                (600 - radius, radius),
            ],
        )
    )
    return glyph

def build_3(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("3", "3")
    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (600 - radius, 800 - radius),
                (250 + diagonal_offset, 450 + diagonal_offset),
                (500 - diagonal_offset, 450 + diagonal_offset),
                (600 - radius, 350 + radius),
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),
                (150 + diagonal_offset, radius),
                (radius, 150 + diagonal_offset),
            ],
        )
    )
    return glyph

def build_4(width: float) -> GlyphDefinition:
    radius = width / 2
    # diagonal_offset = (math.sqrt(2) - 1) * radius
    diagonal_x_offset = (8 / math.sqrt(145)) * radius
    diagonal_y_offset = (9 / math.sqrt(145)) * radius
    corner_y_offset = (9 / 8) * radius

    glyph = init_glyph("4", "4")
    # glyph.add(
    #     polyline(
    #         width,
    #         [
    #             (300, 800 - radius),
    #             (300, 650 - radius + diagonal_offset),
    #             (radius, 350 + diagonal_offset),
    #             (radius, 200),
    #             (600 - radius, 200),
    #         ],
    #     )
    # )
    glyph.add(
        polyline(
            width,
            [
                (400 - diagonal_x_offset, 800 - diagonal_y_offset),
                (radius, 350 + corner_y_offset),
                (radius, 200),
                (600 - radius, 200),
            ],
        )
    )
    glyph.add(
        line(
            width,
            (400, 450 - radius),
            (400, radius),
        )
    )
    return glyph

def build_5(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("5", "5")
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 800 - radius),
                (radius, 800 - radius),
                (radius, 500 - radius + diagonal_offset),
                (100 + diagonal_offset, 400),
                (500 - diagonal_offset, 400),
                (600 - radius, 300 + radius - diagonal_offset),
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),
                (150 + diagonal_offset, radius),
                (radius, 150 + diagonal_offset),
            ],
        )
    )
    return glyph

def build_6(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("6", "6")
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 650 - diagonal_offset),
                (450 - diagonal_offset, 800 - radius),
                (150 + diagonal_offset, 800 - radius),
                (radius, 650 - diagonal_offset),
                (radius, 150 + diagonal_offset),
                (150 + diagonal_offset, radius),
                (450 - diagonal_offset, radius),
                (600 - radius, 150 + diagonal_offset),
                (600 - radius, 300 + radius - diagonal_offset),
                (500 - diagonal_offset, 400),
                (radius, 400),
            ],
        )
    )
    return glyph

def build_7(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_y_offset = (5 / 6) * radius

    glyph = init_glyph("7", "7")
    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (600 - radius, 800 - radius),
                (600 - radius, 650 - diagonal_y_offset),
                (300, 400),
                (300, radius),
            ],
        )
    )
    return glyph

def build_8(width: float) -> GlyphDefinition:
    # radius = width / 2
    # diagonal_offset = (math.sqrt(2) - 1) * radius
    # middle_offset = radius - diagonal_offset

    # glyph = init_glyph("8", "8")
    # glyph.add(
    #     polyline(
    #         width,
    #         [
    #             (300, radius),
    #             (150 + diagonal_offset, radius),
    #             (radius, 150 + diagonal_offset),
    #             (radius, 300 + middle_offset),
    #             (100 + diagonal_offset, 400),
    #             (radius, 500 - middle_offset),
    #             (radius, 650 - diagonal_offset),
    #             (150 + diagonal_offset, 800 - radius),
    #             (450 - diagonal_offset, 800 - radius),
    #             (600 - radius, 650 - diagonal_offset),
    #             (600 - radius, 500 - middle_offset),
    #             (500 - diagonal_offset, 400),
    #             (600 - radius, 300 + middle_offset),
    #             (600 - radius, 150 + diagonal_offset),
    #             (450 - diagonal_offset, radius),
    #             (300, radius),
    #         ],
    #     )
    # )
    # glyph.add(
    #     line(
    #         width,
    #         (100 + diagonal_offset, 400),
    #         (500 - diagonal_offset, 400),
    #     )
    # )
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("8", "8")

    glyph.add(
        polyline(
            width,
            [
                (300, 400),
                (150 + diagonal_offset, 400),
                (radius, 550 - middle_offset),
                (radius, 650 - diagonal_offset),
                (150 + diagonal_offset, 800 - radius),
                (450 - diagonal_offset, 800 - radius),
                (600 - radius, 650 - diagonal_offset),
                (600 - radius, 550 - middle_offset),
                (450 - diagonal_offset, 400),
                (300, 400),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (300, 400),
                (150 + diagonal_offset, 400),
                (radius, 250 + middle_offset),
                (radius, 150 + diagonal_offset),
                (150 + diagonal_offset, radius),
                (450 - diagonal_offset, radius),
                (600 - radius, 150 + diagonal_offset),
                (600 - radius, 250 + middle_offset),
                (450 - diagonal_offset, 400),
                (300, 400),
            ],
        )
    )

    return glyph

def build_9(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("9", "9")
    glyph.add(
        polyline(
            width,
            [
                (radius, 150 + diagonal_offset),
                (150 + diagonal_offset, radius),
                (450 - diagonal_offset, radius),
                (600 - radius, 150 + diagonal_offset),
                (600 - radius, 650 - diagonal_offset),
                (450 - diagonal_offset, 800 - radius),
                (150 + diagonal_offset, 800 - radius),
                (radius, 650 - diagonal_offset),
                (radius, 500 - radius + diagonal_offset),
                (100 + diagonal_offset, 400),
                (600 - radius, 400),
            ],
        )
    )
    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    '0': build_0,
    '1': build_1,
    '2': build_2,
    '3': build_3,
    '4': build_4,
    '5': build_5,
    '6': build_6,
    '7': build_7,
    '8': build_8,
    '9': build_9,
}

__all__ = ['BUILDERS', 'build_0', 'build_1', 'build_2', 'build_3', 'build_4', 'build_5', 'build_6', 'build_7', 'build_8', 'build_9']
