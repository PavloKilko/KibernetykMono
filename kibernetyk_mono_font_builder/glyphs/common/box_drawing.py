"""Explicit builders for all Unicode Box Drawing characters.

Light strokes use 70% and heavy strokes 130% of the weight's line width.
Local bounds are x=-75..675 and y=-275..1075, centered on (300, 400).
Square-corner arms extend another 30 units to bridge gaps at dashed joins.
Double lines use two light strokes with a gap of two stroke widths between them.
"""

from __future__ import annotations

import math

from kibernetyk_mono_font_builder.core import (
    ADVANCE_WIDTH,
    VERTICAL_BOX_BOTTOM,
    VERTICAL_BOX_TOP,
    GlyphBuilder,
    GlyphDefinition,
    init_glyph,
    line,
    polyline,
)

def build_box_drawings_light_horizontal(width: float) -> GlyphDefinition:
    """U+2500 ─ BOX DRAWINGS LIGHT HORIZONTAL."""
    glyph = init_glyph("uni2500", 0x2500)

    width = width * 0.7
    radius = width / 2

    glyph.add(
        line(
            width,
            (-75 + radius, 400),
            (675 - radius, 400)
        )
    )
    
    return glyph


def build_box_drawings_heavy_horizontal(width: float) -> GlyphDefinition:
    """U+2501 ━ BOX DRAWINGS HEAVY HORIZONTAL."""
    glyph = init_glyph("uni2501", 0x2501)

    width = width * 1.3
    radius = width / 2

    glyph.add(
        line(
            width,
            (-75 + radius, 400),
            (675 - radius, 400)
        )
    )
    
    return glyph


def build_box_drawings_light_vertical(width: float) -> GlyphDefinition:
    """U+2502 │ BOX DRAWINGS LIGHT VERTICAL."""
    glyph = init_glyph("uni2502", 0x2502)

    width = width * 0.7
    radius = width / 2

    glyph.add(
        line(
            width,
            (300, -275 + radius),
            (300, 1075 - radius)
        )
    )
    
    return glyph


def build_box_drawings_heavy_vertical(width: float) -> GlyphDefinition:
    """U+2503 ┃ BOX DRAWINGS HEAVY VERTICAL."""
    glyph = init_glyph("uni2503", 0x2503)

    width = width * 1.3
    radius = width / 2

    glyph.add(
        line(
            width,
            (300, -275 + radius),
            (300, 1075 - radius)
        )
    )
    
    return glyph


def build_box_drawings_light_triple_dash_horizontal(width: float) -> GlyphDefinition:
    """U+2504 ┄ BOX DRAWINGS LIGHT TRIPLE DASH HORIZONTAL."""
    glyph = init_glyph("uni2504", 0x2504)

    width = width * 0.7
    radius = width / 2

    dash_step = ADVANCE_WIDTH / 3
    dash_length = dash_step * 0.75
    start_x = 300 - ADVANCE_WIDTH / 2 + dash_step / 8

    # Half a gap at each cell edge makes repeated characters evenly spaced.

    glyph.add(
        line(
            width,
            (start_x + radius, 400),
            (start_x + dash_length - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (start_x + dash_step + radius, 400),
            (start_x + dash_step + dash_length - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (start_x + 2 * dash_step + radius, 400),
            (start_x + 2 * dash_step + dash_length - radius, 400),
        )
    )

    return glyph


def build_box_drawings_heavy_triple_dash_horizontal(width: float) -> GlyphDefinition:
    """U+2505 ┅ BOX DRAWINGS HEAVY TRIPLE DASH HORIZONTAL."""
    glyph = init_glyph("uni2505", 0x2505)

    width = width * 1.3
    radius = width / 2

    dash_step = ADVANCE_WIDTH / 3
    dash_length = dash_step * 0.75
    start_x = 300 - ADVANCE_WIDTH / 2 + dash_step / 8

    # Half a gap at each cell edge makes repeated characters evenly spaced.

    glyph.add(
        line(
            width,
            (start_x + radius, 400),
            (start_x + dash_length - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (start_x + dash_step + radius, 400),
            (start_x + dash_step + dash_length - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (start_x + 2 * dash_step + radius, 400),
            (start_x + 2 * dash_step + dash_length - radius, 400),
        )
    )

    return glyph


def build_box_drawings_light_triple_dash_vertical(width: float) -> GlyphDefinition:
    """U+2506 ┆ BOX DRAWINGS LIGHT TRIPLE DASH VERTICAL."""
    glyph = init_glyph("uni2506", 0x2506)

    width = width * 0.7
    radius = width / 2

    row_height = VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM
    dash_step = row_height / 3
    dash_length = dash_step * 0.75
    start_y = 400 - row_height / 2 + dash_step / 8

    # Half a gap at each cell edge makes repeated characters evenly spaced.

    glyph.add(
        line(
            width,
            (300, start_y + radius),
            (300, start_y + dash_length - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300, start_y + dash_step + radius),
            (300, start_y + dash_step + dash_length - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300, start_y + 2 * dash_step + radius),
            (300, start_y + 2 * dash_step + dash_length - radius),
        )
    )

    return glyph


def build_box_drawings_heavy_triple_dash_vertical(width: float) -> GlyphDefinition:
    """U+2507 ┇ BOX DRAWINGS HEAVY TRIPLE DASH VERTICAL."""
    glyph = init_glyph("uni2507", 0x2507)

    width = width * 1.3
    radius = width / 2

    row_height = VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM
    dash_step = row_height / 3
    dash_length = dash_step * 0.75
    start_y = 400 - row_height / 2 + dash_step / 8

    # Half a gap at each cell edge makes repeated characters evenly spaced.

    glyph.add(
        line(
            width,
            (300, start_y + radius),
            (300, start_y + dash_length - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300, start_y + dash_step + radius),
            (300, start_y + dash_step + dash_length - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300, start_y + 2 * dash_step + radius),
            (300, start_y + 2 * dash_step + dash_length - radius),
        )
    )

    return glyph


def build_box_drawings_light_quadruple_dash_horizontal(width: float) -> GlyphDefinition:
    """U+2508 ┈ BOX DRAWINGS LIGHT QUADRUPLE DASH HORIZONTAL."""
    glyph = init_glyph("uni2508", 0x2508)

    width = width * 0.7
    radius = width / 2

    dash_step = ADVANCE_WIDTH / 4
    dash_length = dash_step * 0.75
    start_x = 300 - ADVANCE_WIDTH / 2 + dash_step / 8

    # Half a gap at each cell edge makes repeated characters evenly spaced.

    glyph.add(
        line(
            width,
            (start_x + radius, 400),
            (start_x + dash_length - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (start_x + dash_step + radius, 400),
            (start_x + dash_step + dash_length - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (start_x + 2 * dash_step + radius, 400),
            (start_x + 2 * dash_step + dash_length - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (start_x + 3 * dash_step + radius, 400),
            (start_x + 3 * dash_step + dash_length - radius, 400),
        )
    )

    return glyph


def build_box_drawings_heavy_quadruple_dash_horizontal(width: float) -> GlyphDefinition:
    """U+2509 ┉ BOX DRAWINGS HEAVY QUADRUPLE DASH HORIZONTAL."""
    glyph = init_glyph("uni2509", 0x2509)

    width = width * 1.3
    radius = width / 2

    dash_step = ADVANCE_WIDTH / 4
    dash_length = dash_step * 0.75
    start_x = 300 - ADVANCE_WIDTH / 2 + dash_step / 8

    # Half a gap at each cell edge makes repeated characters evenly spaced.
    # Two half-width strokes keep short, thick dashes rectangular at every weight.

    glyph.add(
        line(
            width / 2,
            (start_x + radius / 2, 400 - radius / 2),
            (start_x + dash_length - radius / 2, 400 - radius / 2),
        )
    )

    glyph.add(
        line(
            width / 2,
            (start_x + radius / 2, 400 + radius / 2),
            (start_x + dash_length - radius / 2, 400 + radius / 2),
        )
    )

    glyph.add(
        line(
            width / 2,
            (start_x + dash_step + radius / 2, 400 - radius / 2),
            (start_x + dash_step + dash_length - radius / 2, 400 - radius / 2),
        )
    )

    glyph.add(
        line(
            width / 2,
            (start_x + dash_step + radius / 2, 400 + radius / 2),
            (start_x + dash_step + dash_length - radius / 2, 400 + radius / 2),
        )
    )

    glyph.add(
        line(
            width / 2,
            (start_x + 2 * dash_step + radius / 2, 400 - radius / 2),
            (start_x + 2 * dash_step + dash_length - radius / 2, 400 - radius / 2),
        )
    )

    glyph.add(
        line(
            width / 2,
            (start_x + 2 * dash_step + radius / 2, 400 + radius / 2),
            (start_x + 2 * dash_step + dash_length - radius / 2, 400 + radius / 2),
        )
    )

    glyph.add(
        line(
            width / 2,
            (start_x + 3 * dash_step + radius / 2, 400 - radius / 2),
            (start_x + 3 * dash_step + dash_length - radius / 2, 400 - radius / 2),
        )
    )

    glyph.add(
        line(
            width / 2,
            (start_x + 3 * dash_step + radius / 2, 400 + radius / 2),
            (start_x + 3 * dash_step + dash_length - radius / 2, 400 + radius / 2),
        )
    )

    return glyph


def build_box_drawings_light_quadruple_dash_vertical(width: float) -> GlyphDefinition:
    """U+250A ┊ BOX DRAWINGS LIGHT QUADRUPLE DASH VERTICAL."""
    glyph = init_glyph("uni250A", 0x250A)

    width = width * 0.7
    radius = width / 2

    row_height = VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM
    dash_step = row_height / 4
    dash_length = dash_step * 0.75
    start_y = 400 - row_height / 2 + dash_step / 8

    # Half a gap at each cell edge makes repeated characters evenly spaced.

    glyph.add(
        line(
            width,
            (300, start_y + radius),
            (300, start_y + dash_length - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300, start_y + dash_step + radius),
            (300, start_y + dash_step + dash_length - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300, start_y + 2 * dash_step + radius),
            (300, start_y + 2 * dash_step + dash_length - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300, start_y + 3 * dash_step + radius),
            (300, start_y + 3 * dash_step + dash_length - radius),
        )
    )

    return glyph


def build_box_drawings_heavy_quadruple_dash_vertical(width: float) -> GlyphDefinition:
    """U+250B ┋ BOX DRAWINGS HEAVY QUADRUPLE DASH VERTICAL."""
    glyph = init_glyph("uni250B", 0x250B)

    width = width * 1.3
    radius = width / 2

    row_height = VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM
    dash_step = row_height / 4
    dash_length = dash_step * 0.75
    start_y = 400 - row_height / 2 + dash_step / 8

    # Half a gap at each cell edge makes repeated characters evenly spaced.

    glyph.add(
        line(
            width,
            (300, start_y + radius),
            (300, start_y + dash_length - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300, start_y + dash_step + radius),
            (300, start_y + dash_step + dash_length - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300, start_y + 2 * dash_step + radius),
            (300, start_y + 2 * dash_step + dash_length - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300, start_y + 3 * dash_step + radius),
            (300, start_y + 3 * dash_step + dash_length - radius),
        )
    )

    return glyph


def build_box_drawings_light_down_and_right(width: float) -> GlyphDefinition:
    """U+250C ┌ BOX DRAWINGS LIGHT DOWN AND RIGHT."""
    glyph = init_glyph("uni250C", 0x250C)

    width = width * 0.7
    radius = width / 2

    glyph.add(
        polyline(
            width,
            [
                (705 - radius, 400),
                (300, 400),
                (300, -305 + radius),
            ],
        )
    )

    return glyph


def build_box_drawings_down_light_and_right_heavy(width: float) -> GlyphDefinition:
    """U+250D ┍ BOX DRAWINGS DOWN LIGHT AND RIGHT HEAVY."""
    glyph = init_glyph("uni250D", 0x250D)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (300 - light_radius + heavy_radius, 400),
            (705 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -305 + light_radius),
            (300, 400 + heavy_radius - light_radius),
        )
    )

    return glyph


def build_box_drawings_down_heavy_and_right_light(width: float) -> GlyphDefinition:
    """U+250E ┎ BOX DRAWINGS DOWN HEAVY AND RIGHT LIGHT."""
    glyph = init_glyph("uni250E", 0x250E)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (300 - heavy_radius + light_radius, 400),
            (705 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -305 + heavy_radius),
            (300, 400 + light_radius - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_heavy_down_and_right(width: float) -> GlyphDefinition:
    """U+250F ┏ BOX DRAWINGS HEAVY DOWN AND RIGHT."""
    glyph = init_glyph("uni250F", 0x250F)

    width = width * 1.3
    radius = width / 2

    glyph.add(
        polyline(
            width,
            [
                (705 - radius, 400),
                (300, 400),
                (300, -305 + radius),
            ],
        )
    )

    return glyph


def build_box_drawings_light_down_and_left(width: float) -> GlyphDefinition:
    """U+2510 ┐ BOX DRAWINGS LIGHT DOWN AND LEFT."""
    glyph = init_glyph("uni2510", 0x2510)

    width = width * 0.7
    radius = width / 2

    glyph.add(
        polyline(
            width,
            [
                (-105 + radius, 400),
                (300, 400),
                (300, -305 + radius),
            ],
        )
    )

    return glyph


def build_box_drawings_down_light_and_left_heavy(width: float) -> GlyphDefinition:
    """U+2511 ┑ BOX DRAWINGS DOWN LIGHT AND LEFT HEAVY."""
    glyph = init_glyph("uni2511", 0x2511)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-105 + heavy_radius, 400),
            (300 + light_radius - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -305 + light_radius),
            (300, 400 + heavy_radius - light_radius),
        )
    )

    return glyph


def build_box_drawings_down_heavy_and_left_light(width: float) -> GlyphDefinition:
    """U+2512 ┒ BOX DRAWINGS DOWN HEAVY AND LEFT LIGHT."""
    glyph = init_glyph("uni2512", 0x2512)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-105 + light_radius, 400),
            (300 + heavy_radius - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -305 + heavy_radius),
            (300, 400 + light_radius - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_heavy_down_and_left(width: float) -> GlyphDefinition:
    """U+2513 ┓ BOX DRAWINGS HEAVY DOWN AND LEFT."""
    glyph = init_glyph("uni2513", 0x2513)

    width = width * 1.3
    radius = width / 2

    glyph.add(
        polyline(
            width,
            [
                (-105 + radius, 400),
                (300, 400),
                (300, -305 + radius),
            ],
        )
    )

    return glyph


def build_box_drawings_light_up_and_right(width: float) -> GlyphDefinition:
    """U+2514 └ BOX DRAWINGS LIGHT UP AND RIGHT."""
    glyph = init_glyph("uni2514", 0x2514)

    width = width * 0.7
    radius = width / 2

    glyph.add(
        polyline(
            width,
            [
                (705 - radius, 400),
                (300, 400),
                (300, 1105 - radius),
            ],
        )
    )

    return glyph


def build_box_drawings_up_light_and_right_heavy(width: float) -> GlyphDefinition:
    """U+2515 ┕ BOX DRAWINGS UP LIGHT AND RIGHT HEAVY."""
    glyph = init_glyph("uni2515", 0x2515)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (300 - light_radius + heavy_radius, 400),
            (705 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, 400 - heavy_radius + light_radius),
            (300, 1105 - light_radius),
        )
    )

    return glyph


def build_box_drawings_up_heavy_and_right_light(width: float) -> GlyphDefinition:
    """U+2516 ┖ BOX DRAWINGS UP HEAVY AND RIGHT LIGHT."""
    glyph = init_glyph("uni2516", 0x2516)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (300 - heavy_radius + light_radius, 400),
            (705 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, 400 - light_radius + heavy_radius),
            (300, 1105 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_heavy_up_and_right(width: float) -> GlyphDefinition:
    """U+2517 ┗ BOX DRAWINGS HEAVY UP AND RIGHT."""
    glyph = init_glyph("uni2517", 0x2517)

    width = width * 1.3
    radius = width / 2

    glyph.add(
        polyline(
            width,
            [
                (705 - radius, 400),
                (300, 400),
                (300, 1105 - radius),
            ],
        )
    )

    return glyph


def build_box_drawings_light_up_and_left(width: float) -> GlyphDefinition:
    """U+2518 ┘ BOX DRAWINGS LIGHT UP AND LEFT."""
    glyph = init_glyph("uni2518", 0x2518)

    width = width * 0.7
    radius = width / 2

    glyph.add(
        polyline(
            width,
            [
                (-105 + radius, 400),
                (300, 400),
                (300, 1105 - radius),
            ],
        )
    )

    return glyph


def build_box_drawings_up_light_and_left_heavy(width: float) -> GlyphDefinition:
    """U+2519 ┙ BOX DRAWINGS UP LIGHT AND LEFT HEAVY."""
    glyph = init_glyph("uni2519", 0x2519)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-105 + heavy_radius, 400),
            (300 + light_radius - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, 400 - heavy_radius + light_radius),
            (300, 1105 - light_radius),
        )
    )

    return glyph


