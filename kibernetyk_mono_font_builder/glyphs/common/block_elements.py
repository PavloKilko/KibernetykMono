"""Explicit builders for all Unicode Block Elements characters.

Solid fills use the full advance width and vertical box, with a five-unit
outer-edge overlap to reduce rasterization seams. Shades use an exact 12-by-20
pixel grid without overlap. All three use one 4-by-4 Bayer threshold map,
adding black squares at 25%, 50%, and 75% coverage.
"""

from __future__ import annotations

from kibernetyk_mono_font_builder.core import (
    ADVANCE_WIDTH,
    GLYPH_CENTER_X,
    VERTICAL_BOX_BOTTOM,
    VERTICAL_BOX_TOP,
    GlyphBuilder,
    GlyphDefinition,
    init_glyph,
    line,
)


BLOCK_EDGE_OVERLAP = 5

BAYER_4X4 = (
    (0, 8, 2, 10),
    (12, 4, 14, 6),
    (3, 11, 1, 9),
    (15, 7, 13, 5),
)


def build_upper_half_block(width: float) -> GlyphDefinition:
    """U+2580 ▀ UPPER HALF BLOCK."""
    glyph = init_glyph("uni2580", 0x2580)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = top - bottom
    radius = width / 2

    glyph.add(
        line(
            width,
            (left + radius, (bottom + top) / 2),
            (right - radius, (bottom + top) / 2),
        )
    )

    return glyph


def build_lower_one_eighth_block(width: float) -> GlyphDefinition:
    """U+2581 ▁ LOWER ONE EIGHTH BLOCK."""
    glyph = init_glyph("uni2581", 0x2581)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_BOTTOM + (VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM) * 1 / 8
    width = top - bottom
    radius = width / 2

    glyph.add(
        line(
            width,
            (left + radius, (bottom + top) / 2),
            (right - radius, (bottom + top) / 2),
        )
    )

    return glyph


def build_lower_one_quarter_block(width: float) -> GlyphDefinition:
    """U+2582 ▂ LOWER ONE QUARTER BLOCK."""
    glyph = init_glyph("uni2582", 0x2582)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_BOTTOM + (VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM) * 2 / 8
    width = top - bottom
    radius = width / 2

    glyph.add(
        line(
            width,
            (left + radius, (bottom + top) / 2),
            (right - radius, (bottom + top) / 2),
        )
    )

    return glyph


def build_lower_three_eighths_block(width: float) -> GlyphDefinition:
    """U+2583 ▃ LOWER THREE EIGHTHS BLOCK."""
    glyph = init_glyph("uni2583", 0x2583)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_BOTTOM + (VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM) * 3 / 8
    width = top - bottom
    radius = width / 2

    glyph.add(
        line(
            width,
            (left + radius, (bottom + top) / 2),
            (right - radius, (bottom + top) / 2),
        )
    )

    return glyph


def build_lower_half_block(width: float) -> GlyphDefinition:
    """U+2584 ▄ LOWER HALF BLOCK."""
    glyph = init_glyph("uni2584", 0x2584)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_BOTTOM + (VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM) * 4 / 8
    width = top - bottom
    radius = width / 2

    glyph.add(
        line(
            width,
            (left + radius, (bottom + top) / 2),
            (right - radius, (bottom + top) / 2),
        )
    )

    return glyph


