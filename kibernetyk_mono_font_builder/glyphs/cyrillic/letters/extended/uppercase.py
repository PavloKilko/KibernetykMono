"""Blank builders for uppercase Cyrillic Core additions."""

from __future__ import annotations

import math

from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition, dot, init_glyph, line, polygon, polyline


def build_Dje_cy(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("Dje-cy", 0x0402)

    glyph.add(
        line(
            width,
            (radius, 800 - radius),
            (400 - radius, 800 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (200, 800 - radius),
            (200, radius),
        )
    )

    glyph.add(
        polyline(
            width,
            [
                # Preserve 45° transition from stem into shoulder
                (200, 400 - middle_offset),
                (300 - diagonal_offset, 500 - radius),

                (500 - diagonal_offset, 500 - radius),

                # Upper-right 45°
                (600 - radius, 400 - diagonal_offset),

                # Right vertical
                (600 - radius, -100 + diagonal_offset),

                # Lower-right 45°
                (500 - diagonal_offset, -200 + radius),

                # Open horizontal endpoint
                (400 + radius, -200 + radius),
            ],
        )
    )

    return glyph


def build_Je_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("Je-cy", 0x0408)
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    # glyph = init_glyph("J", "J")
    glyph.add(
        polyline(
            width,
            [
                (100 + radius, 800 - radius),
                (600 - radius, 800 - radius),
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),
                (150 + diagonal_offset, radius),
                (radius, 150 + diagonal_offset),
                (radius, 300 - radius),
            ],
        )
    )
    return glyph



def build_Lje_cy(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    long_slope_offset = radius / 14

    glyph = init_glyph("Lje-cy", 0x0409)

    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (100, 100),
                (150 - long_slope_offset, 800 - radius),
                (350, 800 - radius),
                (350, radius),
                (500 - diagonal_offset, radius),
                (600 - radius, 100 + diagonal_offset),

                # Preserve 45° approach to fixed y=400
                (600 - radius, 300 + middle_offset),
                (500 - diagonal_offset, 400),

                # Structural middle line stays fixed
                (350, 400),
            ],
        )
    )

    return glyph