def build_box_drawings_up_heavy_and_left_light(width: float) -> GlyphDefinition:
    """U+251A ┚ BOX DRAWINGS UP HEAVY AND LEFT LIGHT."""
    glyph = init_glyph("uni251A", 0x251A)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-105 + light_radius, 400),
            (300 + heavy_radius - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, 400 - light_radius + heavy_radius),
            (300, 1105 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_heavy_up_and_left(width: float) -> GlyphDefinition:
    """U+251B ┛ BOX DRAWINGS HEAVY UP AND LEFT."""
    glyph = init_glyph("uni251B", 0x251B)

    width = width * 1.3
    radius = width / 2

    glyph.add(
        polyline(
            width,
            [
                (-105 + radius, 400),
                (300, 400),
                (300, 1105 - radius),
            ],
        )
    )

    return glyph


def build_box_drawings_light_vertical_and_right(width: float) -> GlyphDefinition:
    """U+251C ├ BOX DRAWINGS LIGHT VERTICAL AND RIGHT."""
    glyph = init_glyph("uni251C", 0x251C)

    width = width * 0.7
    radius = width / 2

    glyph.add(
        line(
            width,
            (300 - radius + radius, 400),
            (675 - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (300, -275 + radius),
            (300, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_vertical_light_and_right_heavy(width: float) -> GlyphDefinition:
    """U+251D ┝ BOX DRAWINGS VERTICAL LIGHT AND RIGHT HEAVY."""
    glyph = init_glyph("uni251D", 0x251D)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (300 - light_radius + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_up_heavy_and_right_down_light(width: float) -> GlyphDefinition:
    """U+251E ┞ BOX DRAWINGS UP HEAVY AND RIGHT DOWN LIGHT."""
    glyph = init_glyph("uni251E", 0x251E)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (300 - heavy_radius + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 400 + light_radius - light_radius),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, 400 - light_radius + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_down_heavy_and_right_up_light(width: float) -> GlyphDefinition:
    """U+251F ┟ BOX DRAWINGS DOWN HEAVY AND RIGHT UP LIGHT."""
    glyph = init_glyph("uni251F", 0x251F)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (300 - heavy_radius + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 400 + light_radius - heavy_radius),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, 400 - light_radius + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_vertical_heavy_and_right_light(width: float) -> GlyphDefinition:
    """U+2520 ┠ BOX DRAWINGS VERTICAL HEAVY AND RIGHT LIGHT."""
    glyph = init_glyph("uni2520", 0x2520)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (300 - heavy_radius + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_down_light_and_right_up_heavy(width: float) -> GlyphDefinition:
    """U+2521 ┡ BOX DRAWINGS DOWN LIGHT AND RIGHT UP HEAVY."""
    glyph = init_glyph("uni2521", 0x2521)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (300 - heavy_radius + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 400 + heavy_radius - light_radius),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, 400 - heavy_radius + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_up_light_and_right_down_heavy(width: float) -> GlyphDefinition:
    """U+2522 ┢ BOX DRAWINGS UP LIGHT AND RIGHT DOWN HEAVY."""
    glyph = init_glyph("uni2522", 0x2522)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (300 - heavy_radius + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 400 + heavy_radius - heavy_radius),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, 400 - heavy_radius + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_heavy_vertical_and_right(width: float) -> GlyphDefinition:
    """U+2523 ┣ BOX DRAWINGS HEAVY VERTICAL AND RIGHT."""
    glyph = init_glyph("uni2523", 0x2523)

    width = width * 1.3
    radius = width / 2

    glyph.add(
        line(
            width,
            (300 - radius + radius, 400),
            (675 - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (300, -275 + radius),
            (300, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_light_vertical_and_left(width: float) -> GlyphDefinition:
    """U+2524 ┤ BOX DRAWINGS LIGHT VERTICAL AND LEFT."""
    glyph = init_glyph("uni2524", 0x2524)

    width = width * 0.7
    radius = width / 2

    glyph.add(
        line(
            width,
            (-75 + radius, 400),
            (300 + radius - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (300, -275 + radius),
            (300, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_vertical_light_and_left_heavy(width: float) -> GlyphDefinition:
    """U+2525 ┥ BOX DRAWINGS VERTICAL LIGHT AND LEFT HEAVY."""
    glyph = init_glyph("uni2525", 0x2525)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (300 + light_radius - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_up_heavy_and_left_down_light(width: float) -> GlyphDefinition:
    """U+2526 ┦ BOX DRAWINGS UP HEAVY AND LEFT DOWN LIGHT."""
    glyph = init_glyph("uni2526", 0x2526)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (300 + heavy_radius - light_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 400 + light_radius - light_radius),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, 400 - light_radius + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_down_heavy_and_left_up_light(width: float) -> GlyphDefinition:
    """U+2527 ┧ BOX DRAWINGS DOWN HEAVY AND LEFT UP LIGHT."""
    glyph = init_glyph("uni2527", 0x2527)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (300 + heavy_radius - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 400 + light_radius - heavy_radius),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, 400 - light_radius + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_vertical_heavy_and_left_light(width: float) -> GlyphDefinition:
    """U+2528 ┨ BOX DRAWINGS VERTICAL HEAVY AND LEFT LIGHT."""
    glyph = init_glyph("uni2528", 0x2528)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (300 + heavy_radius - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_down_light_and_left_up_heavy(width: float) -> GlyphDefinition:
    """U+2529 ┩ BOX DRAWINGS DOWN LIGHT AND LEFT UP HEAVY."""
    glyph = init_glyph("uni2529", 0x2529)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (300 + heavy_radius - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 400 + heavy_radius - light_radius),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, 400 - heavy_radius + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_up_light_and_left_down_heavy(width: float) -> GlyphDefinition:
    """U+252A ┪ BOX DRAWINGS UP LIGHT AND LEFT DOWN HEAVY."""
    glyph = init_glyph("uni252A", 0x252A)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (300 + heavy_radius - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 400 + heavy_radius - heavy_radius),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, 400 - heavy_radius + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_heavy_vertical_and_left(width: float) -> GlyphDefinition:
    """U+252B ┫ BOX DRAWINGS HEAVY VERTICAL AND LEFT."""
    glyph = init_glyph("uni252B", 0x252B)

    width = width * 1.3
    radius = width / 2

    glyph.add(
        line(
            width,
            (-75 + radius, 400),
            (300 + radius - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (300, -275 + radius),
            (300, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_light_down_and_horizontal(width: float) -> GlyphDefinition:
    """U+252C ┬ BOX DRAWINGS LIGHT DOWN AND HORIZONTAL."""
    glyph = init_glyph("uni252C", 0x252C)

    width = width * 0.7
    radius = width / 2

    glyph.add(
        line(
            width,
            (-75 + radius, 400),
            (675 - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (300, -275 + radius),
            (300, 400 + radius - radius),
        )
    )

    return glyph


def build_box_drawings_left_heavy_and_right_down_light(width: float) -> GlyphDefinition:
    """U+252D ┭ BOX DRAWINGS LEFT HEAVY AND RIGHT DOWN LIGHT."""
    glyph = init_glyph("uni252D", 0x252D)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (300 + light_radius - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300 - light_radius + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 400 + heavy_radius - light_radius),
        )
    )

    return glyph


def build_box_drawings_right_heavy_and_left_down_light(width: float) -> GlyphDefinition:
    """U+252E ┮ BOX DRAWINGS RIGHT HEAVY AND LEFT DOWN LIGHT."""
    glyph = init_glyph("uni252E", 0x252E)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (300 + light_radius - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300 - light_radius + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 400 + heavy_radius - light_radius),
        )
    )

    return glyph


def build_box_drawings_down_light_and_horizontal_heavy(width: float) -> GlyphDefinition:
    """U+252F ┯ BOX DRAWINGS DOWN LIGHT AND HORIZONTAL HEAVY."""
    glyph = init_glyph("uni252F", 0x252F)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 400 + heavy_radius - light_radius),
        )
    )

    return glyph


def build_box_drawings_down_heavy_and_horizontal_light(width: float) -> GlyphDefinition:
    """U+2530 ┰ BOX DRAWINGS DOWN HEAVY AND HORIZONTAL LIGHT."""
    glyph = init_glyph("uni2530", 0x2530)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 400 + light_radius - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_right_light_and_left_down_heavy(width: float) -> GlyphDefinition:
    """U+2531 ┱ BOX DRAWINGS RIGHT LIGHT AND LEFT DOWN HEAVY."""
    glyph = init_glyph("uni2531", 0x2531)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (300 + heavy_radius - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300 - heavy_radius + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 400 + heavy_radius - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_left_light_and_right_down_heavy(width: float) -> GlyphDefinition:
    """U+2532 ┲ BOX DRAWINGS LEFT LIGHT AND RIGHT DOWN HEAVY."""
    glyph = init_glyph("uni2532", 0x2532)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (300 + heavy_radius - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300 - heavy_radius + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 400 + heavy_radius - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_heavy_down_and_horizontal(width: float) -> GlyphDefinition:
    """U+2533 ┳ BOX DRAWINGS HEAVY DOWN AND HORIZONTAL."""
    glyph = init_glyph("uni2533", 0x2533)

    width = width * 1.3
    radius = width / 2

    glyph.add(
        line(
            width,
            (-75 + radius, 400),
            (675 - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (300, -275 + radius),
            (300, 400 + radius - radius),
        )
    )

    return glyph


def build_box_drawings_light_up_and_horizontal(width: float) -> GlyphDefinition:
    """U+2534 ┴ BOX DRAWINGS LIGHT UP AND HORIZONTAL."""
    glyph = init_glyph("uni2534", 0x2534)

    width = width * 0.7
    radius = width / 2

    glyph.add(
        line(
            width,
            (-75 + radius, 400),
            (675 - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (300, 400 - radius + radius),
            (300, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_left_heavy_and_right_up_light(width: float) -> GlyphDefinition:
    """U+2535 ┵ BOX DRAWINGS LEFT HEAVY AND RIGHT UP LIGHT."""
    glyph = init_glyph("uni2535", 0x2535)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (300 + light_radius - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300 - light_radius + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, 400 - heavy_radius + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_right_heavy_and_left_up_light(width: float) -> GlyphDefinition:
    """U+2536 ┶ BOX DRAWINGS RIGHT HEAVY AND LEFT UP LIGHT."""
    glyph = init_glyph("uni2536", 0x2536)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (300 + light_radius - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300 - light_radius + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, 400 - heavy_radius + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_up_light_and_horizontal_heavy(width: float) -> GlyphDefinition:
    """U+2537 ┷ BOX DRAWINGS UP LIGHT AND HORIZONTAL HEAVY."""
    glyph = init_glyph("uni2537", 0x2537)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, 400 - heavy_radius + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_up_heavy_and_horizontal_light(width: float) -> GlyphDefinition:
    """U+2538 ┸ BOX DRAWINGS UP HEAVY AND HORIZONTAL LIGHT."""
    glyph = init_glyph("uni2538", 0x2538)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, 400 - light_radius + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_right_light_and_left_up_heavy(width: float) -> GlyphDefinition:
    """U+2539 ┹ BOX DRAWINGS RIGHT LIGHT AND LEFT UP HEAVY."""
    glyph = init_glyph("uni2539", 0x2539)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (300 + heavy_radius - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300 - heavy_radius + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, 400 - heavy_radius + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_left_light_and_right_up_heavy(width: float) -> GlyphDefinition:
    """U+253A ┺ BOX DRAWINGS LEFT LIGHT AND RIGHT UP HEAVY."""
    glyph = init_glyph("uni253A", 0x253A)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (300 + heavy_radius - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300 - heavy_radius + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, 400 - heavy_radius + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_heavy_up_and_horizontal(width: float) -> GlyphDefinition:
    """U+253B ┻ BOX DRAWINGS HEAVY UP AND HORIZONTAL."""
    glyph = init_glyph("uni253B", 0x253B)

    width = width * 1.3
    radius = width / 2

    glyph.add(
        line(
            width,
            (-75 + radius, 400),
            (675 - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (300, 400 - radius + radius),
            (300, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_light_vertical_and_horizontal(width: float) -> GlyphDefinition:
    """U+253C ┼ BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL."""
    glyph = init_glyph("uni253C", 0x253C)

    width = width * 0.7
    radius = width / 2

    glyph.add(
        line(
            width,
            (-75 + radius, 400),
            (675 - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (300, -275 + radius),
            (300, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_left_heavy_and_right_vertical_light(width: float) -> GlyphDefinition:
    """U+253D ┽ BOX DRAWINGS LEFT HEAVY AND RIGHT VERTICAL LIGHT."""
    glyph = init_glyph("uni253D", 0x253D)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (300 + light_radius - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300 - light_radius + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_right_heavy_and_left_vertical_light(width: float) -> GlyphDefinition:
    """U+253E ┾ BOX DRAWINGS RIGHT HEAVY AND LEFT VERTICAL LIGHT."""
    glyph = init_glyph("uni253E", 0x253E)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (300 + light_radius - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300 - light_radius + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_vertical_light_and_horizontal_heavy(width: float) -> GlyphDefinition:
    """U+253F ┿ BOX DRAWINGS VERTICAL LIGHT AND HORIZONTAL HEAVY."""
    glyph = init_glyph("uni253F", 0x253F)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_up_heavy_and_down_horizontal_light(width: float) -> GlyphDefinition:
    """U+2540 ╀ BOX DRAWINGS UP HEAVY AND DOWN HORIZONTAL LIGHT."""
    glyph = init_glyph("uni2540", 0x2540)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 400 + light_radius - light_radius),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, 400 - light_radius + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_down_heavy_and_up_horizontal_light(width: float) -> GlyphDefinition:
    """U+2541 ╁ BOX DRAWINGS DOWN HEAVY AND UP HORIZONTAL LIGHT."""
    glyph = init_glyph("uni2541", 0x2541)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 400 + light_radius - heavy_radius),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, 400 - light_radius + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_vertical_heavy_and_horizontal_light(width: float) -> GlyphDefinition:
    """U+2542 ╂ BOX DRAWINGS VERTICAL HEAVY AND HORIZONTAL LIGHT."""
    glyph = init_glyph("uni2542", 0x2542)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_left_up_heavy_and_right_down_light(width: float) -> GlyphDefinition:
    """U+2543 ╃ BOX DRAWINGS LEFT UP HEAVY AND RIGHT DOWN LIGHT."""
    glyph = init_glyph("uni2543", 0x2543)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (300 + heavy_radius - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300 - heavy_radius + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 400 + heavy_radius - light_radius),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, 400 - heavy_radius + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_right_up_heavy_and_left_down_light(width: float) -> GlyphDefinition:
    """U+2544 ╄ BOX DRAWINGS RIGHT UP HEAVY AND LEFT DOWN LIGHT."""
    glyph = init_glyph("uni2544", 0x2544)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (300 + heavy_radius - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300 - heavy_radius + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 400 + heavy_radius - light_radius),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, 400 - heavy_radius + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_left_down_heavy_and_right_up_light(width: float) -> GlyphDefinition:
    """U+2545 ╅ BOX DRAWINGS LEFT DOWN HEAVY AND RIGHT UP LIGHT."""
    glyph = init_glyph("uni2545", 0x2545)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (300 + heavy_radius - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300 - heavy_radius + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 400 + heavy_radius - heavy_radius),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, 400 - heavy_radius + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_right_down_heavy_and_left_up_light(width: float) -> GlyphDefinition:
    """U+2546 ╆ BOX DRAWINGS RIGHT DOWN HEAVY AND LEFT UP LIGHT."""
    glyph = init_glyph("uni2546", 0x2546)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (300 + heavy_radius - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300 - heavy_radius + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 400 + heavy_radius - heavy_radius),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, 400 - heavy_radius + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_down_light_and_up_horizontal_heavy(width: float) -> GlyphDefinition:
    """U+2547 ╇ BOX DRAWINGS DOWN LIGHT AND UP HORIZONTAL HEAVY."""
    glyph = init_glyph("uni2547", 0x2547)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 400 + heavy_radius - light_radius),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, 400 - heavy_radius + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_up_light_and_down_horizontal_heavy(width: float) -> GlyphDefinition:
    """U+2548 ╈ BOX DRAWINGS UP LIGHT AND DOWN HORIZONTAL HEAVY."""
    glyph = init_glyph("uni2548", 0x2548)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 400 + heavy_radius - heavy_radius),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, 400 - heavy_radius + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_right_light_and_left_vertical_heavy(width: float) -> GlyphDefinition:
    """U+2549 ╉ BOX DRAWINGS RIGHT LIGHT AND LEFT VERTICAL HEAVY."""
    glyph = init_glyph("uni2549", 0x2549)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (300 + heavy_radius - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300 - heavy_radius + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_left_light_and_right_vertical_heavy(width: float) -> GlyphDefinition:
    """U+254A ╊ BOX DRAWINGS LEFT LIGHT AND RIGHT VERTICAL HEAVY."""
    glyph = init_glyph("uni254A", 0x254A)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (300 + heavy_radius - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300 - heavy_radius + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


def build_box_drawings_heavy_vertical_and_horizontal(width: float) -> GlyphDefinition:
    """U+254B ╋ BOX DRAWINGS HEAVY VERTICAL AND HORIZONTAL."""
    glyph = init_glyph("uni254B", 0x254B)

    width = width * 1.3
    radius = width / 2

    glyph.add(
        line(
            width,
            (-75 + radius, 400),
            (675 - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (300, -275 + radius),
            (300, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_light_double_dash_horizontal(width: float) -> GlyphDefinition:
    """U+254C ╌ BOX DRAWINGS LIGHT DOUBLE DASH HORIZONTAL."""
    glyph = init_glyph("uni254C", 0x254C)

    width = width * 0.7
    radius = width / 2

    dash_step = ADVANCE_WIDTH / 2
    dash_length = dash_step * 0.75
    start_x = 300 - ADVANCE_WIDTH / 2 + dash_step / 8

    # Half a gap at each cell edge makes repeated characters evenly spaced.

    glyph.add(
        line(
            width,
            (start_x + radius, 400),
            (start_x + dash_length - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (start_x + dash_step + radius, 400),
            (start_x + dash_step + dash_length - radius, 400),
        )
    )

    return glyph


def build_box_drawings_heavy_double_dash_horizontal(width: float) -> GlyphDefinition:
    """U+254D ╍ BOX DRAWINGS HEAVY DOUBLE DASH HORIZONTAL."""
    glyph = init_glyph("uni254D", 0x254D)

    width = width * 1.3
    radius = width / 2

    dash_step = ADVANCE_WIDTH / 2
    dash_length = dash_step * 0.75
    start_x = 300 - ADVANCE_WIDTH / 2 + dash_step / 8

    # Half a gap at each cell edge makes repeated characters evenly spaced.

    glyph.add(
        line(
            width,
            (start_x + radius, 400),
            (start_x + dash_length - radius, 400),
        )
    )

    glyph.add(
        line(
            width,
            (start_x + dash_step + radius, 400),
            (start_x + dash_step + dash_length - radius, 400),
        )
    )

    return glyph


def build_box_drawings_light_double_dash_vertical(width: float) -> GlyphDefinition:
    """U+254E ╎ BOX DRAWINGS LIGHT DOUBLE DASH VERTICAL."""
    glyph = init_glyph("uni254E", 0x254E)

    width = width * 0.7
    radius = width / 2

    row_height = VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM
    dash_step = row_height / 2
    dash_length = dash_step * 0.75
    start_y = 400 - row_height / 2 + dash_step / 8

    # Half a gap at each cell edge makes repeated characters evenly spaced.

    glyph.add(
        line(
            width,
            (300, start_y + radius),
            (300, start_y + dash_length - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300, start_y + dash_step + radius),
            (300, start_y + dash_step + dash_length - radius),
        )
    )

    return glyph


def build_box_drawings_heavy_double_dash_vertical(width: float) -> GlyphDefinition:
    """U+254F ╏ BOX DRAWINGS HEAVY DOUBLE DASH VERTICAL."""
    glyph = init_glyph("uni254F", 0x254F)

    width = width * 1.3
    radius = width / 2

    row_height = VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM
    dash_step = row_height / 2
    dash_length = dash_step * 0.75
    start_y = 400 - row_height / 2 + dash_step / 8

    # Half a gap at each cell edge makes repeated characters evenly spaced.

    glyph.add(
        line(
            width,
            (300, start_y + radius),
            (300, start_y + dash_length - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300, start_y + dash_step + radius),
            (300, start_y + dash_step + dash_length - radius),
        )
    )

    return glyph


def build_box_drawings_double_horizontal(width: float) -> GlyphDefinition:
    """U+2550 ═ BOX DRAWINGS DOUBLE HORIZONTAL."""
    glyph = init_glyph("uni2550", 0x2550)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (-75 + radius, 400 - offset),
            (675 - radius, 400 - offset),
        )
    )

    glyph.add(
        line(
            width,
            (-75 + radius, 400 + offset),
            (675 - radius, 400 + offset),
        )
    )

    return glyph


def build_box_drawings_double_vertical(width: float) -> GlyphDefinition:
    """U+2551 ║ BOX DRAWINGS DOUBLE VERTICAL."""
    glyph = init_glyph("uni2551", 0x2551)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (300 - offset, -275 + radius),
            (300 - offset, 1075 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300 + offset, -275 + radius),
            (300 + offset, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_down_single_and_right_double(width: float) -> GlyphDefinition:
    """U+2552 ╒ BOX DRAWINGS DOWN SINGLE AND RIGHT DOUBLE."""
    glyph = init_glyph("uni2552", 0x2552)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (300, 400 - offset),
            (705 - radius, 400 - offset),
        )
    )

    glyph.add(
        line(
            width,
            (300, 400 + offset),
            (705 - radius, 400 + offset),
        )
    )

    glyph.add(
        line(
            width,
            (300, 400 + offset),
            (300, -305 + radius),
        )
    )

    return glyph


def build_box_drawings_down_double_and_right_single(width: float) -> GlyphDefinition:
    """U+2553 ╓ BOX DRAWINGS DOWN DOUBLE AND RIGHT SINGLE."""
    glyph = init_glyph("uni2553", 0x2553)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (300 - offset, 400),
            (300 - offset, -305 + radius),
        )
    )

    glyph.add(
        line(
            width,
            (300 + offset, 400),
            (300 + offset, -305 + radius),
        )
    )

    glyph.add(
        line(
            width,
            (300 - offset, 400),
            (705 - radius, 400),
        )
    )

    return glyph


def build_box_drawings_double_down_and_right(width: float) -> GlyphDefinition:
    """U+2554 ╔ BOX DRAWINGS DOUBLE DOWN AND RIGHT."""
    glyph = init_glyph("uni2554", 0x2554)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        polyline(
            width,
            [
                (705 - radius, 400 - offset),
                (300 + offset, 400 - offset),
                (300 + offset, -305 + radius),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (705 - radius, 400 + offset),
                (300 - offset, 400 + offset),
                (300 - offset, -305 + radius),
            ],
        )
    )

    return glyph


def build_box_drawings_down_single_and_left_double(width: float) -> GlyphDefinition:
    """U+2555 ╕ BOX DRAWINGS DOWN SINGLE AND LEFT DOUBLE."""
    glyph = init_glyph("uni2555", 0x2555)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (300, 400 - offset),
            (-105 + radius, 400 - offset),
        )
    )

    glyph.add(
        line(
            width,
            (300, 400 + offset),
            (-105 + radius, 400 + offset),
        )
    )

    glyph.add(
        line(
            width,
            (300, 400 + offset),
            (300, -305 + radius),
        )
    )

    return glyph


def build_box_drawings_down_double_and_left_single(width: float) -> GlyphDefinition:
    """U+2556 ╖ BOX DRAWINGS DOWN DOUBLE AND LEFT SINGLE."""
    glyph = init_glyph("uni2556", 0x2556)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (300 - offset, 400),
            (300 - offset, -305 + radius),
        )
    )

    glyph.add(
        line(
            width,
            (300 + offset, 400),
            (300 + offset, -305 + radius),
        )
    )

    glyph.add(
        line(
            width,
            (300 + offset, 400),
            (-105 + radius, 400),
        )
    )

    return glyph


def build_box_drawings_double_down_and_left(width: float) -> GlyphDefinition:
    """U+2557 ╗ BOX DRAWINGS DOUBLE DOWN AND LEFT."""
    glyph = init_glyph("uni2557", 0x2557)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        polyline(
            width,
            [
                (-105 + radius, 400 - offset),
                (300 - offset, 400 - offset),
                (300 - offset, -305 + radius),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (-105 + radius, 400 + offset),
                (300 + offset, 400 + offset),
                (300 + offset, -305 + radius),
            ],
        )
    )

    return glyph


def build_box_drawings_up_single_and_right_double(width: float) -> GlyphDefinition:
    """U+2558 ╘ BOX DRAWINGS UP SINGLE AND RIGHT DOUBLE."""
    glyph = init_glyph("uni2558", 0x2558)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (300, 400 - offset),
            (705 - radius, 400 - offset),
        )
    )

    glyph.add(
        line(
            width,
            (300, 400 + offset),
            (705 - radius, 400 + offset),
        )
    )

    glyph.add(
        line(
            width,
            (300, 400 - offset),
            (300, 1105 - radius),
        )
    )

    return glyph


def build_box_drawings_up_double_and_right_single(width: float) -> GlyphDefinition:
    """U+2559 ╙ BOX DRAWINGS UP DOUBLE AND RIGHT SINGLE."""
    glyph = init_glyph("uni2559", 0x2559)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (300 - offset, 400),
            (300 - offset, 1105 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300 + offset, 400),
            (300 + offset, 1105 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300 - offset, 400),
            (705 - radius, 400),
        )
    )

    return glyph


def build_box_drawings_double_up_and_right(width: float) -> GlyphDefinition:
    """U+255A ╚ BOX DRAWINGS DOUBLE UP AND RIGHT."""
    glyph = init_glyph("uni255A", 0x255A)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        polyline(
            width,
            [
                (705 - radius, 400 + offset),
                (300 + offset, 400 + offset),
                (300 + offset, 1105 - radius),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (705 - radius, 400 - offset),
                (300 - offset, 400 - offset),
                (300 - offset, 1105 - radius),
            ],
        )
    )

    return glyph


def build_box_drawings_up_single_and_left_double(width: float) -> GlyphDefinition:
    """U+255B ╛ BOX DRAWINGS UP SINGLE AND LEFT DOUBLE."""
    glyph = init_glyph("uni255B", 0x255B)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (300, 400 - offset),
            (-105 + radius, 400 - offset),
        )
    )

    glyph.add(
        line(
            width,
            (300, 400 + offset),
            (-105 + radius, 400 + offset),
        )
    )

    glyph.add(
        line(
            width,
            (300, 400 - offset),
            (300, 1105 - radius),
        )
    )

    return glyph


def build_box_drawings_up_double_and_left_single(width: float) -> GlyphDefinition:
    """U+255C ╜ BOX DRAWINGS UP DOUBLE AND LEFT SINGLE."""
    glyph = init_glyph("uni255C", 0x255C)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (300 - offset, 400),
            (300 - offset, 1105 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300 + offset, 400),
            (300 + offset, 1105 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300 + offset, 400),
            (-105 + radius, 400),
        )
    )

    return glyph


def build_box_drawings_double_up_and_left(width: float) -> GlyphDefinition:
    """U+255D ╝ BOX DRAWINGS DOUBLE UP AND LEFT."""
    glyph = init_glyph("uni255D", 0x255D)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        polyline(
            width,
            [
                (-105 + radius, 400 + offset),
                (300 - offset, 400 + offset),
                (300 - offset, 1105 - radius),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (-105 + radius, 400 - offset),
                (300 + offset, 400 - offset),
                (300 + offset, 1105 - radius),
            ],
        )
    )

    return glyph


def build_box_drawings_vertical_single_and_right_double(width: float) -> GlyphDefinition:
    """U+255E ╞ BOX DRAWINGS VERTICAL SINGLE AND RIGHT DOUBLE."""
    glyph = init_glyph("uni255E", 0x255E)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (300, 400 - offset),
            (675 - radius, 400 - offset),
        )
    )

    glyph.add(
        line(
            width,
            (300, 400 + offset),
            (675 - radius, 400 + offset),
        )
    )

    glyph.add(
        line(
            width,
            (300, -275 + radius),
            (300, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_vertical_double_and_right_single(width: float) -> GlyphDefinition:
    """U+255F ╟ BOX DRAWINGS VERTICAL DOUBLE AND RIGHT SINGLE."""
    glyph = init_glyph("uni255F", 0x255F)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (300 - offset, -275 + radius),
            (300 - offset, 1075 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300 + offset, -275 + radius),
            (300 + offset, 1075 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300 + offset, 400),
            (675 - radius, 400),
        )
    )

    return glyph


def build_box_drawings_double_vertical_and_right(width: float) -> GlyphDefinition:
    """U+2560 ╠ BOX DRAWINGS DOUBLE VERTICAL AND RIGHT."""
    glyph = init_glyph("uni2560", 0x2560)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        polyline(
            width,
            [
                (675 - radius, 400 - offset),
                (300 + offset, 400 - offset),
                (300 + offset, -275 + radius),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (675 - radius, 400 + offset),
                (300 + offset, 400 + offset),
                (300 + offset, 1075 - radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (300 - offset, -275 + radius),
            (300 - offset, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_vertical_single_and_left_double(width: float) -> GlyphDefinition:
    """U+2561 ╡ BOX DRAWINGS VERTICAL SINGLE AND LEFT DOUBLE."""
    glyph = init_glyph("uni2561", 0x2561)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (300, 400 - offset),
            (-75 + radius, 400 - offset),
        )
    )

    glyph.add(
        line(
            width,
            (300, 400 + offset),
            (-75 + radius, 400 + offset),
        )
    )

    glyph.add(
        line(
            width,
            (300, -275 + radius),
            (300, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_vertical_double_and_left_single(width: float) -> GlyphDefinition:
    """U+2562 ╢ BOX DRAWINGS VERTICAL DOUBLE AND LEFT SINGLE."""
    glyph = init_glyph("uni2562", 0x2562)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (300 - offset, -275 + radius),
            (300 - offset, 1075 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300 + offset, -275 + radius),
            (300 + offset, 1075 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300 - offset, 400),
            (-75 + radius, 400),
        )
    )

    return glyph


def build_box_drawings_double_vertical_and_left(width: float) -> GlyphDefinition:
    """U+2563 ╣ BOX DRAWINGS DOUBLE VERTICAL AND LEFT."""
    glyph = init_glyph("uni2563", 0x2563)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        polyline(
            width,
            [
                (-75 + radius, 400 - offset),
                (300 - offset, 400 - offset),
                (300 - offset, -275 + radius),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (-75 + radius, 400 + offset),
                (300 - offset, 400 + offset),
                (300 - offset, 1075 - radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (300 + offset, -275 + radius),
            (300 + offset, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_down_single_and_horizontal_double(width: float) -> GlyphDefinition:
    """U+2564 ╤ BOX DRAWINGS DOWN SINGLE AND HORIZONTAL DOUBLE."""
    glyph = init_glyph("uni2564", 0x2564)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (-75 + radius, 400 - offset),
            (675 - radius, 400 - offset),
        )
    )

    glyph.add(
        line(
            width,
            (-75 + radius, 400 + offset),
            (675 - radius, 400 + offset),
        )
    )

    glyph.add(
        line(
            width,
            (300, 400 - offset),
            (300, -275 + radius),
        )
    )

    return glyph


def build_box_drawings_down_double_and_horizontal_single(width: float) -> GlyphDefinition:
    """U+2565 ╥ BOX DRAWINGS DOWN DOUBLE AND HORIZONTAL SINGLE."""
    glyph = init_glyph("uni2565", 0x2565)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (300 - offset, 400),
            (300 - offset, -275 + radius),
        )
    )

    glyph.add(
        line(
            width,
            (300 + offset, 400),
            (300 + offset, -275 + radius),
        )
    )

    glyph.add(
        line(
            width,
            (-75 + radius, 400),
            (675 - radius, 400),
        )
    )

    return glyph


def build_box_drawings_double_down_and_horizontal(width: float) -> GlyphDefinition:
    """U+2566 ╦ BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL."""
    glyph = init_glyph("uni2566", 0x2566)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        polyline(
            width,
            [
                (-75 + radius, 400 - offset),
                (300 - offset, 400 - offset),
                (300 - offset, -275 + radius),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (675 - radius, 400 - offset),
                (300 + offset, 400 - offset),
                (300 + offset, -275 + radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (-75 + radius, 400 + offset),
            (675 - radius, 400 + offset),
        )
    )

    return glyph


def build_box_drawings_up_single_and_horizontal_double(width: float) -> GlyphDefinition:
    """U+2567 ╧ BOX DRAWINGS UP SINGLE AND HORIZONTAL DOUBLE."""
    glyph = init_glyph("uni2567", 0x2567)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (-75 + radius, 400 - offset),
            (675 - radius, 400 - offset),
        )
    )

    glyph.add(
        line(
            width,
            (-75 + radius, 400 + offset),
            (675 - radius, 400 + offset),
        )
    )

    glyph.add(
        line(
            width,
            (300, 400 + offset),
            (300, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_up_double_and_horizontal_single(width: float) -> GlyphDefinition:
    """U+2568 ╨ BOX DRAWINGS UP DOUBLE AND HORIZONTAL SINGLE."""
    glyph = init_glyph("uni2568", 0x2568)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (300 - offset, 400),
            (300 - offset, 1075 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300 + offset, 400),
            (300 + offset, 1075 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (-75 + radius, 400),
            (675 - radius, 400),
        )
    )

    return glyph


def build_box_drawings_double_up_and_horizontal(width: float) -> GlyphDefinition:
    """U+2569 ╩ BOX DRAWINGS DOUBLE UP AND HORIZONTAL."""
    glyph = init_glyph("uni2569", 0x2569)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        polyline(
            width,
            [
                (-75 + radius, 400 + offset),
                (300 - offset, 400 + offset),
                (300 - offset, 1075 - radius),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (675 - radius, 400 + offset),
                (300 + offset, 400 + offset),
                (300 + offset, 1075 - radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (-75 + radius, 400 - offset),
            (675 - radius, 400 - offset),
        )
    )

    return glyph


def build_box_drawings_vertical_single_and_horizontal_double(width: float) -> GlyphDefinition:
    """U+256A ╪ BOX DRAWINGS VERTICAL SINGLE AND HORIZONTAL DOUBLE."""
    glyph = init_glyph("uni256A", 0x256A)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (-75 + radius, 400 - offset),
            (675 - radius, 400 - offset),
        )
    )

    glyph.add(
        line(
            width,
            (-75 + radius, 400 + offset),
            (675 - radius, 400 + offset),
        )
    )

    glyph.add(
        line(
            width,
            (300, -275 + radius),
            (300, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_vertical_double_and_horizontal_single(width: float) -> GlyphDefinition:
    """U+256B ╫ BOX DRAWINGS VERTICAL DOUBLE AND HORIZONTAL SINGLE."""
    glyph = init_glyph("uni256B", 0x256B)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        line(
            width,
            (300 - offset, -275 + radius),
            (300 - offset, 1075 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (300 + offset, -275 + radius),
            (300 + offset, 1075 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (-75 + radius, 400),
            (675 - radius, 400),
        )
    )

    return glyph


def build_box_drawings_double_vertical_and_horizontal(width: float) -> GlyphDefinition:
    """U+256C ╬ BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL."""
    glyph = init_glyph("uni256C", 0x256C)

    width = width * 0.7
    radius = width / 2
    offset = width * 1.5

    glyph.add(
        polyline(
            width,
            [
                (-75 + radius, 400 - offset),
                (300 - offset, 400 - offset),
                (300 - offset, -275 + radius),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (-75 + radius, 400 + offset),
                (300 - offset, 400 + offset),
                (300 - offset, 1075 - radius),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (675 - radius, 400 - offset),
                (300 + offset, 400 - offset),
                (300 + offset, -275 + radius),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (675 - radius, 400 + offset),
                (300 + offset, 400 + offset),
                (300 + offset, 1075 - radius),
            ],
        )
    )

    return glyph


def build_box_drawings_light_arc_down_and_right(width: float) -> GlyphDefinition:
    """U+256D ╭ BOX DRAWINGS LIGHT ARC DOWN AND RIGHT."""
    glyph = init_glyph("uni256D", 0x256D)

    width = width * 0.7
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph.add(
        polyline(
            width,
            [
                (300, -305 + radius),
                (300, 200 + radius - diagonal_offset),
                (500 - radius + diagonal_offset, 400),
                (705 - radius, 400),
            ],
        )
    )

    return glyph


def build_box_drawings_light_arc_down_and_left(width: float) -> GlyphDefinition:
    """U+256E ╮ BOX DRAWINGS LIGHT ARC DOWN AND LEFT."""
    glyph = init_glyph("uni256E", 0x256E)

    width = width * 0.7
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph.add(
        polyline(
            width,
            [
                (300, -305 + radius),
                (300, 200 + radius - diagonal_offset),
                (100 + radius - diagonal_offset, 400),
                (-105 + radius, 400),
            ],
        )
    )

    return glyph


def build_box_drawings_light_arc_up_and_left(width: float) -> GlyphDefinition:
    """U+256F ╯ BOX DRAWINGS LIGHT ARC UP AND LEFT."""
    glyph = init_glyph("uni256F", 0x256F)

    width = width * 0.7
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph.add(
        polyline(
            width,
            [
                (300, 1105 - radius),
                (300, 600 - radius + diagonal_offset),
                (100 + radius - diagonal_offset, 400),
                (-105 + radius, 400),
            ],
        )
    )

    return glyph


def build_box_drawings_light_arc_up_and_right(width: float) -> GlyphDefinition:
    """U+2570 ╰ BOX DRAWINGS LIGHT ARC UP AND RIGHT."""
    glyph = init_glyph("uni2570", 0x2570)

    width = width * 0.7
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph.add(
        polyline(
            width,
            [
                (300, 1105 - radius),
                (300, 600 - radius + diagonal_offset),
                (500 - radius + diagonal_offset, 400),
                (705 - radius, 400),
            ],
        )
    )

    return glyph


def build_box_drawings_light_diagonal_upper_right_to_lower_left(width: float) -> GlyphDefinition:
    """U+2571 ╱ BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT."""
    glyph = init_glyph("uni2571", 0x2571)

    width = width * 0.7
    radius = width / 2
    row_height = VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM
    diagonal_length = math.hypot(ADVANCE_WIDTH, row_height)

    # Match the cell's diagonal without extending past its corner centers.
    direction_x = ADVANCE_WIDTH / diagonal_length
    direction_y = row_height / diagonal_length
    left = 300 - ADVANCE_WIDTH / 2
    right = 300 + ADVANCE_WIDTH / 2
    bottom = 400 - row_height / 2
    top = 400 + row_height / 2

    # Fit the existing square caps inside the diagonal's full stroke width.
    # Offset the two overlapping passes to preserve that width along the body.
    stroke_width = width / (direction_x + direction_y)
    stroke_radius = stroke_width / 2
    diagonal_x_offset = direction_y * (radius - stroke_radius)
    diagonal_y_offset = direction_x * (radius - stroke_radius)

    glyph.add(
        polyline(
            stroke_width,
            [
                (left, bottom),
                (left - diagonal_x_offset, bottom + diagonal_y_offset),
                (right - diagonal_x_offset, top + diagonal_y_offset),
                (right + diagonal_x_offset, top - diagonal_y_offset),
                (left + diagonal_x_offset, bottom - diagonal_y_offset),
                (left, bottom),
            ],
        )
    )

    return glyph


def build_box_drawings_light_diagonal_upper_left_to_lower_right(width: float) -> GlyphDefinition:
    """U+2572 ╲ BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT."""
    glyph = init_glyph("uni2572", 0x2572)

    width = width * 0.7
    radius = width / 2
    row_height = VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM
    diagonal_length = math.hypot(ADVANCE_WIDTH, row_height)

    # Match the cell's diagonal without extending past its corner centers.
    direction_x = ADVANCE_WIDTH / diagonal_length
    direction_y = row_height / diagonal_length
    left = 300 - ADVANCE_WIDTH / 2
    right = 300 + ADVANCE_WIDTH / 2
    bottom = 400 - row_height / 2
    top = 400 + row_height / 2

    # Fit the existing square caps inside the diagonal's full stroke width.
    # Offset the two overlapping passes to preserve that width along the body.
    stroke_width = width / (direction_x + direction_y)
    stroke_radius = stroke_width / 2
    diagonal_x_offset = direction_y * (radius - stroke_radius)
    diagonal_y_offset = direction_x * (radius - stroke_radius)

    glyph.add(
        polyline(
            stroke_width,
            [
                (left, top),
                (left - diagonal_x_offset, top - diagonal_y_offset),
                (right - diagonal_x_offset, bottom - diagonal_y_offset),
                (right + diagonal_x_offset, bottom + diagonal_y_offset),
                (left + diagonal_x_offset, top + diagonal_y_offset),
                (left, top),
            ],
        )
    )

    return glyph


def build_box_drawings_light_diagonal_cross(width: float) -> GlyphDefinition:
    """U+2573 ╳ BOX DRAWINGS LIGHT DIAGONAL CROSS."""
    glyph = init_glyph("uni2573", 0x2573)

    width = width * 0.7
    radius = width / 2
    row_height = VERTICAL_BOX_TOP - VERTICAL_BOX_BOTTOM
    diagonal_length = math.hypot(ADVANCE_WIDTH, row_height)

    # Match the cell's diagonal without extending past its corner centers.
    direction_x = ADVANCE_WIDTH / diagonal_length
    direction_y = row_height / diagonal_length
    left = 300 - ADVANCE_WIDTH / 2
    right = 300 + ADVANCE_WIDTH / 2
    bottom = 400 - row_height / 2
    top = 400 + row_height / 2

    # Fit the existing square caps inside the diagonal's full stroke width.
    # Offset the two overlapping passes to preserve that width along the body.
    stroke_width = width / (direction_x + direction_y)
    stroke_radius = stroke_width / 2
    diagonal_x_offset = direction_y * (radius - stroke_radius)
    diagonal_y_offset = direction_x * (radius - stroke_radius)

    glyph.add(
        polyline(
            stroke_width,
            [
                (left, bottom),
                (left - diagonal_x_offset, bottom + diagonal_y_offset),
                (right - diagonal_x_offset, top + diagonal_y_offset),
                (right + diagonal_x_offset, top - diagonal_y_offset),
                (left + diagonal_x_offset, bottom - diagonal_y_offset),
                (left, bottom),
            ],
        )
    )

    glyph.add(
        polyline(
            stroke_width,
            [
                (left, top),
                (left - diagonal_x_offset, top - diagonal_y_offset),
                (right - diagonal_x_offset, bottom - diagonal_y_offset),
                (right + diagonal_x_offset, bottom + diagonal_y_offset),
                (left + diagonal_x_offset, top + diagonal_y_offset),
                (left, top),
            ],
        )
    )

    return glyph


def build_box_drawings_light_left(width: float) -> GlyphDefinition:
    """U+2574 ╴ BOX DRAWINGS LIGHT LEFT."""
    glyph = init_glyph("uni2574", 0x2574)

    width = width * 0.7
    radius = width / 2

    glyph.add(
        line(
            width,
            (-75 + radius, 400),
            (300 - radius, 400),
        )
    )

    return glyph


def build_box_drawings_light_up(width: float) -> GlyphDefinition:
    """U+2575 ╵ BOX DRAWINGS LIGHT UP."""
    glyph = init_glyph("uni2575", 0x2575)

    width = width * 0.7
    radius = width / 2

    glyph.add(
        line(
            width,
            (300, 400 + radius),
            (300, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_light_right(width: float) -> GlyphDefinition:
    """U+2576 ╶ BOX DRAWINGS LIGHT RIGHT."""
    glyph = init_glyph("uni2576", 0x2576)

    width = width * 0.7
    radius = width / 2

    glyph.add(
        line(
            width,
            (300 + radius, 400),
            (675 - radius, 400),
        )
    )

    return glyph


def build_box_drawings_light_down(width: float) -> GlyphDefinition:
    """U+2577 ╷ BOX DRAWINGS LIGHT DOWN."""
    glyph = init_glyph("uni2577", 0x2577)

    width = width * 0.7
    radius = width / 2

    glyph.add(
        line(
            width,
            (300, -275 + radius),
            (300, 400 - radius),
        )
    )

    return glyph


def build_box_drawings_heavy_left(width: float) -> GlyphDefinition:
    """U+2578 ╸ BOX DRAWINGS HEAVY LEFT."""
    glyph = init_glyph("uni2578", 0x2578)

    width = width * 1.3
    radius = width / 2

    glyph.add(
        line(
            width,
            (-75 + radius, 400),
            (300 - radius, 400),
        )
    )

    return glyph


def build_box_drawings_heavy_up(width: float) -> GlyphDefinition:
    """U+2579 ╹ BOX DRAWINGS HEAVY UP."""
    glyph = init_glyph("uni2579", 0x2579)

    width = width * 1.3
    radius = width / 2

    glyph.add(
        line(
            width,
            (300, 400 + radius),
            (300, 1075 - radius),
        )
    )

    return glyph


def build_box_drawings_heavy_right(width: float) -> GlyphDefinition:
    """U+257A ╺ BOX DRAWINGS HEAVY RIGHT."""
    glyph = init_glyph("uni257A", 0x257A)

    width = width * 1.3
    radius = width / 2

    glyph.add(
        line(
            width,
            (300 + radius, 400),
            (675 - radius, 400),
        )
    )

    return glyph


def build_box_drawings_heavy_down(width: float) -> GlyphDefinition:
    """U+257B ╻ BOX DRAWINGS HEAVY DOWN."""
    glyph = init_glyph("uni257B", 0x257B)

    width = width * 1.3
    radius = width / 2

    glyph.add(
        line(
            width,
            (300, -275 + radius),
            (300, 400 - radius),
        )
    )

    return glyph


def build_box_drawings_light_left_and_heavy_right(width: float) -> GlyphDefinition:
    """U+257C ╼ BOX DRAWINGS LIGHT LEFT AND HEAVY RIGHT."""
    glyph = init_glyph("uni257C", 0x257C)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (-75 + light_radius, 400),
            (300 - light_radius, 400),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300 + heavy_radius, 400),
            (675 - heavy_radius, 400),
        )
    )

    return glyph


def build_box_drawings_light_up_and_heavy_down(width: float) -> GlyphDefinition:
    """U+257D ╽ BOX DRAWINGS LIGHT UP AND HEAVY DOWN."""
    glyph = init_glyph("uni257D", 0x257D)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (300, -275 + heavy_radius),
            (300, 400 - heavy_radius),
        )
    )

    glyph.add(
        line(
            light_width,
            (300, 400 + light_radius),
            (300, 1075 - light_radius),
        )
    )

    return glyph


def build_box_drawings_heavy_left_and_light_right(width: float) -> GlyphDefinition:
    """U+257E ╾ BOX DRAWINGS HEAVY LEFT AND LIGHT RIGHT."""
    glyph = init_glyph("uni257E", 0x257E)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            heavy_width,
            (-75 + heavy_radius, 400),
            (300 - heavy_radius, 400),
        )
    )

    glyph.add(
        line(
            light_width,
            (300 + light_radius, 400),
            (675 - light_radius, 400),
        )
    )

    return glyph


def build_box_drawings_heavy_up_and_light_down(width: float) -> GlyphDefinition:
    """U+257F ╿ BOX DRAWINGS HEAVY UP AND LIGHT DOWN."""
    glyph = init_glyph("uni257F", 0x257F)

    light_width = width * 0.7
    heavy_width = width * 1.3
    light_radius = light_width / 2
    heavy_radius = heavy_width / 2

    glyph.add(
        line(
            light_width,
            (300, -275 + light_radius),
            (300, 400 - light_radius),
        )
    )

    glyph.add(
        line(
            heavy_width,
            (300, 400 + heavy_radius),
            (300, 1075 - heavy_radius),
        )
    )

    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    "\u2500": build_box_drawings_light_horizontal,
    "\u2501": build_box_drawings_heavy_horizontal,
    "\u2502": build_box_drawings_light_vertical,
    "\u2503": build_box_drawings_heavy_vertical,
    "\u2504": build_box_drawings_light_triple_dash_horizontal,
    "\u2505": build_box_drawings_heavy_triple_dash_horizontal,
    "\u2506": build_box_drawings_light_triple_dash_vertical,
    "\u2507": build_box_drawings_heavy_triple_dash_vertical,
    "\u2508": build_box_drawings_light_quadruple_dash_horizontal,
    "\u2509": build_box_drawings_heavy_quadruple_dash_horizontal,
    "\u250A": build_box_drawings_light_quadruple_dash_vertical,
    "\u250B": build_box_drawings_heavy_quadruple_dash_vertical,
    "\u250C": build_box_drawings_light_down_and_right,
    "\u250D": build_box_drawings_down_light_and_right_heavy,
    "\u250E": build_box_drawings_down_heavy_and_right_light,
    "\u250F": build_box_drawings_heavy_down_and_right,
    "\u2510": build_box_drawings_light_down_and_left,
    "\u2511": build_box_drawings_down_light_and_left_heavy,
    "\u2512": build_box_drawings_down_heavy_and_left_light,
    "\u2513": build_box_drawings_heavy_down_and_left,
    "\u2514": build_box_drawings_light_up_and_right,
    "\u2515": build_box_drawings_up_light_and_right_heavy,
    "\u2516": build_box_drawings_up_heavy_and_right_light,
    "\u2517": build_box_drawings_heavy_up_and_right,
    "\u2518": build_box_drawings_light_up_and_left,
    "\u2519": build_box_drawings_up_light_and_left_heavy,
    "\u251A": build_box_drawings_up_heavy_and_left_light,
    "\u251B": build_box_drawings_heavy_up_and_left,
    "\u251C": build_box_drawings_light_vertical_and_right,
    "\u251D": build_box_drawings_vertical_light_and_right_heavy,
    "\u251E": build_box_drawings_up_heavy_and_right_down_light,
    "\u251F": build_box_drawings_down_heavy_and_right_up_light,
    "\u2520": build_box_drawings_vertical_heavy_and_right_light,
    "\u2521": build_box_drawings_down_light_and_right_up_heavy,
    "\u2522": build_box_drawings_up_light_and_right_down_heavy,
    "\u2523": build_box_drawings_heavy_vertical_and_right,
    "\u2524": build_box_drawings_light_vertical_and_left,
    "\u2525": build_box_drawings_vertical_light_and_left_heavy,
    "\u2526": build_box_drawings_up_heavy_and_left_down_light,
    "\u2527": build_box_drawings_down_heavy_and_left_up_light,
    "\u2528": build_box_drawings_vertical_heavy_and_left_light,
    "\u2529": build_box_drawings_down_light_and_left_up_heavy,
    "\u252A": build_box_drawings_up_light_and_left_down_heavy,
    "\u252B": build_box_drawings_heavy_vertical_and_left,
    "\u252C": build_box_drawings_light_down_and_horizontal,
    "\u252D": build_box_drawings_left_heavy_and_right_down_light,
    "\u252E": build_box_drawings_right_heavy_and_left_down_light,
    "\u252F": build_box_drawings_down_light_and_horizontal_heavy,
    "\u2530": build_box_drawings_down_heavy_and_horizontal_light,
    "\u2531": build_box_drawings_right_light_and_left_down_heavy,
    "\u2532": build_box_drawings_left_light_and_right_down_heavy,
    "\u2533": build_box_drawings_heavy_down_and_horizontal,
    "\u2534": build_box_drawings_light_up_and_horizontal,
    "\u2535": build_box_drawings_left_heavy_and_right_up_light,
    "\u2536": build_box_drawings_right_heavy_and_left_up_light,
    "\u2537": build_box_drawings_up_light_and_horizontal_heavy,
    "\u2538": build_box_drawings_up_heavy_and_horizontal_light,
    "\u2539": build_box_drawings_right_light_and_left_up_heavy,
    "\u253A": build_box_drawings_left_light_and_right_up_heavy,
    "\u253B": build_box_drawings_heavy_up_and_horizontal,
    "\u253C": build_box_drawings_light_vertical_and_horizontal,
    "\u253D": build_box_drawings_left_heavy_and_right_vertical_light,
    "\u253E": build_box_drawings_right_heavy_and_left_vertical_light,
    "\u253F": build_box_drawings_vertical_light_and_horizontal_heavy,
    "\u2540": build_box_drawings_up_heavy_and_down_horizontal_light,
    "\u2541": build_box_drawings_down_heavy_and_up_horizontal_light,
    "\u2542": build_box_drawings_vertical_heavy_and_horizontal_light,
    "\u2543": build_box_drawings_left_up_heavy_and_right_down_light,
    "\u2544": build_box_drawings_right_up_heavy_and_left_down_light,
    "\u2545": build_box_drawings_left_down_heavy_and_right_up_light,
    "\u2546": build_box_drawings_right_down_heavy_and_left_up_light,
    "\u2547": build_box_drawings_down_light_and_up_horizontal_heavy,
    "\u2548": build_box_drawings_up_light_and_down_horizontal_heavy,
    "\u2549": build_box_drawings_right_light_and_left_vertical_heavy,
    "\u254A": build_box_drawings_left_light_and_right_vertical_heavy,
    "\u254B": build_box_drawings_heavy_vertical_and_horizontal,
    "\u254C": build_box_drawings_light_double_dash_horizontal,
    "\u254D": build_box_drawings_heavy_double_dash_horizontal,
    "\u254E": build_box_drawings_light_double_dash_vertical,
    "\u254F": build_box_drawings_heavy_double_dash_vertical,
    "\u2550": build_box_drawings_double_horizontal,
    "\u2551": build_box_drawings_double_vertical,
    "\u2552": build_box_drawings_down_single_and_right_double,
    "\u2553": build_box_drawings_down_double_and_right_single,
    "\u2554": build_box_drawings_double_down_and_right,
    "\u2555": build_box_drawings_down_single_and_left_double,
    "\u2556": build_box_drawings_down_double_and_left_single,
    "\u2557": build_box_drawings_double_down_and_left,
    "\u2558": build_box_drawings_up_single_and_right_double,
    "\u2559": build_box_drawings_up_double_and_right_single,
    "\u255A": build_box_drawings_double_up_and_right,
    "\u255B": build_box_drawings_up_single_and_left_double,
    "\u255C": build_box_drawings_up_double_and_left_single,
    "\u255D": build_box_drawings_double_up_and_left,
    "\u255E": build_box_drawings_vertical_single_and_right_double,
    "\u255F": build_box_drawings_vertical_double_and_right_single,
    "\u2560": build_box_drawings_double_vertical_and_right,
    "\u2561": build_box_drawings_vertical_single_and_left_double,
    "\u2562": build_box_drawings_vertical_double_and_left_single,
    "\u2563": build_box_drawings_double_vertical_and_left,
    "\u2564": build_box_drawings_down_single_and_horizontal_double,
    "\u2565": build_box_drawings_down_double_and_horizontal_single,
    "\u2566": build_box_drawings_double_down_and_horizontal,
    "\u2567": build_box_drawings_up_single_and_horizontal_double,
    "\u2568": build_box_drawings_up_double_and_horizontal_single,
    "\u2569": build_box_drawings_double_up_and_horizontal,
    "\u256A": build_box_drawings_vertical_single_and_horizontal_double,
    "\u256B": build_box_drawings_vertical_double_and_horizontal_single,
    "\u256C": build_box_drawings_double_vertical_and_horizontal,
    "\u256D": build_box_drawings_light_arc_down_and_right,
    "\u256E": build_box_drawings_light_arc_down_and_left,
    "\u256F": build_box_drawings_light_arc_up_and_left,
    "\u2570": build_box_drawings_light_arc_up_and_right,
    "\u2571": build_box_drawings_light_diagonal_upper_right_to_lower_left,
    "\u2572": build_box_drawings_light_diagonal_upper_left_to_lower_right,
    "\u2573": build_box_drawings_light_diagonal_cross,
    "\u2574": build_box_drawings_light_left,
    "\u2575": build_box_drawings_light_up,
    "\u2576": build_box_drawings_light_right,
    "\u2577": build_box_drawings_light_down,
    "\u2578": build_box_drawings_heavy_left,
    "\u2579": build_box_drawings_heavy_up,
    "\u257A": build_box_drawings_heavy_right,
    "\u257B": build_box_drawings_heavy_down,
    "\u257C": build_box_drawings_light_left_and_heavy_right,
    "\u257D": build_box_drawings_light_up_and_heavy_down,
    "\u257E": build_box_drawings_heavy_left_and_light_right,
    "\u257F": build_box_drawings_heavy_up_and_light_down,
}


__all__ = [
    "BUILDERS",
    "build_box_drawings_light_horizontal",
    "build_box_drawings_heavy_horizontal",
    "build_box_drawings_light_vertical",
    "build_box_drawings_heavy_vertical",
    "build_box_drawings_light_triple_dash_horizontal",
    "build_box_drawings_heavy_triple_dash_horizontal",
    "build_box_drawings_light_triple_dash_vertical",
    "build_box_drawings_heavy_triple_dash_vertical",
    "build_box_drawings_light_quadruple_dash_horizontal",
    "build_box_drawings_heavy_quadruple_dash_horizontal",
    "build_box_drawings_light_quadruple_dash_vertical",
    "build_box_drawings_heavy_quadruple_dash_vertical",
    "build_box_drawings_light_down_and_right",
    "build_box_drawings_down_light_and_right_heavy",
    "build_box_drawings_down_heavy_and_right_light",
    "build_box_drawings_heavy_down_and_right",
    "build_box_drawings_light_down_and_left",
    "build_box_drawings_down_light_and_left_heavy",
    "build_box_drawings_down_heavy_and_left_light",
    "build_box_drawings_heavy_down_and_left",
    "build_box_drawings_light_up_and_right",
    "build_box_drawings_up_light_and_right_heavy",
    "build_box_drawings_up_heavy_and_right_light",
    "build_box_drawings_heavy_up_and_right",
    "build_box_drawings_light_up_and_left",
    "build_box_drawings_up_light_and_left_heavy",
    "build_box_drawings_up_heavy_and_left_light",
    "build_box_drawings_heavy_up_and_left",
    "build_box_drawings_light_vertical_and_right",
    "build_box_drawings_vertical_light_and_right_heavy",
    "build_box_drawings_up_heavy_and_right_down_light",
    "build_box_drawings_down_heavy_and_right_up_light",
    "build_box_drawings_vertical_heavy_and_right_light",
    "build_box_drawings_down_light_and_right_up_heavy",
    "build_box_drawings_up_light_and_right_down_heavy",
    "build_box_drawings_heavy_vertical_and_right",
    "build_box_drawings_light_vertical_and_left",
    "build_box_drawings_vertical_light_and_left_heavy",
    "build_box_drawings_up_heavy_and_left_down_light",
    "build_box_drawings_down_heavy_and_left_up_light",
    "build_box_drawings_vertical_heavy_and_left_light",
    "build_box_drawings_down_light_and_left_up_heavy",
    "build_box_drawings_up_light_and_left_down_heavy",
    "build_box_drawings_heavy_vertical_and_left",
    "build_box_drawings_light_down_and_horizontal",
    "build_box_drawings_left_heavy_and_right_down_light",
    "build_box_drawings_right_heavy_and_left_down_light",
    "build_box_drawings_down_light_and_horizontal_heavy",
    "build_box_drawings_down_heavy_and_horizontal_light",
    "build_box_drawings_right_light_and_left_down_heavy",
    "build_box_drawings_left_light_and_right_down_heavy",
    "build_box_drawings_heavy_down_and_horizontal",
    "build_box_drawings_light_up_and_horizontal",
    "build_box_drawings_left_heavy_and_right_up_light",
    "build_box_drawings_right_heavy_and_left_up_light",
    "build_box_drawings_up_light_and_horizontal_heavy",
    "build_box_drawings_up_heavy_and_horizontal_light",
    "build_box_drawings_right_light_and_left_up_heavy",
    "build_box_drawings_left_light_and_right_up_heavy",
    "build_box_drawings_heavy_up_and_horizontal",
    "build_box_drawings_light_vertical_and_horizontal",
    "build_box_drawings_left_heavy_and_right_vertical_light",
    "build_box_drawings_right_heavy_and_left_vertical_light",
    "build_box_drawings_vertical_light_and_horizontal_heavy",
    "build_box_drawings_up_heavy_and_down_horizontal_light",
    "build_box_drawings_down_heavy_and_up_horizontal_light",
    "build_box_drawings_vertical_heavy_and_horizontal_light",
    "build_box_drawings_left_up_heavy_and_right_down_light",
    "build_box_drawings_right_up_heavy_and_left_down_light",
    "build_box_drawings_left_down_heavy_and_right_up_light",
    "build_box_drawings_right_down_heavy_and_left_up_light",
    "build_box_drawings_down_light_and_up_horizontal_heavy",
    "build_box_drawings_up_light_and_down_horizontal_heavy",
    "build_box_drawings_right_light_and_left_vertical_heavy",
    "build_box_drawings_left_light_and_right_vertical_heavy",
    "build_box_drawings_heavy_vertical_and_horizontal",
    "build_box_drawings_light_double_dash_horizontal",
    "build_box_drawings_heavy_double_dash_horizontal",
    "build_box_drawings_light_double_dash_vertical",
    "build_box_drawings_heavy_double_dash_vertical",
    "build_box_drawings_double_horizontal",
    "build_box_drawings_double_vertical",
    "build_box_drawings_down_single_and_right_double",
    "build_box_drawings_down_double_and_right_single",
    "build_box_drawings_double_down_and_right",
    "build_box_drawings_down_single_and_left_double",
    "build_box_drawings_down_double_and_left_single",
    "build_box_drawings_double_down_and_left",
    "build_box_drawings_up_single_and_right_double",
    "build_box_drawings_up_double_and_right_single",
    "build_box_drawings_double_up_and_right",
    "build_box_drawings_up_single_and_left_double",
    "build_box_drawings_up_double_and_left_single",
    "build_box_drawings_double_up_and_left",
    "build_box_drawings_vertical_single_and_right_double",
    "build_box_drawings_vertical_double_and_right_single",
    "build_box_drawings_double_vertical_and_right",
    "build_box_drawings_vertical_single_and_left_double",
    "build_box_drawings_vertical_double_and_left_single",
    "build_box_drawings_double_vertical_and_left",
    "build_box_drawings_down_single_and_horizontal_double",
    "build_box_drawings_down_double_and_horizontal_single",
    "build_box_drawings_double_down_and_horizontal",
    "build_box_drawings_up_single_and_horizontal_double",
    "build_box_drawings_up_double_and_horizontal_single",
    "build_box_drawings_double_up_and_horizontal",
    "build_box_drawings_vertical_single_and_horizontal_double",
    "build_box_drawings_vertical_double_and_horizontal_single",
    "build_box_drawings_double_vertical_and_horizontal",
    "build_box_drawings_light_arc_down_and_right",
    "build_box_drawings_light_arc_down_and_left",
    "build_box_drawings_light_arc_up_and_left",
    "build_box_drawings_light_arc_up_and_right",
    "build_box_drawings_light_diagonal_upper_right_to_lower_left",
    "build_box_drawings_light_diagonal_upper_left_to_lower_right",
    "build_box_drawings_light_diagonal_cross",
    "build_box_drawings_light_left",
    "build_box_drawings_light_up",
    "build_box_drawings_light_right",
    "build_box_drawings_light_down",
    "build_box_drawings_heavy_left",
    "build_box_drawings_heavy_up",
    "build_box_drawings_heavy_right",
    "build_box_drawings_heavy_down",
    "build_box_drawings_light_left_and_heavy_right",
    "build_box_drawings_light_up_and_heavy_down",
    "build_box_drawings_heavy_left_and_light_right",
    "build_box_drawings_heavy_up_and_light_down",
]
