"""Procedural builders extracted from the legacy monolithic script."""

from __future__ import annotations

import math

from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition, dot, init_glyph, line, polygon, polyline


def build_space(width: float) -> GlyphDefinition:
    glyph = init_glyph("space", " ")
    return glyph

def build_exclamation(width: float) -> GlyphDefinition:
    radius = width / 2
    dot_radius = width * 0.75

    glyph = init_glyph("exclamation", "!")
    glyph.add(
        dot(
            width * 1.25,
            (300, dot_radius),
        )
    )
    glyph.add(
        line(
            width,
            (300, 250 + radius),
            (300, 800 - radius),
        )
    )
    return glyph

def build_quotedbl(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("quotedbl", '"')
    glyph.add(
        line(
            width,
            (200, 850 - radius),
            (200, 500 + radius),
        )
    )
    glyph.add(
        line(
            width,
            (400, 850 - radius),
            (400, 500 + radius),
        )
    )
    return glyph

def build_numbersign(width: float) -> GlyphDefinition:
    radius = width / 2
    slant_x_offset = (150 / 800) * radius

    glyph = init_glyph("numbersign", "#")

    glyph.add(
        line(
            width,
            (100 + slant_x_offset, radius),
            (250 - slant_x_offset, 800 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (350 + slant_x_offset, radius),
            (500 - slant_x_offset, 800 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (radius, 250),
            (550 - radius, 250),
        )
    )

    glyph.add(
        line(
            width,
            (50 + radius, 550),
            (600 - radius, 550),
        )
    )

    return glyph

def build_dollar(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("dollar", "$")

    # glyph.add(
    #     polyline(
    #         width,
    #         [
    #             (radius, 150 + diagonal_offset),
    #             (150 + diagonal_offset, radius),
    #             (450 - diagonal_offset, radius),
    #             (600 - radius, 150 + diagonal_offset),
    #             (600 - radius, 300 + middle_offset),
    #             (500 - diagonal_offset, 400),
    #             (100 + diagonal_offset, 400),
    #             (radius, 500 - middle_offset),
    #             (radius, 650 - diagonal_offset),
    #             (150 + diagonal_offset, 800 - radius),
    #             (450 - diagonal_offset, 800 - radius),
    #             (600 - radius, 650 - diagonal_offset),
    #         ],
    #     )
    # )
    glyph.add(
        polyline(
            width,
            [
                (radius, 150 + diagonal_offset),
                (150 + diagonal_offset, radius),
                (450 - diagonal_offset, radius),
                (600 - radius, 150 + diagonal_offset),
                (600 - radius, 250 + middle_offset),
                (450 - diagonal_offset, 400),
                (150 + diagonal_offset, 400),
                (radius, 550 - middle_offset),
                (radius, 650 - diagonal_offset),
                (150 + diagonal_offset, 800 - radius),
                (450 - diagonal_offset, 800 - radius),
                (600 - radius, 650 - diagonal_offset),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (300, 900 - radius),
            (300, -100 + radius),
        )
    )

    return glyph

def build_percent(width: float) -> GlyphDefinition:
    radius = width / 2
    ring_scale = (300 - radius) / 300

    width = width * 9 / 10

    glyph = init_glyph("percent", "%")

    glyph.add(
        polyline(
            width,
            [
                # (radius, radius),
                (radius, 100 + radius),
                (600 - radius, 700 - radius),
                # (600 - radius, 800 - radius),
            ],
        )
    )

    glyph.add(
        polygon(
            width,
            [
                (radius, 500 + 150 * ring_scale),
                (radius, 500 + 200 * ring_scale),
                (radius + 100 * ring_scale, 800 - radius),
                (radius + 200 * ring_scale, 800 - radius),
                (300, 500 + 200 * ring_scale),
                (300, 500 + 100 * ring_scale),
                (radius + 200 * ring_scale, 500),
                (radius + 100 * ring_scale, 500),
                (radius, 500 + 100 * ring_scale),
            ],
        )
    )

    glyph.add(
        polygon(
            width,
            [
                (300, radius + 150 * ring_scale),
                (300, radius + 200 * ring_scale),
                (300 + 100 * ring_scale, 300),
                (300 + 200 * ring_scale, 300),
                (600 - radius, radius + 200 * ring_scale),
                (600 - radius, radius + 100 * ring_scale),
                (300 + 200 * ring_scale, radius),
                (300 + 100 * ring_scale, radius),
                (300, radius + 100 * ring_scale),
            ],
        )
    )

    return glyph

def build_ampersand(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("ampersand", "&")
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, radius),

                (50 + radius, 600 - diagonal_offset),

                (50 + radius, 700 - diagonal_offset),
                (150 + diagonal_offset, 800 - radius),

                (300 - diagonal_offset, 800 - radius),

                (400 - radius, 700 - diagonal_offset),
                (400 - radius, 600),

                (radius, 250),
                (radius, 150 + diagonal_offset),
                (150 + diagonal_offset, radius),
                (300, radius),
                (600 - radius, 250),
                (600 - radius, 400 - radius),
            ],
        )
    )

    return glyph

def build_quotesingle(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("quotesingle", "'")
    glyph.add(
        line(
            width,
            (300, 850 - radius),
            (300, 500 + radius),
        )
    )
    return glyph

def build_parenleft(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    inner_y_offset = radius - diagonal_offset

    glyph = init_glyph("parenleft", "(")
    glyph.add(
        polyline(
            width,
            [
                (550 - radius, -150 + radius),
                (400 - diagonal_offset, -150 + radius),
                (250, inner_y_offset),
                (250, 800 - inner_y_offset),
                (400 - diagonal_offset, 950 - radius),
                (550 - radius, 950 - radius),
            ],
        )
    )
    return glyph

def build_parenright(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    inner_y_offset = radius - diagonal_offset

    glyph = init_glyph("parenright", ")")
    glyph.add(
        polyline(
            width,
            [
                (50 + radius, -150 + radius),
                (200 + diagonal_offset, -150 + radius),
                (350, inner_y_offset),
                (350, 800 - inner_y_offset),
                (200 + diagonal_offset, 950 - radius),
                (50 + radius, 950 - radius),
            ],
        )
    )
    return glyph

# def build_asterisk(width: float) -> GlyphDefinition:
#     radius = width / 2

#     glyph = init_glyph("asterisk", "*")

#     # Reference length: same as compensated vertical line
#     line_length = 500 - 2 * radius
#     half_length = line_length / 2

#     # Original diagonal direction is (500, 300) -> normalized to (5, 3) / sqrt(34)
#     diagonal_x = (5 / math.sqrt(34)) * half_length
#     diagonal_y = (3 / math.sqrt(34)) * half_length

#     glyph.add(
#         line(
#             width,
#             (300, 750 - radius),
#             (300, 250 + radius),
#         )
#     )

#     glyph.add(
#         line(
#             width,
#             (300 - diagonal_x, 400 - diagonal_y),
#             (300 + diagonal_x, 400 + diagonal_y),
#         )
#     )

#     glyph.add(
#         line(
#             width,
#             (300 - diagonal_x, 400 + diagonal_y),
#             (300 + diagonal_x, 400 - diagonal_y),
#         )
#     )

#     return glyph

def build_asterisk(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("asterisk", "*")

    # Same compensated centerline length for all three strokes.
    line_length = 500 - 2 * radius
    half_length = line_length / 2

    # Original diagonal direction: 500:300 = 5:3.
    diagonal_x = (5 / math.sqrt(34)) * half_length
    diagonal_y = (3 / math.sqrt(34)) * half_length

    # Whole glyph shifted down by 100 units.
    center_x = 300
    center_y = 300

    glyph.add(
        line(
            width,
            (center_x, 550 - radius),
            (center_x, 50 + radius),
        )
    )

    glyph.add(
        line(
            width,
            (center_x - diagonal_x, center_y - diagonal_y),
            (center_x + diagonal_x, center_y + diagonal_y),
        )
    )

    glyph.add(
        line(
            width,
            (center_x - diagonal_x, center_y + diagonal_y),
            (center_x + diagonal_x, center_y - diagonal_y),
        )
    )

    return glyph

def build_plus(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("plus", "+")
    glyph.add(
        line(
            width,
            (300, 550 - radius),
            (300, 50 + radius),
        )
    )
    glyph.add(
        line(
            width,
            (50 + radius, 300),
            (550 - radius, 300),
        )
    )
    return glyph

def build_comma(width: float) -> GlyphDefinition:
    dot_width = width * 1.5
    dot_radius = dot_width / 2

    tail_width = dot_radius
    tail_radius = tail_width / 2

    # Align visible right edge of tail with visible right edge of dot
    tail_x = 300 + dot_radius - tail_radius

    glyph = init_glyph("comma", ",")

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

def build_hyphen(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("hyphen", "-")
    glyph.add(
        line(
            width,
            (50 + radius, 300),
            (550 - radius, 300),
        )
    )
    return glyph

def build_period(width: float) -> GlyphDefinition:
    dot_width = width * 1.5
    dot_radius = dot_width / 2

    glyph = init_glyph("period", ".")

    glyph.add(
        dot(
            dot_width,
            (300, dot_radius),
        )
    )

    return glyph

def build_slash(width: float) -> GlyphDefinition:
    radius = width / 2

    diagonal_x_offset = (2 / math.sqrt(29)) * radius
    diagonal_y_offset = (5 / math.sqrt(29)) * radius

    glyph = init_glyph("slash", "/")
    glyph.add(
        line(
            width,
            (
                100 + diagonal_x_offset,
                -100 + diagonal_y_offset,
            ),
            (
                500 - diagonal_x_offset,
                900 - diagonal_y_offset,
            ),
        )
    )
    return glyph

def build_colon(width: float) -> GlyphDefinition:
    dot_width = width * 1.5
    dot_radius = dot_width / 2

    glyph = init_glyph("colon", ":")
    glyph.add(
        dot(
            dot_width,
            (300, dot_radius),
        )
    )
    glyph.add(
        dot(
            dot_width,
            (300, 600 - dot_radius),
        )
    )
    return glyph

def build_semicolon(width: float) -> GlyphDefinition:
    dot_width = width * 1.5
    dot_radius = dot_width / 2

    tail_width = dot_radius
    tail_radius = tail_width / 2

    # Align visible right edge of tail with visible right edge of dot
    tail_x = 300 + dot_radius - tail_radius

    glyph = init_glyph("semicolon", ";")

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

    glyph.add(
        dot(
            dot_width,
            (300, 600 - dot_radius),
        )
    )

    return glyph

def build_less(width: float) -> GlyphDefinition:
    radius = width / 2

    diagonal_x_offset = (2 / math.sqrt(5)) * radius
    diagonal_y_offset = (1 / math.sqrt(5)) * radius
    middle_x_offset = math.sqrt(5) * radius

    glyph = init_glyph("less", "<")
    glyph.add(
        polyline(
            width,
            [
                (550 - diagonal_x_offset, 550 - diagonal_y_offset),
                (50 + middle_x_offset, 300),
                (550 - diagonal_x_offset, 50 + diagonal_y_offset),
            ],
        )
    )
    return glyph

def build_equal(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("equal", "=")
    glyph.add(
        line(
            width,
            (50 + radius, 150),
            (550 - radius, 150),
        )
    )
    glyph.add(
        line(
            width,
            (50 + radius, 450),
            (550 - radius, 450),
        )
    )
    return glyph

def build_greater(width: float) -> GlyphDefinition:
    radius = width / 2

    diagonal_x_offset = (2 / math.sqrt(5)) * radius
    diagonal_y_offset = (1 / math.sqrt(5)) * radius
    middle_x_offset = math.sqrt(5) * radius

    glyph = init_glyph("greater", ">")
    glyph.add(
        polyline(
            width,
            [
                (50 + diagonal_x_offset, 550 - diagonal_y_offset),
                (550 - middle_x_offset, 300),
                (50 + diagonal_x_offset, 50 + diagonal_y_offset),
            ],
        )
    )
    return glyph

def build_question(width: float) -> GlyphDefinition:
    radius = width / 2
    dot_width = width * 1.25
    dot_radius = dot_width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    slant_y_offset = (2 / 3) * radius

    glyph = init_glyph("question", "?")

    glyph.add(
        dot(
            dot_width,
            (300, dot_radius),
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (radius, 650 - diagonal_offset),
                (150 + diagonal_offset, 800 - radius),
                (450 - diagonal_offset, 800 - radius),
                (600 - radius, 650 - diagonal_offset),
                (600 - radius, 550 - slant_y_offset),
                (300, 350),
                (300, 250 + radius),
            ],
        )
    )

    return glyph

def build_at(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    inner_offset = radius - diagonal_offset

    width = width * 9 / 10

    glyph = init_glyph("at", "@")

    glyph.add(
        polyline(
            width,
            [
                (600 - radius, radius),
                (600 - radius, 650 - diagonal_offset),
                (450 - diagonal_offset, 800 - radius),
                (150 + diagonal_offset, 800 - radius),
                (radius, 650 - diagonal_offset),
                (radius, -100 + diagonal_offset),
                (100 + diagonal_offset, -200 + radius),
                (500 - diagonal_offset, -200 + radius),
                (600 - radius, -200 + radius),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),

                # Lower-left corner
                (300 - diagonal_offset, radius),
                (200, 100 + inner_offset),

                (200, 300 + diagonal_offset),

                # Upper-left corner — symmetric with lower-left
                (300 - diagonal_offset, 400),

                (450 - diagonal_offset, 400),

                # Top-right unchanged
                (600 - radius, 250 + diagonal_offset),
            ],
        )
    )

    return glyph

def build_bracketleft(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("bracketleft", "[")
    glyph.add(
        polyline(
            width,
            [
                (550 - radius, -150 + radius),
                (250 + radius, -150 + radius),
                (250 + radius, 950 - radius),
                (550 - radius, 950 - radius),
            ],
        )
    )
    return glyph

def build_backslash(width: float) -> GlyphDefinition:
    radius = width / 2

    diagonal_x_offset = (2 / math.sqrt(29)) * radius
    diagonal_y_offset = (5 / math.sqrt(29)) * radius

    glyph = init_glyph("backslash", "\\")
    glyph.add(
        line(
            width,
            (
                500 - diagonal_x_offset,
                -100 + diagonal_y_offset,
            ),
            (
                100 + diagonal_x_offset,
                900 - diagonal_y_offset,
            ),
        )
    )
    return glyph

def build_bracketright(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("bracketright", "]")
    glyph.add(
        polyline(
            width,
            [
                (50 + radius, -150 + radius),
                (350 - radius, -150 + radius),
                (350 - radius, 950 - radius),
                (50 + radius, 950 - radius),
            ],
        )
    )
    return glyph

# def build_asciicircum(width: float) -> GlyphDefinition:
#     radius = width / 2

#     diagonal_x_offset = (2 / math.sqrt(13)) * radius
#     diagonal_y_offset = (3 / math.sqrt(13)) * radius
#     peak_offset = (math.sqrt(13) / 2) * radius

#     glyph = init_glyph("asciicircum", "^")
#     glyph.add(
#         polyline(
#             width,
#             [
#                 (
#                     100 + diagonal_x_offset,
#                     500 + diagonal_y_offset,
#                 ),
#                 (
#                     300,
#                     800 - peak_offset,
#                 ),
#                 (
#                     500 - diagonal_x_offset,
#                     500 + diagonal_y_offset,
#                 ),
#             ],
#         )
#     )
#     return glyph

def build_asciicircum(width: float) -> GlyphDefinition:
    radius = width / 2

    diagonal_x_offset = (4 / math.sqrt(65)) * radius
    diagonal_y_offset = (7 / math.sqrt(65)) * radius
    peak_offset = (math.sqrt(65) / 4) * radius

    glyph = init_glyph("asciicircum", "^")
    glyph.add(
        polyline(
            width,
            [
                (
                    100 + diagonal_x_offset,
                    500 + diagonal_y_offset,
                ),
                (
                    300,
                    850 - peak_offset,
                ),
                (
                    500 - diagonal_x_offset,
                    500 + diagonal_y_offset,
                ),
            ],
        )
    )
    return glyph

def build_underscore(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("underscore", "_")
    glyph.add(
        line(
            width,
            (50 + radius, -150 + radius),
            (550 - radius, -150 + radius),
        )
    )
    return glyph

def build_grave(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = radius / math.sqrt(2)

    glyph = init_glyph("grave", "`")
    glyph.add(
        line(
            width,
            (
                150 + diagonal_offset,
                850 - diagonal_offset,
            ),
            (
                450 - diagonal_offset,
                550 + diagonal_offset,
            ),
        )
    )
    return glyph

# def build_braceleft(width: float) -> GlyphDefinition:
#     radius = width / 2
#     diagonal_offset = (math.sqrt(2) - 1) * radius

#     glyph = init_glyph("braceleft", "{")
#     glyph.add(
#         polyline(
#             width,
#             [
#                 (600 - radius, -150 + radius),
#                 (450 - diagonal_offset, -150 + radius),
#                 (350, -50 + radius - diagonal_offset),
#                 (350, 250 + radius),
#                 (150 + radius, 400),
#                 (350, 550 - radius),
#                 (350, 850 - radius + diagonal_offset),
#                 (450 - diagonal_offset, 950 - radius),
#                 (600 - radius, 950 - radius),
#             ],
#         )
#     )
#     return glyph

def build_braceleft(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    center_offset = (3 / 4) * radius

    glyph = init_glyph("braceleft", "{")
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, -150 + radius),
                (450 - diagonal_offset, -150 + radius),
                (350, -50 + radius - diagonal_offset),
                (350, 250 + center_offset),
                (150 + radius, 400),
                (350, 550 - center_offset),
                (350, 850 - radius + diagonal_offset),
                (450 - diagonal_offset, 950 - radius),
                (600 - radius, 950 - radius),
            ],
        )
    )
    return glyph

def build_bar(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("bar", "|")
    glyph.add(
        line(
            width,
            (300, 900 - radius),
            (300, -100 + radius),
        )
    )
    return glyph


# def build_braceright(width: float) -> GlyphDefinition:
#     radius = width / 2
#     diagonal_offset = (math.sqrt(2) - 1) * radius

#     glyph = init_glyph("braceright", "}")
#     glyph.add(
#         polyline(
#             width,
#             [
#                 (radius, -150 + radius),
#                 (150 + diagonal_offset, -150 + radius),
#                 (250, -50 + radius - diagonal_offset),
#                 (250, 250 + radius),
#                 (450 - radius, 400),
#                 (250, 550 - radius),
#                 (250, 850 - radius + diagonal_offset),
#                 (150 + diagonal_offset, 950 - radius),
#                 (radius, 950 - radius),
#             ],
#         )
#     )
#     return glyph

def build_braceright(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    center_offset = (3 / 4) * radius

    glyph = init_glyph("braceright", "}")
    glyph.add(
        polyline(
            width,
            [
                (radius, -150 + radius),
                (150 + diagonal_offset, -150 + radius),
                (250, -50 + radius - diagonal_offset),
                (250, 250 + center_offset),
                (450 - radius, 400),
                (250, 550 - center_offset),
                (250, 850 - radius + diagonal_offset),
                (150 + diagonal_offset, 950 - radius),
                (radius, 950 - radius),
            ],
        )
    )
    return glyph

def build_asciitilde(width: float) -> GlyphDefinition:
    radius = width / 2
    endpoint_offset = radius / math.sqrt(2)

    glyph = init_glyph("asciitilde", "~")
    glyph.add(
        polyline(
            width,
            [
                (50 + endpoint_offset, 300 + endpoint_offset),
                (150, 400),
                (250, 400),
                (350, 300),
                (450, 300),
                (550 - endpoint_offset, 400 - endpoint_offset),
            ],
        )
    )
    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    ' ': build_space,
    '!': build_exclamation,
    '"': build_quotedbl,
    '#': build_numbersign,
    '$': build_dollar,
    '%': build_percent,
    '&': build_ampersand,
    "'": build_quotesingle,
    '(': build_parenleft,
    ')': build_parenright,
    '*': build_asterisk,
    '+': build_plus,
    ',': build_comma,
    '-': build_hyphen,
    '.': build_period,
    '/': build_slash,
    ':': build_colon,
    ';': build_semicolon,
    '<': build_less,
    '=': build_equal,
    '>': build_greater,
    '?': build_question,
    '@': build_at,
    '[': build_bracketleft,
    '\\': build_backslash,
    ']': build_bracketright,
    '^': build_asciicircum,
    '_': build_underscore,
    '`': build_grave,
    '{': build_braceleft,
    '|': build_bar,
    '}': build_braceright,
    '~': build_asciitilde,
}

__all__ = ['BUILDERS', 'build_space', 'build_exclamation', 'build_quotedbl', 'build_numbersign', 'build_dollar', 'build_percent', 'build_ampersand', 'build_quotesingle', 'build_parenleft', 'build_parenright', 'build_asterisk', 'build_plus', 'build_comma', 'build_hyphen', 'build_period', 'build_slash', 'build_colon', 'build_semicolon', 'build_less', 'build_equal', 'build_greater', 'build_question', 'build_at', 'build_bracketleft', 'build_backslash', 'build_bracketright', 'build_asciicircum', 'build_underscore', 'build_grave', 'build_braceleft', 'build_bar', 'build_braceright', 'build_asciitilde']
