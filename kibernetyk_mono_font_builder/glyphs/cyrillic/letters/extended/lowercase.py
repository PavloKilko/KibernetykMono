"""Blank builders for lowercase Cyrillic Core additions."""

from __future__ import annotations

import math

from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition, dot, init_glyph, line, polygon, polyline


def build_dje_cy(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("djecyrillic", 0x0452)

    glyph.add(
        line(
            width,
            (200, 800 - radius),
            (200, radius),
        )
    )

    glyph.add(
        line(
            width,
            (radius, 600),
            (450 - radius, 600),
        )
    )

    glyph.add(
        polyline(
            width,
            [
                # Preserve 45° transition from stem into shoulder
                (200, 300 - middle_offset),
                (300 - diagonal_offset, 400 - radius),

                (500 - diagonal_offset, 400 - radius),

                # Upper-right 45°
                (600 - radius, 300 - diagonal_offset),

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


def build_je_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("jecyrillic", 0x0458)
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    # glyph = init_glyph("j", "j")
    glyph.add(
        dot(
            width * 1.25,
            (400, 800),
        )
    )
    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (400, 600 - radius),
                (400, -50 + radius - diagonal_offset),
                (250 + diagonal_offset, -200 + radius),
                (radius, -200 + radius),
            ],
        )
    )
    return glyph


def build_lje_cy(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    # Preserve the original 50:500 = 1:10 slope
    long_slope_offset = radius / 10

    glyph = init_glyph("ljecyrillic", 0x0459)

    glyph.add(
        polyline(
            width,
            [
                # Lower-left 45° diagonal
                (radius, radius),
                (100, 100),

                # Long rising diagonal
                (150 - long_slope_offset, 600 - radius),

                # Main stem
                (350, 600 - radius),
                (350, radius),

                # Lower bowl
                (500 - diagonal_offset, radius),
                (600 - radius, 100 + diagonal_offset),

                # Preserve 45° approach to structural y = 300
                (600 - radius, 200 + middle_offset),
                (500 - diagonal_offset, 300),

                # Structural middle line stays fixed
                (350, 300),
            ],
        )
    )

    return glyph


def build_nje_cy(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("njecyrillic", 0x045A)

    # Left stem
    glyph.add(
        line(
            width,
            (radius, radius),
            (radius, 600 - radius),
        )
    )

    # Structural middle line stays at y = 300
    glyph.add(
        line(
            width,
            (radius, 300),
            (350, 300),
        )
    )

    # Right stem + lower bowl
    glyph.add(
        polyline(
            width,
            [
                (350, 600 - radius),
                (350, radius),
                (500 - diagonal_offset, radius),
                (600 - radius, 100 + diagonal_offset),

                # Preserve 45° approach to fixed y = 300
                (600 - radius, 200 + middle_offset),
                (500 - diagonal_offset, 300),

                (400, 300),
            ],
        )
    )

    return glyph

def build_tshe_cy(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("tshecyrillic", 0x045B)

    glyph.add(
        line(
            width,
            (radius, 600),
            (450 - radius, 600),
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
                # Preserve 45° transition into upper bowl
                (200, 300 - middle_offset),
                (300 - diagonal_offset, 400 - radius),

                (500 - diagonal_offset, 400 - radius),

                # Preserve upper-right 45°
                (600 - radius, 300 - diagonal_offset),

                # Right vertical
                (600 - radius, radius),
            ],
        )
    )

    return glyph


def build_dzhe_cy(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("dzhecyrillic", 0x045F)

    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (radius, radius),
                (600 - radius, radius),
                (600 - radius, 600 - radius),
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


def build_gestroke_cy(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("gestrokecyrillic", 0x0493)

    glyph.add(
        line(
            width,
            (radius, 300),
            (400 - radius, 300),
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (150, radius),
                (150, 600 - radius),
                (600 - radius, 600 - radius),
            ],
        )
    )

    return glyph

def build_zhedescender_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("zhedescendercyrillic", 0x0497)
    radius = width / 2

    # Original diagonals:
    # (0, 600) -> (150, 300) and (150, 300) -> (0, 0)
    # Δx:Δy = 150:300 = 1:2
    #
    # With outer endpoints compensated inward by `radius`,
    # the middle junction must move by `radius / 2`
    # to preserve the original slope.
    middle_offset = radius / 2

    # glyph = init_glyph("zhecyrillic", "ж")

    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (150 + middle_offset, 300),
                (radius, radius),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 600 - radius),
                (450 - middle_offset, 300),
                (600 - radius, radius),
                (675 - radius, radius),
                (675 - radius, -200 + radius)
            ],
        )
    )

    glyph.add(
        line(
            width,
            (300, 600 - radius),
            (300, radius),
        )
    )

    glyph.add(
        line(
            width,
            (150 + middle_offset, 300),
            (450 - middle_offset, 300),
        )
    )

    return glyph