def build_lower_five_eighths_block(width: float) -> GlyphDefinition:
    """U+2585 ▅ LOWER FIVE EIGHTHS BLOCK."""
    glyph = init_glyph("uni2585", 0x2585)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_BOTTOM + (VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM) * 5 / 8
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_lower_three_quarters_block(width: float) -> GlyphDefinition:
    """U+2586 ▆ LOWER THREE QUARTERS BLOCK."""
    glyph = init_glyph("uni2586", 0x2586)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_BOTTOM + (VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM) * 6 / 8
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_lower_seven_eighths_block(width: float) -> GlyphDefinition:
    """U+2587 ▇ LOWER SEVEN EIGHTHS BLOCK."""
    glyph = init_glyph("uni2587", 0x2587)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_BOTTOM + (VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM) * 7 / 8
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_full_block(width: float) -> GlyphDefinition:
    """U+2588 █ FULL BLOCK."""
    glyph = init_glyph("uni2588", 0x2588)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_left_seven_eighths_block(width: float) -> GlyphDefinition:
    """U+2589 ▉ LEFT SEVEN EIGHTHS BLOCK."""
    glyph = init_glyph("uni2589", 0x2589)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 + ADVANCE_WIDTH * 7 / 8
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_left_three_quarters_block(width: float) -> GlyphDefinition:
    """U+258A ▊ LEFT THREE QUARTERS BLOCK."""
    glyph = init_glyph("uni258A", 0x258A)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 + ADVANCE_WIDTH * 6 / 8
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_left_five_eighths_block(width: float) -> GlyphDefinition:
    """U+258B ▋ LEFT FIVE EIGHTHS BLOCK."""
    glyph = init_glyph("uni258B", 0x258B)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 + ADVANCE_WIDTH * 5 / 8
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_left_half_block(width: float) -> GlyphDefinition:
    """U+258C ▌ LEFT HALF BLOCK."""
    glyph = init_glyph("uni258C", 0x258C)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 + ADVANCE_WIDTH * 4 / 8
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_left_three_eighths_block(width: float) -> GlyphDefinition:
    """U+258D ▍ LEFT THREE EIGHTHS BLOCK."""
    glyph = init_glyph("uni258D", 0x258D)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 + ADVANCE_WIDTH * 3 / 8
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_left_one_quarter_block(width: float) -> GlyphDefinition:
    """U+258E ▎ LEFT ONE QUARTER BLOCK."""
    glyph = init_glyph("uni258E", 0x258E)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 + ADVANCE_WIDTH * 2 / 8
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_left_one_eighth_block(width: float) -> GlyphDefinition:
    """U+258F ▏ LEFT ONE EIGHTH BLOCK."""
    glyph = init_glyph("uni258F", 0x258F)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 + ADVANCE_WIDTH * 1 / 8
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_right_half_block(width: float) -> GlyphDefinition:
    """U+2590 ▐ RIGHT HALF BLOCK."""
    glyph = init_glyph("uni2590", 0x2590)

    left = GLYPH_CENTER_X
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_light_shade(width: float) -> GlyphDefinition:
    """U+2591 ░ LIGHT SHADE."""
    glyph = init_glyph("uni2591", 0x2591)

    pixel_width = ADVANCE_WIDTH / 12
    pixel_height = (VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM) / 20
    width = pixel_width / 2
    radius = width / 2
    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2

    for row in range(20):
        for column in range(12):
            if BAYER_4X4[row % 4][column % 4] < 4:
                x = left + column * pixel_width
                y = VERTICAL_BOX_TOP - (row + 1) * pixel_height

                glyph.add(
                    line(
                        width,
                        (x + radius, y + radius),
                        (x + radius, y + pixel_height - radius),
                    )
                )
                glyph.add(
                    line(
                        width,
                        (x + pixel_width - radius, y + radius),
                        (x + pixel_width - radius, y + pixel_height - radius),
                    )
                )

    return glyph


def build_medium_shade(width: float) -> GlyphDefinition:
    """U+2592 ▒ MEDIUM SHADE."""
    glyph = init_glyph("uni2592", 0x2592)

    pixel_width = ADVANCE_WIDTH / 12
    pixel_height = (VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM) / 20
    width = pixel_width / 2
    radius = width / 2
    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2

    for row in range(20):
        for column in range(12):
            if BAYER_4X4[row % 4][column % 4] < 8:
                x = left + column * pixel_width
                y = VERTICAL_BOX_TOP - (row + 1) * pixel_height

                glyph.add(
                    line(
                        width,
                        (x + radius, y + radius),
                        (x + radius, y + pixel_height - radius),
                    )
                )
                glyph.add(
                    line(
                        width,
                        (x + pixel_width - radius, y + radius),
                        (x + pixel_width - radius, y + pixel_height - radius),
                    )
                )

    return glyph