def build_Nje_cy(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("Nje-cy", 0x040A)

    # Left stem
    glyph.add(
        line(
            width,
            (radius, radius),
            (radius, 800 - radius),
        )
    )

    # Structural middle line stays at y = 400
    glyph.add(
        line(
            width,
            (radius, 400),
            (350, 400),
        )
    )

    # Right stem + lower bowl
    glyph.add(
        polyline(
            width,
            [
                (350, 800 - radius),
                (350, radius),
                (500 - diagonal_offset, radius),
                (600 - radius, 100 + diagonal_offset),

                # Preserve 45° approach to fixed y = 400
                (600 - radius, 300 + middle_offset),
                (500 - diagonal_offset, 400),

                (350, 400),
            ],
        )
    )

    return glyph


def build_Tshe_cy(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset
    glyph = init_glyph("Tshe-cy", 0x040B)
    # glyph = init_glyph("Dje-cy", 0x0402)

    glyph.add(
        line(
            width,
            (radius, 800 - radius),
            (400 - radius, 800 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (200, 800 - radius),
            (200, radius),
        )
    )

    glyph.add(
        polyline(
            width,
            [
                # Preserve 45° transition from stem into shoulder
                (200, 400 - middle_offset),
                (300 - diagonal_offset, 500 - radius),

                (500 - diagonal_offset, 500 - radius),

                # Upper-right 45°
                (600 - radius, 400 - diagonal_offset),

                # Right vertical
                (600 - radius, radius),
            ],
        )
    )

    return glyph


def build_Dzhe_cy(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("Dzhe-cy", 0x040F)

    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (radius, radius),
                (600 - radius, radius),
                (600 - radius, 800 - radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (300, radius),
            (300, -200 + radius),
        )
    )

    return glyph


def build_Gestroke_cy(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("Gestroke-cy", 0x0492)

    glyph.add(
        polyline(
            width,
            [
                (150, radius),
                (150, 800 - radius),
                (600 - radius, 800 - radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (radius, 400),
            (400 - radius, 400),
        )
    )

    return glyph


def build_Zhedescender_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("Zhedescender-cy", 0x0496)

    radius = width / 2
    middle_offset = (5 / 8) * radius

    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (150 + middle_offset, 400),
                (radius, radius),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 800 - radius),
                (450 - middle_offset, 400),
                (600 - radius, radius),
                (675 - radius, radius),
                (675 - radius, -200 + radius)
            ],
        )
    )

    glyph.add(
        line(
            width,
            (300, 800 - radius),
            (300, radius),
        )
    )

    glyph.add(
        line(
            width,
            (150 + middle_offset, 400),
            (450 - middle_offset, 400),
        )
    )

    return glyph


def build_Kadescender_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("Kadescender-cy", 0x049A)
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    notch_offset = math.sqrt(2) * radius

    glyph.add(
        line(
            width,
            (radius, radius),
            (radius, 800 - radius),
        )
    )
    glyph.add(
        line(
            width,
            (radius, 400),
            (400 - notch_offset, 400),
        )
    )
    glyph.add(
        polyline(
            width,
            [   
                (675 - radius, -200 + radius),
                (675 - radius, radius),
                (600 - radius, radius),
                (600 - radius, 200 - diagonal_offset),
                (400 - notch_offset, 400),
                (600 - radius, 600 + diagonal_offset),
                (600 - radius, 800 - radius),
            ],
        )
    )
    return glyph


def build_Endescender_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("Endescender-cy", 0x04A2)
    radius = width / 2

    glyph.add(
        line(
            width,
            (radius, radius),
            (radius, 800 - radius),
        )
    )
    glyph.add(
        polyline(
            width,
            [
                (675 - radius, -200 + radius),
                (675 - radius, radius),
                (600 - radius, radius),
                (600 - radius, 800 - radius),
            ]
        )
    )
    glyph.add(
        line(
            width,
            (radius, 400),
            (600 - radius, 400),
        )
    )
    return glyph


def build_Ustraight_cy(width: float) -> GlyphDefinition:
    radius = width / 2

    # Diagonal ratio 300:400 = 3:4
    diagonal_length = math.sqrt(300**2 + 400**2)
    diagonal_x_offset = (300 / diagonal_length) * radius
    diagonal_y_offset = (400 / diagonal_length) * radius

    glyph = init_glyph("Ustraight-cy", 0x04AE)

    glyph.add(
        polyline(
            width,
            [
                (
                    diagonal_x_offset,
                    800 - diagonal_y_offset,
                ),
                (300, 400),
                (
                    600 - diagonal_x_offset,
                    800 - diagonal_y_offset,
                ),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (300, 400),
            (300, radius),
        )
    )

    return glyph


def build_Ustraightstroke_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("Ustraightstroke-cy", 0x04B0)
    radius = width / 2

    # Diagonal ratio 300:400 = 3:4
    diagonal_length = math.sqrt(300**2 + 400**2)
    diagonal_x_offset = (300 / diagonal_length) * radius
    diagonal_y_offset = (400 / diagonal_length) * radius

    # glyph = init_glyph("Ustraight-cy", 0x04AE)

    glyph.add(
        polyline(
            width,
            [
                (
                    diagonal_x_offset,
                    800 - diagonal_y_offset,
                ),
                (300, 400),
                (
                    600 - diagonal_x_offset,
                    800 - diagonal_y_offset,
                ),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (300, 400),
            (300, radius),
        )
    )

    glyph.add(
        line(
            width,
            (50 + radius, 350),
            (550 - radius, 350)
        )
    )

    return glyph


def build_Hadescender_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("Hadescender-cy", 0x04B2)
    radius = width / 2
    diagonal_y_offset = (5 / 6) * radius

    # glyph = init_glyph("X", "X")
    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (radius, 650 - diagonal_y_offset),
                (600 - radius, 150 + diagonal_y_offset),
                (600 - radius, radius),
                (675 - radius, radius),
                (675 - radius, -200 + radius)
            ],
        )
    )
    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 150 + diagonal_y_offset),
                (600 - radius, 650 - diagonal_y_offset),
                (600 - radius, 800 - radius),
            ],
        )
    )
    return glyph


