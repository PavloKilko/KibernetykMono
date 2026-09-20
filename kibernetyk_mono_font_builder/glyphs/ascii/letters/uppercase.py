"""Procedural builders extracted from the legacy monolithic script."""

from __future__ import annotations

import math

from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition, dot, init_glyph, line, polygon, polyline


def build_A(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    glyph = init_glyph("A", "A")
    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 650 - diagonal_offset),
                (150 + diagonal_offset, 800 - radius),
                (450 - diagonal_offset, 800 - radius),
                (600 - radius, 650 - diagonal_offset),
                (600 - radius, radius),
            ],
        )
    )
    glyph.add(line(width, (radius, 400), (600 - radius, 400)))
    return glyph

# def build_B(width: float) -> GlyphDefinition:
#     radius = width / 2
#     diagonal_offset = (math.sqrt(2) - 1) * radius
#     notch_offset = math.sqrt(2) * radius
#     glyph = init_glyph("B", "B")
#     glyph.add(
#         polyline(
#             width,
#             [
#                 (radius, 400),
#                 (radius, 800 - radius),
#                 (500 - diagonal_offset, 800 - radius),
#                 (600 - radius, 700 - diagonal_offset),
#                 (600 - radius, 500 + diagonal_offset),
#                 (500 - notch_offset, 400),
#                 (600 - radius, 300 - diagonal_offset),
#                 (600 - radius, 100 + diagonal_offset),
#                 (500 - diagonal_offset, radius),
#                 (radius, radius),
#                 (radius, 400),
#             ],
#         )
#     )
#     glyph.add(
#         line(
#             width,
#             (radius, 400),
#             (500 - notch_offset, 400),
#         )
#     )
#     return glyph

def build_B(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("B", "B")
    glyph.add(
        polyline(
            width,
            [
                (radius, 400),
                (radius, 800 - radius),
                (500 - diagonal_offset, 800 - radius),
                (600 - radius, 700 - diagonal_offset),

                # Upper diagonal into the fixed y=400 middle
                (600 - radius, 600 - middle_offset),
                (400 - diagonal_offset, 400),

                # Lower diagonal out of the fixed y=400 middle
                (600 - radius, 200 + middle_offset),

                (600 - radius, 100 + diagonal_offset),
                (500 - diagonal_offset, radius),
                (radius, radius),
                (radius, 400),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (radius, 400),
            (400 - diagonal_offset, 400),
        )
    )

    return glyph

def build_C(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    glyph = init_glyph("C", "C")
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),
                (150 + diagonal_offset, radius),
                (radius, 150 + diagonal_offset),
                (radius, 650 - diagonal_offset),
                (150 + diagonal_offset, 800 - radius),
                (450 - diagonal_offset, 800 - radius),
                (600 - radius, 650 - diagonal_offset),
            ],
        )
    )

    # Alternate C proportions kept for experimentation:
    # glyph = init_glyph("C", "C")
    # glyph.add(
    #     polyline(
    #         width,
    #         [
    #             (600 - radius, 100 + diagonal_offset),
    #             (500 - diagonal_offset, radius),
    #             (100 + diagonal_offset, radius),
    #             (radius, 100 + diagonal_offset),
    #             (radius, 700 - diagonal_offset),
    #             (100 + diagonal_offset, 800 - radius),
    #             (500 - diagonal_offset, 800 - radius),
    #             (600 - radius, 700 - diagonal_offset),
    #         ],
    #     )
    # )
    return glyph


def build_D(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    glyph = init_glyph("D", "D")
    glyph.add(
        polyline(
            width,
            [
                (radius, 400),
                (radius, 800 - radius),
                (450 - diagonal_offset, 800 - radius),
                (600 - radius, 650 - diagonal_offset),
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),
                (radius, radius),
                (radius, 400),
            ],
        )
    )
    return glyph


def build_E(width: float) -> GlyphDefinition:
    radius = width / 2
    glyph = init_glyph("E", "E")
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, radius),
                (radius, radius),
                (radius, 800 - radius),
                (600 - radius, 800 - radius),
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

def build_F(width: float) -> GlyphDefinition:
    radius = width / 2
    glyph = init_glyph("F", "F")
    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 800 - radius),
                (600 - radius, 800 - radius),
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
    