def build_kadescender_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("kadescendercyrillic", 0x049B)
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    notch_offset = math.sqrt(2) * radius

    # glyph = init_glyph("kacyrillic", "к")
    glyph.add(
        line(
            width,
            (radius, radius),
            (radius, 600 - radius),
        )
    )
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 600 - radius),
                (600 - radius, 500 + diagonal_offset),
                (400 - notch_offset, 300),
                (600 - radius, 100 - diagonal_offset),
                (600 - radius, radius),
                (675 - radius, radius),
                (675 - radius, -200 + radius)
            ],
        )
    )
    glyph.add(
        line(
            width,
            (radius, 300),
            (400 - notch_offset, 300),
        )
    )
    return glyph


def build_endescender_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("endescendercyrillic", 0x04A3)
    radius = width / 2
    # glyph = init_glyph("encyrillic", "н")
    glyph.add(
        line(
            width,
            (radius, radius),
            (radius, 600 - radius)
        )
    )
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 600 - radius),
                (600 - radius, radius),
                (675 - radius, radius),
                (675 - radius, -200 + radius)
            ]
        )
    )
    glyph.add(
        line(
            width,
            (radius, 300),
            (600 - radius, 300)
        )
    )
    return glyph


def build_ustraight_cy(width: float) -> GlyphDefinition:
    radius = width / 2

    # Diagonal ratio 300:600 = 1:2
    diagonal_length = math.sqrt(300**2 + 600**2)
    diagonal_x_offset = (300 / diagonal_length) * radius
    diagonal_y_offset = (600 / diagonal_length) * radius

    glyph = init_glyph("ustraightcyrillic", 0x04AF)

    glyph.add(
        polyline(
            width,
            [
                (
                    diagonal_x_offset,
                    600 - diagonal_y_offset,
                ),
                (300, 0),
                (
                    600 - diagonal_x_offset,
                    600 - diagonal_y_offset,
                ),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (300, 0),
            (300, -200 + radius),
        )
    )

    return glyph


def build_ustraightstroke_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("ustraightstrokecyrillic", 0x04B1)
    radius = width / 2

    # Diagonal ratio 300:600 = 1:2
    diagonal_length = math.sqrt(300**2 + 600**2)
    diagonal_x_offset = (300 / diagonal_length) * radius
    diagonal_y_offset = (600 / diagonal_length) * radius

    # glyph = init_glyph("ustraightcyrillic", 0x04AF)

    glyph.add(
        polyline(
            width,
            [
                (
                    diagonal_x_offset,
                    600 - diagonal_y_offset,
                ),
                (300, 0),
                (
                    600 - diagonal_x_offset,
                    600 - diagonal_y_offset,
                ),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (300, 0),
            (300, -200 + radius),
        )
    )

    glyph.add(
        line(
            width,
            (100 + radius, -50),
            (500 - radius, -50)
        )
    )

    return glyph


def build_hadescender_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("hadescendercyrillic", 0x04B3)
    radius = width / 2
    diagonal_y_offset = (5 / 6) * radius

    # glyph = init_glyph("khacyrillic", "х")
    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (radius, 550 - diagonal_y_offset),
                (600 - radius, 50 + diagonal_y_offset),
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
                (radius, 50 + diagonal_y_offset),
                (600 - radius, 550 - diagonal_y_offset),
                (600 - radius, 600 - radius),
            ],
        )
    )
    return glyph