def build_dark_shade(width: float) -> GlyphDefinition:
    """U+2593 ▓ DARK SHADE."""
    glyph = init_glyph("uni2593", 0x2593)

    pixel_width = ADVANCE_WIDTH / 12
    pixel_height = (VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM) / 20
    width = pixel_width / 2
    radius = width / 2
    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2

    for row in range(20):
        for column in range(12):
            if BAYER_4X4[row % 4][column % 4] < 12:
                x = left + column * pixel_width
                y = VERTICAL_BOX_TOP - (row + 1) * pixel_height

                glyph.add(
                    line(
                        width,
                        (x + radius, y + radius),
                        (x + radius, y + pixel_height - radius),
                    )
                )
                glyph.add(
                    line(
                        width,
                        (x + pixel_width - radius, y + radius),
                        (x + pixel_width - radius, y + pixel_height - radius),
                    )
                )

    return glyph


def build_upper_one_eighth_block(width: float) -> GlyphDefinition:
    """U+2594 ▔ UPPER ONE EIGHTH BLOCK."""
    glyph = init_glyph("uni2594", 0x2594)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = VERTICAL_BOX_TOP - (VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM) / 8
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = top - bottom
    radius = width / 2

    glyph.add(
        line(
            width,
            (left + radius, (bottom + top) / 2),
            (right - radius, (bottom + top) / 2),
        )
    )

    return glyph


def build_right_one_eighth_block(width: float) -> GlyphDefinition:
    """U+2595 ▕ RIGHT ONE EIGHTH BLOCK."""
    glyph = init_glyph("uni2595", 0x2595)

    left = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 - ADVANCE_WIDTH / 8
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_quadrant_lower_left(width: float) -> GlyphDefinition:
    """U+2596 ▖ QUADRANT LOWER LEFT."""
    glyph = init_glyph("uni2596", 0x2596)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_quadrant_lower_right(width: float) -> GlyphDefinition:
    """U+2597 ▗ QUADRANT LOWER RIGHT."""
    glyph = init_glyph("uni2597", 0x2597)

    left = GLYPH_CENTER_X
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_quadrant_upper_left(width: float) -> GlyphDefinition:
    """U+2598 ▘ QUADRANT UPPER LEFT."""
    glyph = init_glyph("uni2598", 0x2598)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X
    bottom = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_quadrant_upper_left_and_lower_left_and_lower_right(width: float) -> GlyphDefinition:
    """U+2599 ▙ QUADRANT UPPER LEFT AND LOWER LEFT AND LOWER RIGHT."""
    glyph = init_glyph("uni2599", 0x2599)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X
    bottom = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    left = GLYPH_CENTER_X
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_quadrant_upper_left_and_lower_right(width: float) -> GlyphDefinition:
    """U+259A ▚ QUADRANT UPPER LEFT AND LOWER RIGHT."""
    glyph = init_glyph("uni259A", 0x259A)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X
    bottom = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    left = GLYPH_CENTER_X
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_quadrant_upper_left_and_upper_right_and_lower_left(width: float) -> GlyphDefinition:
    """U+259B ▛ QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER LEFT."""
    glyph = init_glyph("uni259B", 0x259B)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X
    bottom = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    left = GLYPH_CENTER_X
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_quadrant_upper_left_and_upper_right_and_lower_right(width: float) -> GlyphDefinition:
    """U+259C ▜ QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER RIGHT."""
    glyph = init_glyph("uni259C", 0x259C)

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X
    bottom = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    left = GLYPH_CENTER_X
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    left = GLYPH_CENTER_X
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_quadrant_upper_right(width: float) -> GlyphDefinition:
    """U+259D ▝ QUADRANT UPPER RIGHT."""
    glyph = init_glyph("uni259D", 0x259D)

    left = GLYPH_CENTER_X
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_quadrant_upper_right_and_lower_left(width: float) -> GlyphDefinition:
    """U+259E ▞ QUADRANT UPPER RIGHT AND LOWER LEFT."""
    glyph = init_glyph("uni259E", 0x259E)

    left = GLYPH_CENTER_X
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