def build_G(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("G", "G")
    glyph.add(
        polyline(
            width,
            [
                (300 + radius, 400),
                (600 - radius, 400),
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),
                (150 + diagonal_offset, radius),
                (radius, 150 + diagonal_offset),
                (radius, 650 - diagonal_offset),
                (150 + diagonal_offset, 800 - radius),
                (450 - diagonal_offset, 800 - radius),
                (600 - radius, 650 - diagonal_offset),
            ],
        )
    )
    return glyph

def build_H(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("H", "H")
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
            (600 - radius, radius),
            (600 - radius, 800 - radius),
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

def build_I(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("I", "I")
    glyph.add(
        line(
            width,
            (radius, radius),
            (600 - radius, radius),
        )
    )
    glyph.add(
        line(
            width,
            (radius, 800 - radius),
            (600 - radius, 800 - radius),
        )
    )
    glyph.add(
        line(
            width,
            (300, 800 - radius),
            (300, radius),
        )
    )
    return glyph
    
def build_J(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("J", "J")
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
    
def build_K(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    notch_offset = math.sqrt(2) * radius

    glyph = init_glyph("K", "K")
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
                (600 - radius, radius),
                (600 - radius, 200 - diagonal_offset),
                (400 - notch_offset, 400),
                (600 - radius, 600 + diagonal_offset),
                (600 - radius, 800 - radius),
            ],
        )
    )
    return glyph

def build_L(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("L", "L")
    glyph.add(
        polyline(
            width,
            [ 
                (600 - radius, radius),
                (radius, radius),
                (radius, 800 - radius),
            ]
        )
    )
    return glyph

def build_M(width: float) -> GlyphDefinition:
    radius = width / 2
    valley_offset = radius / 3
    glyph = init_glyph("M", "M")
    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 800 - radius),
                (300, 400 + valley_offset),
                (600 - radius, 800 - radius),
                (600 - radius, radius),
            ],
        )
    )
    return glyph
    
def build_N(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("N", "N")
    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 800 - radius),
                (600 - radius, radius),
                (600 - radius, 800 - radius),
            ],
        )
    )
    return glyph
    
def build_O(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("O", "O")
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
    return glyph

def build_P(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    notch_offset = math.sqrt(2) * radius

    glyph = init_glyph("P", "P")
    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 800 - radius),
                (500 - diagonal_offset, 800 - radius),
                (600 - radius, 700 - diagonal_offset),
                (600 - radius, 500 + diagonal_offset),
                (500 - notch_offset, 400),
                (radius, 400),
            ],
        )
    )
    return glyph

def build_Q(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("Q", "Q")
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
        polyline(
            width,
            [
                (300, -radius),
                (300, -100 + diagonal_offset),
                (400 - diagonal_offset, -200 + radius),
                (600 - radius, -200 + radius),
            ],
        )
    )
    return glyph

# def build_R(width: float) -> GlyphDefinition:
#     radius = width / 2
#     diagonal_offset = (math.sqrt(2) - 1) * radius
#     notch_offset = math.sqrt(2) * radius

#     glyph = init_glyph("R", "R")
#     glyph.add(
#         polyline(
#             width,
#             [
#                 (radius, radius),
#                 (radius, 800 - radius),
#                 (500 - diagonal_offset, 800 - radius),
#                 (600 - radius, 700 - diagonal_offset),
#                 (600 - radius, 500 + diagonal_offset),
#                 (500 - notch_offset, 400),
#                 (600 - radius, 300 - diagonal_offset),
#                 (600 - radius, radius),
#             ],
#         )
#     )
#     glyph.add(
#         line(
#             width,
#             (radius, 400),
#             (500 - notch_offset, 400),
#         )
#     )
#     return glyph

def build_R(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("R", "R")
    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 800 - radius),

                (500 - diagonal_offset, 800 - radius),
                (600 - radius, 700 - diagonal_offset),

                # Upper diagonal into y = 400
                (600 - radius, 600 - middle_offset),
                (400 - diagonal_offset, 400),

                # Lower diagonal out of y = 400
                (600 - radius, 200 + middle_offset),

                (600 - radius, radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (radius, 400),
            (400 - diagonal_offset, 400),
        )
    )

    return glyph

