"""Blank builders for non-ASCII core symbols."""

from __future__ import annotations

import math

from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition, dot, init_glyph, line, polygon, polyline

def build_cent(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("cent", 0x00A2)

    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 450 - diagonal_offset),
                (450 - diagonal_offset, 600 - radius),
                (150 + diagonal_offset, 600 - radius),
                (radius, 450 - diagonal_offset),
                (radius, 150 + diagonal_offset),
                (150 + diagonal_offset, radius),
                (450 - diagonal_offset, radius),
                (600 - radius, 150 + diagonal_offset),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (300, 700 - radius),
            (300, -100 + radius),
        )
    )

    return glyph


def build_sterling(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("sterling", 0x00A3)

    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 700 - diagonal_offset),
                (500 - diagonal_offset, 800 - radius),
                (250 + diagonal_offset, 800 - radius),
                (150 + radius, 700 - diagonal_offset),
                (150 + radius, 150 + radius),
                (radius, radius),
                (600 - radius, radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (radius, 400),
            (500 - radius, 400),
        )
    )

    return glyph


def build_yen(width: float) -> GlyphDefinition:
    radius = width / 2

    diagonal_length = math.sqrt(300**2 + 400**2)
    diagonal_x_offset = (300 / diagonal_length) * radius
    diagonal_y_offset = (400 / diagonal_length) * radius

    glyph = init_glyph("yen", 0x00A5)

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
            (550 - radius, 350),
        )
    )

    glyph.add(
        line(
            width,
            (50 + radius, 150),
            (550 - radius, 150),
        )
    )

    return glyph


def build_copyright(width: float) -> GlyphDefinition:
    width = width * 0.8
    
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    endpoint_offset = radius / math.sqrt(2)

    glyph = init_glyph("copyright", 0x00A9)

    glyph.add(
        polyline(
            width,
            [
                (radius, 400),
                (radius, 700 - diagonal_offset),
                (100 + diagonal_offset, 800 - radius),
                (500 - diagonal_offset, 800 - radius),
                (600 - radius, 700 - diagonal_offset),
                (600 - radius, 100 + diagonal_offset),
                (500 - diagonal_offset, radius),
                (100 + diagonal_offset, radius),
                (radius, 100 + diagonal_offset),
                (radius, 400),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (450 - endpoint_offset, 600 - endpoint_offset),
                (400 - diagonal_offset, 650 - radius),
                (200 + diagonal_offset, 650 - radius),
                (150 + radius, 600 - diagonal_offset),
                (150 + radius, 200 + diagonal_offset),
                (200 + diagonal_offset, 150 + radius),
                (400 - diagonal_offset, 150 + radius),
                (450 - endpoint_offset, 200 + endpoint_offset),
            ],
        )
    )

    return glyph