def build_quadrant_upper_right_and_lower_left_and_lower_right(width: float) -> GlyphDefinition:
    """U+259F ▟ QUADRANT UPPER RIGHT AND LOWER LEFT AND LOWER RIGHT."""
    glyph = init_glyph("uni259F", 0x259F)

    left = GLYPH_CENTER_X
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    top = VERTICAL_BOX_TOP + BLOCK_EDGE_OVERLAP
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    left = GLYPH_CENTER_X - ADVANCE_WIDTH / 2 - BLOCK_EDGE_OVERLAP
    right = GLYPH_CENTER_X
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    left = GLYPH_CENTER_X
    right = GLYPH_CENTER_X + ADVANCE_WIDTH / 2 + BLOCK_EDGE_OVERLAP
    bottom = VERTICAL_BOX_BOTTOM - BLOCK_EDGE_OVERLAP
    top = (VERTICAL_BOX_TOP + VERTICAL_BOX_BOTTOM) / 2
    width = right - left
    radius = width / 2

    glyph.add(
        line(
            width,
            ((left + right) / 2, bottom + radius),
            ((left + right) / 2, top - radius),
        )
    )

    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    "\u2580": build_upper_half_block,
    "\u2581": build_lower_one_eighth_block,
    "\u2582": build_lower_one_quarter_block,
    "\u2583": build_lower_three_eighths_block,
    "\u2584": build_lower_half_block,
    "\u2585": build_lower_five_eighths_block,
    "\u2586": build_lower_three_quarters_block,
    "\u2587": build_lower_seven_eighths_block,
    "\u2588": build_full_block,
    "\u2589": build_left_seven_eighths_block,
    "\u258A": build_left_three_quarters_block,
    "\u258B": build_left_five_eighths_block,
    "\u258C": build_left_half_block,
    "\u258D": build_left_three_eighths_block,
    "\u258E": build_left_one_quarter_block,
    "\u258F": build_left_one_eighth_block,
    "\u2590": build_right_half_block,
    "\u2591": build_light_shade,
    "\u2592": build_medium_shade,
    "\u2593": build_dark_shade,
    "\u2594": build_upper_one_eighth_block,
    "\u2595": build_right_one_eighth_block,
    "\u2596": build_quadrant_lower_left,
    "\u2597": build_quadrant_lower_right,
    "\u2598": build_quadrant_upper_left,
    "\u2599": build_quadrant_upper_left_and_lower_left_and_lower_right,
    "\u259A": build_quadrant_upper_left_and_lower_right,
    "\u259B": build_quadrant_upper_left_and_upper_right_and_lower_left,
    "\u259C": build_quadrant_upper_left_and_upper_right_and_lower_right,
    "\u259D": build_quadrant_upper_right,
    "\u259E": build_quadrant_upper_right_and_lower_left,
    "\u259F": build_quadrant_upper_right_and_lower_left_and_lower_right,
}


__all__ = [
    "BUILDERS",
    "build_upper_half_block",
    "build_lower_one_eighth_block",
    "build_lower_one_quarter_block",
    "build_lower_three_eighths_block",
    "build_lower_half_block",
    "build_lower_five_eighths_block",
    "build_lower_three_quarters_block",
    "build_lower_seven_eighths_block",
    "build_full_block",
    "build_left_seven_eighths_block",
    "build_left_three_quarters_block",
    "build_left_five_eighths_block",
    "build_left_half_block",
    "build_left_three_eighths_block",
    "build_left_one_quarter_block",
    "build_left_one_eighth_block",
    "build_right_half_block",
    "build_light_shade",
    "build_medium_shade",
    "build_dark_shade",
    "build_upper_one_eighth_block",
    "build_right_one_eighth_block",
    "build_quadrant_lower_left",
    "build_quadrant_lower_right",
    "build_quadrant_upper_left",
    "build_quadrant_upper_left_and_lower_left_and_lower_right",
    "build_quadrant_upper_left_and_lower_right",
    "build_quadrant_upper_left_and_upper_right_and_lower_left",
    "build_quadrant_upper_left_and_upper_right_and_lower_right",
    "build_quadrant_upper_right",
    "build_quadrant_upper_right_and_lower_left",
    "build_quadrant_upper_right_and_lower_left_and_lower_right",
]