def build_S(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    # notch_offset = math.sqrt(2) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("S", "S")
    # glyph.add(
    #     polyline(
    #         width,
    #         [
    #             (radius, 150 + diagonal_offset),
    #             (150 + diagonal_offset, radius),
    #             (450 - diagonal_offset, radius),
    #             (600 - radius, 150 + diagonal_offset),
    #             (600 - radius, 300 - diagonal_offset),
    #             (500 - notch_offset, 400),
    #             (100 + notch_offset, 400),
    #             (radius, 500 + diagonal_offset),
    #             (radius, 650 - diagonal_offset),
    #             (150 + diagonal_offset, 800 - radius),
    #             (450 - diagonal_offset, 800 - radius),
    #             (600 - radius, 650 - diagonal_offset),
    #         ],
    #     )
    # )
    # 
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
    return glyph

def build_T(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("T", "T")
    glyph.add(
        line(
            width,
            (radius, 800 - radius),
            (600 - radius, 800 - radius),
        )
    )
    glyph.add(
        line(
            width,
            (300, 800 - radius),
            (300, radius),
        )
    )
    return glyph

def build_U(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("U", "U")
    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (radius, 150 + diagonal_offset),
                (150 + diagonal_offset, radius),
                (450 - diagonal_offset, radius),
                (600 - radius, 150 + diagonal_offset),
                (600 - radius, 800 - radius),
            ],
        )
    )
    return glyph

def build_V(width: float) -> GlyphDefinition:
    radius = width / 2
    # diagonal_offset = radius / 6
    shoulder_offset = radius / 2

    glyph = init_glyph("V", "V")
    # glyph.add(
    #     polyline(
    #         width,
    #         [
    #             (radius, 800 - radius),
    #             (radius, 250 + diagonal_offset),
    #             (300, radius),
    #             (600 - radius, 250 + diagonal_offset),
    #             (600 - radius, 800 - radius),
    #         ],
    #     )
    # )
    glyph.add(
            polyline(
                width,
                [
                    (radius, 800 - radius),
                    (radius, 450 - shoulder_offset),
                    (300, radius),
                    (600 - radius, 450 - shoulder_offset),
                    (600 - radius, 800 - radius),
                ],
            )
        )
    return glyph

def build_W(width: float) -> GlyphDefinition:
    radius = width / 2
    bottom_x_offset = (3 / 5) * radius
    shoulder_y_offset = radius / 3

    glyph = init_glyph("W", "W")
    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (radius, 250 + shoulder_y_offset),
                (150 + bottom_x_offset, radius),
                (300, 250),
                (450 - bottom_x_offset, radius),
                (600 - radius, 250 + shoulder_y_offset),
                (600 - radius, 800 - radius),
            ],
        )
    )
    glyph.add(
        line(
            width,
            (300, 250),
            (300, 500 - radius),
        )
    )
    return glyph

def build_X(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_y_offset = (5 / 6) * radius

    glyph = init_glyph("X", "X")
    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (radius, 650 - diagonal_y_offset),
                (600 - radius, 150 + diagonal_y_offset),
                (600 - radius, radius),
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

def build_Y(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_y_offset = (5 / 6) * radius

    glyph = init_glyph("Y", "Y")
    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (radius, 650 - diagonal_y_offset),
                (300, 400),
                (600 - radius, 650 - diagonal_y_offset),
                (600 - radius, 800 - radius),
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

def build_Z(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("Z", "Z")
    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (600 - radius, 800 - radius),
                (radius, radius),
                (600 - radius, radius),
            ],
        )
    )
    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    'A': build_A,
    'B': build_B,
    'C': build_C,
    'D': build_D,
    'E': build_E,
    'F': build_F,
    'G': build_G,
    'H': build_H,
    'I': build_I,
    'J': build_J,
    'K': build_K,
    'L': build_L,
    'M': build_M,
    'N': build_N,
    'O': build_O,
    'P': build_P,
    'Q': build_Q,
    'R': build_R,
    'S': build_S,
    'T': build_T,
    'U': build_U,
    'V': build_V,
    'W': build_W,
    'X': build_X,
    'Y': build_Y,
    'Z': build_Z,
}

__all__ = ['BUILDERS', 'build_A', 'build_B', 'build_C', 'build_D', 'build_E', 'build_F', 'build_G', 'build_H', 'build_I', 'build_J', 'build_K', 'build_L', 'build_M', 'build_N', 'build_O', 'build_P', 'build_Q', 'build_R', 'build_S', 'build_T', 'build_U', 'build_V', 'build_W', 'build_X', 'build_Y', 'build_Z']
