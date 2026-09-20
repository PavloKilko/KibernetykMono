"""Procedural builders extracted from the legacy monolithic script."""

from __future__ import annotations

import math

from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition, dot, init_glyph, line, polyline


def build_a(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("a", "a")
    glyph.add(
        polyline(
            width,
            [
                (radius, 500 - diagonal_offset),
                (100 + diagonal_offset, 600 - radius),
                (500 - diagonal_offset, 600 - radius),
                (600 - radius, 500 - diagonal_offset),
                (600 - radius, radius),
            ],
        )
    )
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),
                (100 + diagonal_offset, radius),
                (radius, 100 + diagonal_offset),
                (radius, 200 + radius - diagonal_offset),
                (100 + diagonal_offset, 300),
                (600 - radius, 300),
            ],
        )
    )
    return glyph

def build_b(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("b", "b")
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
                (radius, 450 - diagonal_offset),
                (150 + diagonal_offset, 600 - radius),
                (450 - diagonal_offset, 600 - radius),
                (600 - radius, 450 - diagonal_offset),
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),
                (150 + diagonal_offset, radius),
                (radius, 150 + diagonal_offset),
            ],
        )
    )
    return glyph

def build_c(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("c", "c")
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),
                (150 + diagonal_offset, radius),
                (radius, 150 + diagonal_offset),
                (radius, 450 - diagonal_offset),
                (150 + diagonal_offset, 600 - radius),
                (450 - diagonal_offset, 600 - radius),
                (600 - radius, 450 - diagonal_offset),
            ],
        )
    )
    return glyph

def build_d(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("d", "d")
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),
                (150 + diagonal_offset, radius),
                (radius, 150 + diagonal_offset),
                (radius, 450 - diagonal_offset),
                (150 + diagonal_offset, 600 - radius),
                (450 - diagonal_offset, 600 - radius),
                (600 - radius, 450 - diagonal_offset),
            ],
        )
    )
    glyph.add(
        line(
            width,
            (600 - radius, radius),
            (600 - radius, 800 - radius)
        )
    )
    return glyph

def build_e(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("e", "e")
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 100 + diagonal_offset),
                (500 - diagonal_offset, radius),
                (100 + diagonal_offset, radius),
                (radius, 100 + diagonal_offset),
                (radius, 500 - diagonal_offset),
                (100 + diagonal_offset, 600 - radius),
                (500 - diagonal_offset, 600 - radius),
                (600 - radius, 500 - diagonal_offset),
                (600 - radius, 300),
                (radius, 300),
            ],
        )
    )
    return glyph

def build_f(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("f", "f")
    glyph.add(
        line(
            width,
            (radius, radius),
            (500, radius),
        )
    )
    glyph.add(
        polyline(
            width,
            [
                (200, radius),
                (200, 700 - radius),
                (300, 800 - radius),
                (600 - radius, 800 - radius),
            ],
        )
    )
    glyph.add(
        line(
            width,
            (radius, 600 - radius),
            (600 - radius, 600 - radius),
        )
    )
    return glyph

def build_g(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("g", "g")
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),
                (150 + diagonal_offset, radius),
                (radius, 150 + diagonal_offset),
                (radius, 450 - diagonal_offset),
                (150 + diagonal_offset, 600 - radius),
                (450 - diagonal_offset, 600 - radius),
                (600 - radius, 450 - diagonal_offset),
            ],
        )
    )
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 600 - radius),
                (600 - radius, -100 + diagonal_offset),
                (500 - diagonal_offset, -200 + radius),
                # (100 + diagonal_offset, -200 + radius),
                # (radius, -100 + diagonal_offset),
                 
                # (radius, -200 + radius),
                
                (50 + radius, -200 + radius),
            ],
        )
    )
    return glyph

def build_h(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("h", "h")
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
                (radius, 450 - diagonal_offset),
                (150 + diagonal_offset, 600 - radius),
                (450 - diagonal_offset, 600 - radius),
                (600 - radius, 450 - diagonal_offset),
                (600 - radius, radius),
            ],
        )
    )
    return glyph