def build_registered(width: float) -> GlyphDefinition:
    width = width * 0.8
    
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("registered", 0x00AE)

    # Outer ring
    glyph.add(
        polyline(
            width,
            [
                (radius, 400),
                (radius, 700 - diagonal_offset),
                (100 + diagonal_offset, 800 - radius),
                (500 - diagonal_offset, 800 - radius),
                (600 - radius, 700 - diagonal_offset),
                (600 - radius, 100 + diagonal_offset),
                (500 - diagonal_offset, radius),
                (100 + diagonal_offset, radius),
                (radius, 100 + diagonal_offset),
                (radius, 400),
            ],
        )
    )

    # Inner R
    glyph.add(
        polyline(
            width,
            [
                (150 + radius, 150 + radius),
                (150 + radius, 650 - radius),
                (400 - diagonal_offset, 650 - radius),
                (450 - radius, 600 - diagonal_offset),
                (450 - radius, 500 - middle_offset),
                (350 - diagonal_offset, 400),
                (450 - radius, 300 + middle_offset),
                (450 - radius, 150 + radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (150 + radius, 400),
            (350 - diagonal_offset, 400),
        )
    )

    return glyph

def build_degree(width: float) -> GlyphDefinition:
    radius = width / 2
    ring_scale = (300 - radius) / 300

    width = width * 9 / 10

    glyph = init_glyph("degree", 0x00B0)

    # Same ring geometry as percent, shifted +150 on x
    glyph.add(
        polygon(
            width,
            [
                (150 + radius, 500 + 150 * ring_scale),
                (150 + radius, 500 + 200 * ring_scale),
                (150 + radius + 100 * ring_scale, 800 - radius),
                (150 + radius + 200 * ring_scale, 800 - radius),
                (450, 500 + 200 * ring_scale),
                (450, 500 + 100 * ring_scale),
                (150 + radius + 200 * ring_scale, 500),
                (150 + radius + 100 * ring_scale, 500),
                (150 + radius, 500 + 100 * ring_scale),
            ],
        )
    )

    return glyph

# def build_degree(width: float) -> GlyphDefinition:
#     radius = width / 2
#     diagonal_offset = (math.sqrt(2) - 1) * radius

#     glyph = init_glyph("degree", 0x00B0)

#     glyph.add(
#         polyline(
#             width,
#             [
#                 (150 + radius, 650),
#                 (150 + radius, 750 - diagonal_offset),
#                 (200 + diagonal_offset, 800 - radius),
#                 (400 - diagonal_offset, 800 - radius),
#                 (450 - radius, 750 - diagonal_offset),
#                 (450 - radius, 550 + diagonal_offset),
#                 (400 - diagonal_offset, 500 + radius),
#                 (200 + diagonal_offset, 500 + radius),
#                 (150 + radius, 550 + diagonal_offset),
#                 (150 + radius, 650),
#             ],
#         )
#     )

#     return glyph


def build_multiply(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (250 - radius) / math.sqrt(2)

    glyph = init_glyph("multiply", 0x00D7)

    glyph.add(
        line(
            width,
            (300 - diagonal_offset, 300 - diagonal_offset),
            (300 + diagonal_offset, 300 + diagonal_offset),
        )
    )

    glyph.add(
        line(
            width,
            (300 - diagonal_offset, 300 + diagonal_offset),
            (300 + diagonal_offset, 300 - diagonal_offset),
        )
    )

    return glyph


def build_divide(width: float) -> GlyphDefinition:
    radius = width / 2
    dot_width = width * 1.5

    glyph = init_glyph("divide", 0x00F7)

    glyph.add(
        line(
            width,
            (50 + radius, 300),
            (550 - radius, 300),
        )
    )

    glyph.add(
        dot(
            dot_width * 0.8,
            (300, 100),
        )
    )

    glyph.add(
        dot(
            dot_width * 0.8,
            (300, 500),
        )
    )

    return glyph


def build_euro(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("euro", 0x20AC)

    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 700 - diagonal_offset),
                (500 - diagonal_offset, 800 - radius),
                (250 + diagonal_offset, 800 - radius),
                (150 + radius, 700 - diagonal_offset),
                (150 + radius, 100 + diagonal_offset),
                (250 + diagonal_offset, radius),
                (500 - diagonal_offset, radius),
                (600 - radius, 100 + diagonal_offset),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (radius, 500),
            (450 - radius, 500),
        )
    )

    glyph.add(
        line(
            width,
            (radius, 300),
            (450 - radius, 300),
        )
    )

    return glyph


def build_numero(width: float) -> GlyphDefinition:
    n_width = width * 0.80
    n_radius = n_width / 2

    mark_width = width * 0.70
    mark_radius = mark_width / 2
    diagonal_offset = (math.sqrt(2) - 1) * mark_radius

    glyph = init_glyph("numero", 0x2116)

    # N
    glyph.add(
        polyline(
            n_width,
            [
                (n_radius, n_radius),
                (n_radius, 800 - n_radius),
                (300 - n_radius, n_radius),
                (300 - n_radius, 800 - n_radius),
            ],
        )
    )

    # Raised o
    glyph.add(
        polyline(
            mark_width,
            [
                (350 + mark_radius, 700),
                (350 + mark_radius, 750 - diagonal_offset),
                (400 + diagonal_offset, 800 - mark_radius),
                (550 - diagonal_offset, 800 - mark_radius),
                (600 - mark_radius, 750 - diagonal_offset),
                (600 - mark_radius, 600 + diagonal_offset),
                (550 - diagonal_offset, 550 + mark_radius),
                (400 + diagonal_offset, 550 + mark_radius),
                (350 + mark_radius, 600 + diagonal_offset),
                (350 + mark_radius, 700),
            ],
        )
    )

    # Underline
    glyph.add(
        line(
            mark_width,
            (350 + mark_radius, 400),
            (600 - mark_radius, 400),
        )
    )

    return glyph


def build_trademark(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("trademark", 0x2122)

    # M
    glyph.add(
        polyline(
            width * 0.8,
            [
                (350, 450 + radius),
                (350, 800 - radius),
                (475, 650 - radius),
                (600, 800 - radius),
                (600, 450 + radius),
            ],
        )
    )

    # T
    glyph.add(
        line(
            width * 0.8,
            (radius, 800 - radius),
            (250 - radius, 800 - radius),
        )
    )

    glyph.add(
        line(
            width * 0.8,
            (125, 800 - radius),
            (125, 450 + radius),
        )
    )

    return glyph


def build_minus(width: float) -> GlyphDefinition:
    radius = width / 2
    
    glyph = init_glyph("minus", 0x2212)

    glyph.add(
        line(
            width,
            (50 + radius, 300),
            (550 - radius, 300)
        )
    )

    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    "\u00A2": build_cent,
    "\u00A3": build_sterling,
    "\u00A5": build_yen,
    "\u00A9": build_copyright,
    "\u00AE": build_registered,
    "\u00B0": build_degree,
    "\u00D7": build_multiply,
    "\u00F7": build_divide,
    "\u20AC": build_euro,
    "\u2116": build_numero,
    "\u2122": build_trademark,
    "\u2212": build_minus,
}


__all__ = [
    "BUILDERS",
    "build_cent",
    "build_sterling",
    "build_yen",
    "build_copyright",
    "build_registered",
    "build_degree",
    "build_multiply",
    "build_divide",
    "build_euro",
    "build_numero",
    "build_trademark",
    "build_minus",
]