def build_chedescender_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("chedescendercyrillic", 0x04B7)
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    # glyph = init_glyph("checyrillic", "ч")

    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (radius, 350 - middle_offset),
                (150 + diagonal_offset, 200),
                (450 - diagonal_offset, 200),
                (600 - radius, 350 - middle_offset),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 600 - radius),
                (600 - radius, radius),
                (675 - radius, radius),
                (675 - radius, -200 + radius)
            ]
        )
    )

    return glyph


def build_shha_cy(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("shhacyrillic", 0x04BB)

    glyph.add(
        line(
            width,
            (radius, 600 - radius),
            (radius, radius),
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (radius, 250 - diagonal_offset),
                (150 + diagonal_offset, 400 - radius),
                (450 - diagonal_offset, 400 - radius),
                (600 - radius, 250 - diagonal_offset),
                (600 - radius, radius),
            ],
        )
    )

    return glyph


def build_schwa_cy(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("schwacyrillic", 0x04D9)

    glyph.add(
        polyline(
            width,
            [
                (radius, 500 - diagonal_offset),
                (100 + diagonal_offset, 600 - radius),
                (500 - diagonal_offset, 600 - radius),
                (600 - radius, 500 - diagonal_offset),
                (600 - radius, 100 + diagonal_offset),
                (500 - diagonal_offset, radius),
                (100 + diagonal_offset, radius),
                (radius, 100 + diagonal_offset),

                # Structural middle line stays fixed at y = 300
                (radius, 300),
                (600 - radius, 300),
            ],
        )
    )

    return glyph


def build_imacron_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("imacroncyrillic", 0x04E3)
    return glyph


def build_obarred_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("obarredcyrillic", 0x04E9)
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    # glyph = init_glyph("ocyrillic", "о")
    glyph.add(
        polyline(
            width,
            [
                (radius, 300),
                (radius, 450 - diagonal_offset),
                (150 + diagonal_offset, 600 - radius),
                (450 - diagonal_offset, 600 - radius),
                (600 - radius, 450 - diagonal_offset),
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),
                (150 + diagonal_offset, radius),
                (radius, 150 + diagonal_offset),
                (radius, 300),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (radius, 300),
            (600 - radius, 300)
        )
    )
    return glyph


def build_umacron_cy(width: float) -> GlyphDefinition:
    glyph = init_glyph("umacroncyrillic", 0x04EF)
    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    "\u0452": build_dje_cy,
    "\u0458": build_je_cy,
    "\u0459": build_lje_cy,
    "\u045A": build_nje_cy,
    "\u045B": build_tshe_cy,
    "\u045F": build_dzhe_cy,
    "\u0493": build_gestroke_cy,
    "\u0497": build_zhedescender_cy,
    "\u049B": build_kadescender_cy,
    "\u04A3": build_endescender_cy,
    "\u04AF": build_ustraight_cy,
    "\u04B1": build_ustraightstroke_cy,
    "\u04B3": build_hadescender_cy,
    "\u04B7": build_chedescender_cy,
    "\u04BB": build_shha_cy,
    "\u04D9": build_schwa_cy,
    "\u04E3": build_imacron_cy,
    "\u04E9": build_obarred_cy,
    "\u04EF": build_umacron_cy,
}


__all__ = [
    "BUILDERS",
    "build_dje_cy",
    "build_je_cy",
    "build_lje_cy",
    "build_nje_cy",
    "build_tshe_cy",
    "build_dzhe_cy",
    "build_gestroke_cy",
    "build_zhedescender_cy",
    "build_kadescender_cy",
    "build_endescender_cy",
    "build_ustraight_cy",
    "build_ustraightstroke_cy",
    "build_hadescender_cy",
    "build_chedescender_cy",
    "build_shha_cy",
    "build_schwa_cy",
    "build_imacron_cy",
    "build_obarred_cy",
    "build_umacron_cy",
]
