"""Blank builders for non-ASCII core punctuation."""

from __future__ import annotations

import math

from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition, dot, init_glyph, line, polygon, polyline

def build_exclamdown(width: float) -> GlyphDefinition:
    radius = width / 2
    dot_width = width * 1.5

    glyph = init_glyph("exclamdown", 0x00A1)

    glyph.add(
        dot(
            dot_width,
            (300, 600),
        )
    )

    glyph.add(
        line(
            width,
            (300, 400 - radius),
            (300, -200 + radius),
        )
    )

    return glyph


def build_section(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    # Extra correction required by the connecting 45° diagonals
    junction_offset = 2 * radius - diagonal_offset

    glyph = init_glyph("section", 0x00A7)

    shared_upper = (
        200 + diagonal_offset,
        500 - radius,
    )

    shared_lower = (
        400 - diagonal_offset,
        100 + radius,
    )

    # Center loop
    glyph.add(
        polyline(
            width,
            [
                (300, 100 + radius),
                (200 + diagonal_offset, 100 + radius),
                (100 + radius, 200 + diagonal_offset),
                (100 + radius, 400 - diagonal_offset),
                shared_upper,
                (400 - diagonal_offset, 500 - radius),
                (500 - radius, 400 - diagonal_offset),
                (500 - radius, 200 + diagonal_offset),
                shared_lower,
                (300, 100 + radius),
            ],
        )
    )

    # Upper section
    glyph.add(
        polyline(
            width,
            [
                shared_upper,
                (100 + radius, 600 - junction_offset),
                (100 + radius, 700 - diagonal_offset),
                (200 + diagonal_offset, 800 - radius),
                (400 - diagonal_offset, 800 - radius),
                (500 - radius, 700 - diagonal_offset),
            ],
        )
    )

    # Lower section
    glyph.add(
        polyline(
            width,
            [
                shared_lower,
                (500 - radius, junction_offset),
                (500 - radius, -100 + diagonal_offset),
                (400 - diagonal_offset, -200 + radius),
                (200 + diagonal_offset, -200 + radius),
                (100 + radius, -100 + diagonal_offset),
            ],
        )
    )

    return glyph


def build_guillemetleft(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("guillemetleft", 0x00AB)

    # First chevron: diagonal ratio 200:250
    outer_length = math.sqrt(200**2 + 250**2)
    outer_x_offset = (200 / outer_length) * radius
    outer_y_offset = (250 / outer_length) * radius

    glyph.add(
        polyline(
            width,
            [
                (
                    300 - outer_x_offset,
                    600 - outer_y_offset,
                ),
                (100, 350),
                (
                    300 - outer_x_offset,
                    100 + outer_y_offset,
                ),
            ],
        )
    )

    # Second chevron: 45° diagonals
    inner_offset = radius / math.sqrt(2)

    glyph.add(
        polyline(
            width,
            [
                (
                    500 - inner_offset,
                    500 - inner_offset,
                ),
                (350, 350),
                (
                    500 - inner_offset,
                    200 + inner_offset,
                ),
            ],
        )
    )

    return glyph


def build_paragraph(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("paragraph", 0x00B6)

    glyph.add(
        polygon(
            width,
            [
                (250, 300 + radius),
                (100 + diagonal_offset, 300 + radius),
                (radius, 400 + diagonal_offset),
                (radius, 700 - diagonal_offset),
                (100 + diagonal_offset, 800 - radius),
                (250, 800 - radius),
            ],
            fill=True
        )
    )

    glyph.add(
        line(
            width,
            (250, 300 + radius),
            (250, -200 + radius),
        )
    )

    glyph.add(
        line(
            width,
            (450, 800 - radius),
            (450, -200 + radius),
        )
    )

    return glyph


def build_periodcentered(width: float) -> GlyphDefinition:
    dot_width = width * 1.5

    glyph = init_glyph("periodcentered", 0x00B7)

    glyph.add(
        dot(
            dot_width,
            (300, 300),
        )
    )

    return glyph


def build_guillemetright(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("guillemetright", 0x00BB)

    # First chevron: 45° diagonals
    inner_offset = radius / math.sqrt(2)

    glyph.add(
        polyline(
            width,
            [
                (
                    100 + inner_offset,
                    500 - inner_offset,
                ),
                (250, 350),
                (
                    100 + inner_offset,
                    200 + inner_offset,
                ),
            ],
        )
    )

    # Second chevron: diagonal ratio 200:250
    outer_length = math.sqrt(200**2 + 250**2)
    outer_x_offset = (200 / outer_length) * radius
    outer_y_offset = (250 / outer_length) * radius

    glyph.add(
        polyline(
            width,
            [
                (
                    300 + outer_x_offset,
                    600 - outer_y_offset,
                ),
                (500, 350),
                (
                    300 + outer_x_offset,
                    100 + outer_y_offset,
                ),
            ],
        )
    )

    return glyph


def build_questiondown(width: float) -> GlyphDefinition:
    radius = width / 2
    dot_width = width * 1.25
    dot_radius = dot_width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    slant_y_offset = (2 / 3) * radius

    y_offset = -200

    glyph = init_glyph("questiondown", 0x00BF)

    glyph.add(
        dot(
            dot_width,
            (300, 800 - dot_radius + y_offset),
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (300, 550 - radius + y_offset),
                (300, 450 + y_offset),
                (radius, 250 + slant_y_offset + y_offset),
                (radius, 150 + diagonal_offset + y_offset),
                (150 + diagonal_offset, radius + y_offset),
                (450 - diagonal_offset, radius + y_offset),
                (600 - radius, 150 + diagonal_offset + y_offset),
            ],
        )
    )

    return glyph


def build_apostrophemod(width: float) -> GlyphDefinition:
    dot_width = width * 1.5
    dot_radius = dot_width / 2

    tail_width = dot_radius
    tail_radius = tail_width / 2

    # Align visible right edge of tail with visible right edge of dot
    tail_x = 300 + dot_radius - tail_radius

    # Move comma shape so dot center is at (300, 800)
    y_offset = 800 - dot_radius

    glyph = init_glyph("apostrophemod", 0x02BC)

    glyph.add(
        dot(
            dot_width,
            (300, 800),
        )
    )

    glyph.add(
        polyline(
            tail_width,
            [
                (tail_x, 800),
                (tail_x, -100 + tail_radius + y_offset),
                (tail_x - 50, -150 + tail_radius + y_offset),
                (
                    300 - dot_radius + tail_radius,
                    -150 + tail_radius + y_offset,
                ),
            ],
        )
    )

    return glyph


def build_endash(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("endash", 0x2013)

    glyph.add(
        line(
            width,
            (50 + radius, 300),
            (550 - radius, 300),
        )
    )

    return glyph


def build_emdash(width: float) -> GlyphDefinition:
    radius = width / 2
    
    glyph = init_glyph("emdash", 0x2014)
    
    glyph.add(
        line(
            width,
            (radius, 300),
            (600 - radius, 300),
        )
    )

    return glyph


def build_quoteleft(width: float) -> GlyphDefinition:
    dot_width = width * 1.5
    dot_radius = dot_width / 2

    tail_width = dot_radius
    tail_radius = tail_width / 2

    # Align visible left edge of tail with visible left edge of dot
    tail_x = 300 - dot_radius + tail_radius

    glyph = init_glyph("quoteleft", 0x2018)

    glyph.add(
        dot(
            dot_width,
            (300, 600),
        )
    )

    glyph.add(
        polyline(
            tail_width,
            [
                (tail_x, 600),
                (tail_x, 700 + dot_radius - tail_radius),
                (tail_x + 50, 750 + dot_radius - tail_radius),
                (300 + dot_radius - tail_radius, 750 + dot_radius - tail_radius),
            ],
        )
    )

    return glyph


def build_quoteright(width: float) -> GlyphDefinition:
    dot_width = width * 1.5
    dot_radius = dot_width / 2

    tail_width = dot_radius
    tail_radius = tail_width / 2

    # Align visible right edge of tail with visible right edge of dot
    tail_x = 300 + dot_radius - tail_radius

    # Move comma shape so dot center is at (300, 800)
    y_offset = 800 - dot_radius

    glyph = init_glyph("quoteright", 0x2019)

    glyph.add(
        dot(
            dot_width,
            (300, 800),
        )
    )

    glyph.add(
        polyline(
            tail_width,
            [
                (tail_x, 800),
                (tail_x, -100 + tail_radius + y_offset),
                (tail_x - 50, -150 + tail_radius + y_offset),
                (
                    300 - dot_radius + tail_radius,
                    -150 + tail_radius + y_offset,
                ),
            ],
        )
    )

    return glyph


def build_quotesinglbase(width: float) -> GlyphDefinition:
    dot_width = width * 1.5
    dot_radius = dot_width / 2

    tail_width = dot_radius
    tail_radius = tail_width / 2

    # Align visible right edge of tail with visible right edge of dot
    tail_x = 300 + dot_radius - tail_radius

    glyph = init_glyph("quotesinglbase", 0x201A)

    glyph.add(
        dot(
            dot_width,
            (300, dot_radius),
        )
    )

    glyph.add(
        polyline(
            tail_width,
            [
                (tail_x, dot_radius),
                (tail_x, -100 + tail_radius),
                (tail_x - 50, -150 + tail_radius),
                (300 - dot_radius + tail_radius, -150 + tail_radius),
            ],
        )
    )

    return glyph


def build_quotedblleft(width: float) -> GlyphDefinition:
    dot_width = width * 1.5
    dot_radius = dot_width / 2

    tail_width = dot_radius
    tail_radius = tail_width / 2

    glyph = init_glyph("quotedblleft", 0x201C)

    for dot_x in (150, 450):
        # Align visible left edge of tail with visible left edge of dot
        tail_x = dot_x - dot_radius + tail_radius

        glyph.add(
            dot(
                dot_width,
                (dot_x, 600),
            )
        )

        glyph.add(
            polyline(
                tail_width,
                [
                    (tail_x, 600),
                    (tail_x, 700 + dot_radius - tail_radius),
                    (tail_x + 50, 750 + dot_radius - tail_radius),
                    (
                        dot_x + dot_radius - tail_radius,
                        750 + dot_radius - tail_radius,
                    ),
                ],
            )
        )

    return glyph


def build_quotedblright(width: float) -> GlyphDefinition:
    dot_width = width * 1.5
    dot_radius = dot_width / 2

    tail_width = dot_radius
    tail_radius = tail_width / 2

    y_offset = 800 - dot_radius

    glyph = init_glyph("quotedblright", 0x201D)

    for dot_x in (150, 450):
        # Align visible right edge of tail with visible right edge of dot
        tail_x = dot_x + dot_radius - tail_radius

        glyph.add(
            dot(
                dot_width,
                (dot_x, 800),
            )
        )

        glyph.add(
            polyline(
                tail_width,
                [
                    (tail_x, 800),
                    (tail_x, -100 + tail_radius + y_offset),
                    (tail_x - 50, -150 + tail_radius + y_offset),
                    (
                        dot_x - dot_radius + tail_radius,
                        -150 + tail_radius + y_offset,
                    ),
                ],
            )
        )

    return glyph

def build_quotedblbase(width: float) -> GlyphDefinition:
    dot_width = width * 1.5
    dot_radius = dot_width / 2

    tail_width = dot_radius
    tail_radius = tail_width / 2

    glyph = init_glyph("quotedblbase", 0x201E)

    for dot_x in (150, 450):
        # Keep visible bottom of dot at y = 0
        dot_y = dot_radius

        # Align visible right edge of tail with visible right edge of dot
        tail_x = dot_x + dot_radius - tail_radius

        glyph.add(
            dot(
                dot_width,
                (dot_x, dot_y),
            )
        )

        glyph.add(
            polyline(
                tail_width,
                [
                    (tail_x, dot_y),
                    (tail_x, -100 + tail_radius),
                    (tail_x - 50, -150 + tail_radius),
                    (
                        dot_x - dot_radius + tail_radius,
                        -150 + tail_radius,
                    ),
                ],
            )
        )

    return glyph


def build_bullet(width: float) -> GlyphDefinition:
    dot_width = width * 3

    glyph = init_glyph("bullet", 0x2022)

    glyph.add(
        dot(
            dot_width,
            (300, 300),
        )
    )

    return glyph


def build_ellipsis(width: float) -> GlyphDefinition:
    dot_width = width * 1.25
    dot_radius = dot_width / 2

    glyph = init_glyph("ellipsis", 0x2026)

    for dot_x in (50, 300, 550):
        glyph.add(
            dot(
                dot_width,
                (dot_x, dot_radius),
            )
        )

    return glyph


def build_guilsinglleft(width: float) -> GlyphDefinition:
    radius = width / 2

    diagonal_length = math.sqrt(200**2 + 250**2)
    x_offset = (200 / diagonal_length) * radius
    y_offset = (250 / diagonal_length) * radius

    glyph = init_glyph("guilsinglleft", 0x2039)

    glyph.add(
        polyline(
            width,
            [
                (
                    400 - x_offset,
                    600 - y_offset,
                ),
                (200, 350),
                (
                    400 - x_offset,
                    100 + y_offset,
                ),
            ],
        )
    )

    return glyph


def build_guilsinglright(width: float) -> GlyphDefinition:
    radius = width / 2

    diagonal_length = math.sqrt(200**2 + 250**2)
    x_offset = (200 / diagonal_length) * radius
    y_offset = (250 / diagonal_length) * radius

    glyph = init_glyph("guilsinglright", 0x203A)

    glyph.add(
        polyline(
            width,
            [
                (
                    200 + x_offset,
                    600 - y_offset,
                ),
                (400, 350),
                (
                    200 + x_offset,
                    100 + y_offset,
                ),
            ],
        )
    )

    return glyph

BUILDERS: dict[str, GlyphBuilder] = {
    "\u00A1": build_exclamdown,
    "\u00A7": build_section,
    "\u00AB": build_guillemetleft,
    "\u00B6": build_paragraph,
    "\u00B7": build_periodcentered,
    "\u00BB": build_guillemetright,
    "\u00BF": build_questiondown,
    "\u02BC": build_apostrophemod,
    "\u2013": build_endash,
    "\u2014": build_emdash,
    "\u2018": build_quoteleft,
    "\u2019": build_quoteright,
    "\u201A": build_quotesinglbase,
    "\u201C": build_quotedblleft,
    "\u201D": build_quotedblright,
    "\u201E": build_quotedblbase,
    "\u2022": build_bullet,
    "\u2026": build_ellipsis,
    "\u2039": build_guilsinglleft,
    "\u203A": build_guilsinglright,
}


__all__ = [
    "BUILDERS",
    "build_exclamdown",
    "build_section",
    "build_guillemetleft",
    "build_paragraph",
    "build_periodcentered",
    "build_guillemetright",
    "build_questiondown",
    "build_apostrophemod",
    "build_endash",
    "build_emdash",
    "build_quoteleft",
    "build_quoteright",
    "build_quotesinglbase",
    "build_quotedblleft",
    "build_quotedblright",
    "build_quotedblbase",
    "build_bullet",
    "build_ellipsis",
    "build_guilsinglleft",
    "build_guilsinglright",
]