def build_i(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    junction_offset = radius - diagonal_offset

    glyph = init_glyph("i", "i")
    glyph.add(
        line(
            width,
            (radius, radius),
            (600 - radius, radius),
        )
    )
    glyph.add(
        polyline(
            width,
            [
                (300, radius),
                (300, 600 - radius),
                # (300, 450 - junction_offset),
                # (150 + diagonal_offset, 600 - radius),
                (radius, 600 - radius),
            ],
        )
    )
    glyph.add(
        dot(
            width * 1.25,
            (300, 800),
        )
    )
    return glyph

def build_j(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("j", "j")
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

def build_k(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    notch_offset = math.sqrt(2) * radius

    glyph = init_glyph("k", "k")
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
                (600 - radius, 600 - radius),
                (600 - radius, 500 + diagonal_offset),
                (400 - notch_offset, 300),
                (600 - radius, 100 - diagonal_offset),
                (600 - radius, radius),
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

def build_l(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("l", "l")
    glyph.add(
        line(
            width,
            (radius, radius),
            (600 - radius, radius),
        )
    )
    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (300, 800 - radius),
                # (150, 800 - radius),
                # (300, 650 - radius),
                (300, radius),
            ],
        )
    )
    return glyph

def build_m(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("m", "m")

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
                (radius, 450 - diagonal_offset),
                (150 + diagonal_offset, 600 - radius),
                (200, 600 - radius),
                (300, 500 - radius),
                (400, 600 - radius),
                (500 - diagonal_offset, 600 - radius),
                (600 - radius, 500 - diagonal_offset),
                (600 - radius, radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (300, 500 - radius),
            (300, radius),
        )
    )

    return glyph

def build_n(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("n", "n")
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
                (radius, 450 - diagonal_offset),
                (150 + diagonal_offset, 600 - radius),
                (450 - diagonal_offset, 600 - radius),
                (600 - radius, 450 - diagonal_offset),
                (600 - radius, radius),
            ],
        )
    )
    return glyph

def build_o(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("o", "o")
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
    return glyph

def build_p(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("p", "p")
    glyph.add(
        line(
            width,
            (radius, 600 - radius),
            (radius, -200 + radius),
        )
    )
    glyph.add(
        polyline(
            width,
            [
                (radius, 450 - diagonal_offset),
                (150 + diagonal_offset, 600 - radius),
                (450 - diagonal_offset, 600 - radius),
                (600 - radius, 450 - diagonal_offset),
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),
                (150 + diagonal_offset, radius),
                (radius, 150 + diagonal_offset),
            ],
        )
    )
    return glyph

def build_q(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("q", "q")
    glyph.add(
        line(
            width,
            (600 - radius, 600 - radius),
            (600 - radius, -200 + radius),
        )
    )
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 150 + diagonal_offset),
                (450 - diagonal_offset, radius),
                (150 + diagonal_offset, radius),
                (radius, 150 + diagonal_offset),
                (radius, 450 - diagonal_offset),
                (150 + diagonal_offset, 600 - radius),
                (450 - diagonal_offset, 600 - radius),
                (600 - radius, 450 - diagonal_offset),
            ],
        )
    )
    return glyph

def build_r(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("r", "r")
    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (100, 600 - radius),
                (200, 500 - radius),
                (300, 600 - radius),
                (600 - radius, 600 - radius),
            ],
        )
    )
    glyph.add(
        line(
            width,
            (200, 500 - radius),
            (200, radius),
        )
    )
    glyph.add(
        line(
            width,
            (radius, radius),
            (500 - radius, radius),
        )
    )
    return glyph