def build_Chedescender_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("Chedescender-cy", 0x04B6)
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    # glyph = init_glyph("Checyrillic", "Ч")

    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (radius, 450 - middle_offset),
                (150 + diagonal_offset, 300),
                (450 - diagonal_offset, 300),
                (600 - radius, 450 - middle_offset),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [ 
                (600 - radius, 800 - radius),
                (600 - radius, radius),
                (675 - radius, radius),
                (675 - radius, -200 + radius)
            ]
        )
    )

    return glyph


def build_Shha_cy(width: float) -> GlyphDefinition:
    radius = width / 2

    # Diagonal: 100 × 150
    slope_length = math.sqrt(100**2 + 150**2)

    # Compensation at vertical and horizontal boundaries
    vertical_offset = ((slope_length - 150) / 100) * radius
    horizontal_offset = ((slope_length - 100) / 150) * radius

    glyph = init_glyph("Shha-cy", 0x04BA)

    glyph.add(
        line(
            width,
            (radius, radius),
            (radius, 800 - radius),
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (radius, 350 - vertical_offset),
                (100 + horizontal_offset, 500 - radius),
                (450 - horizontal_offset, 500 - radius),
                (600 - radius, 350 - vertical_offset),
                (600 - radius, radius),
            ],
        )
    )

    return glyph


def build_Schwa_cy(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("Schwa-cy", 0x04D8)

    glyph.add(
        polyline(
            width,
            [
                (radius, 650 - diagonal_offset),
                (150 + diagonal_offset, 800 - radius),
                (450 - diagonal_offset, 800 - radius),
                (600 - radius, 650 - diagonal_offset),
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),
                (150 + diagonal_offset, radius),
                (radius, 150 + diagonal_offset),

                # Structural middle line stays at y = 400
                (radius, 400),
                (600 - radius, 400),
            ],
        )
    )

    return glyph


def build_Imacron_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("Imacron-cy", 0x04E2)
    return glyph


def build_Obarred_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("Obarred-cy", 0x04E8)
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    # glyph = init_glyph("Ocyrillic", "О")
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
            (radius, 400),
            (600 - radius, 400),
        )
    )
    return glyph


def build_Umacron_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("Umacron-cy", 0x04EE)
    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    "\u0402": build_Dje_cy,
    "\u0408": build_Je_cy,
    "\u0409": build_Lje_cy,
    "\u040A": build_Nje_cy,
    "\u040B": build_Tshe_cy,
    "\u040F": build_Dzhe_cy,
    "\u0492": build_Gestroke_cy,
    "\u0496": build_Zhedescender_cy,
    "\u049A": build_Kadescender_cy,
    "\u04A2": build_Endescender_cy,
    "\u04AE": build_Ustraight_cy,
    "\u04B0": build_Ustraightstroke_cy,
    "\u04B2": build_Hadescender_cy,
    "\u04B6": build_Chedescender_cy,
    "\u04BA": build_Shha_cy,
    "\u04D8": build_Schwa_cy,
    "\u04E2": build_Imacron_cy,
    "\u04E8": build_Obarred_cy,
    "\u04EE": build_Umacron_cy,
}


__all__ = [
    "BUILDERS",
    "build_Dje_cy",
    "build_Je_cy",
    "build_Lje_cy",
    "build_Nje_cy",
    "build_Tshe_cy",
    "build_Dzhe_cy",
    "build_Gestroke_cy",
    "build_Zhedescender_cy",
    "build_Kadescender_cy",
    "build_Endescender_cy",
    "build_Ustraight_cy",
    "build_Ustraightstroke_cy",
    "build_Hadescender_cy",
    "build_Chedescender_cy",
    "build_Shha_cy",
    "build_Schwa_cy",
    "build_Imacron_cy",
    "build_Obarred_cy",
    "build_Umacron_cy",
]