def build_s(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("s", "s")
    glyph.add(
        polyline(
            width,
            [
                (radius, 100 + diagonal_offset),
                (100 + diagonal_offset, radius),
                (500 - diagonal_offset, radius),
                (600 - radius, 100 + diagonal_offset),

                # Middle-right diagonal
                (600 - radius, 200 + radius - diagonal_offset),
                (500 - diagonal_offset, 300),

                # Middle horizontal
                (100 + diagonal_offset, 300),

                # Middle-left diagonal
                (radius, 400 - radius + diagonal_offset),

                (radius, 500 - diagonal_offset),
                (100 + diagonal_offset, 600 - radius),
                (500 - diagonal_offset, 600 - radius),
                (600 - radius, 500 - diagonal_offset),
            ],
        )
    )
    return glyph

def build_t(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("t", "t")
    glyph.add(
        polyline(
            width,
            [
                (200, 800 - radius),
                (200, 100 + radius),
                (300, radius),
                (600 - radius, radius),
            ],
        )
    )
    glyph.add(
        line(
            width,
            (radius, 600 - radius),
            (600 - radius, 600 - radius),
        )
    )
    return glyph

def build_u(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("u", "u")
    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
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
            (600 - radius, 600 - radius),
            (600 - radius, radius),
        )
    )
    return glyph

def build_v(width: float) -> GlyphDefinition:
    radius = width / 2
    # diagonal_offset = radius / 6
    shoulder_offset = radius / 2

    glyph = init_glyph("v", "v")
    # glyph.add(
    #     polyline(
    #         width,
    #         [
    #             (radius, 600 - radius),
    #             (radius, 250 + diagonal_offset),
    #             (300, radius),
    #             (600 - radius, 250 + diagonal_offset),
    #             (600 - radius, 600 - radius),
    #         ],
    #     )
    # )
    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (radius, 450 - shoulder_offset),
                (300, radius),
                (600 - radius, 450 - shoulder_offset),
                (600 - radius, 600 - radius),
            ],
        )
    )

    return glyph

def build_w(width: float) -> GlyphDefinition:
    radius = width / 2
    bottom_x_offset = (3 / 5) * radius
    shoulder_y_offset = radius / 3

    glyph = init_glyph("w", "w")
    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (radius, 250 + shoulder_y_offset),
                (150 + bottom_x_offset, radius),
                (300, 250),
                (450 - bottom_x_offset, radius),
                (600 - radius, 250 + shoulder_y_offset),
                (600 - radius, 600 - radius),
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

def build_x(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_y_offset = (5 / 6) * radius

    glyph = init_glyph("x", "x")
    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (radius, 550 - diagonal_y_offset),
                (600 - radius, 50 + diagonal_y_offset),
                (600 - radius, radius),
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

def build_y(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("y", "y")
    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (radius, 150 + diagonal_offset),
                (150 + diagonal_offset, radius),
                (450 - diagonal_offset, radius),
                (600 - radius, 150 + diagonal_offset),
            ],
        )
    )
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 600 - radius),
                (600 - radius, -100 + diagonal_offset),
                (500 - diagonal_offset, -200 + radius),
                # (100 + diagonal_offset, -200 + radius),
                # (radius, -100 + diagonal_offset),
                
                # (radius, -200 + radius),

                (50 + radius, -200 + radius),
            ],
        )
    )
    return glyph

def build_z(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("z", "z")
    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (600 - radius, 600 - radius),
                (radius, radius),
                (600 - radius, radius),
            ],
        )
    )
    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    'a': build_a,
    'b': build_b,
    'c': build_c,
    'd': build_d,
    'e': build_e,
    'f': build_f,
    'g': build_g,
    'h': build_h,
    'i': build_i,
    'j': build_j,
    'k': build_k,
    'l': build_l,
    'm': build_m,
    'n': build_n,
    'o': build_o,
    'p': build_p,
    'q': build_q,
    'r': build_r,
    's': build_s,
    't': build_t,
    'u': build_u,
    'v': build_v,
    'w': build_w,
    'x': build_x,
    'y': build_y,
    'z': build_z,
}

__all__ = ['BUILDERS', 'build_a', 'build_b', 'build_c', 'build_d', 'build_e', 'build_f', 'build_g', 'build_h', 'build_i', 'build_j', 'build_k', 'build_l', 'build_m', 'build_n', 'build_o', 'build_p', 'build_q', 'build_r', 'build_s', 'build_t', 'build_u', 'build_v', 'build_w', 'build_x', 'build_y', 'build_z']
