"""Blank builders for the basic lowercase Cyrillic repertoire."""

from __future__ import annotations

import math

from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition, dot, init_glyph, line, polyline

def build_a_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    
    glyph = init_glyph("acyrillic", "а")

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


def build_be_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("becyrillic", "б")

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
        polyline(
            width,
            [
                (radius, 450 + radius),
                (radius, 700 - diagonal_offset),
                (100 + diagonal_offset, 800 - radius),
                (550 - radius, 800 - radius),
                (600 - radius, 850 - radius),
            ],
        )
    )

    return glyph

def build_ve_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("vecyrillic", "в")

    glyph.add(
        polyline(
            width,
            [
                (radius, 300),
                (radius, 600 - radius),
                (500 - diagonal_offset, 600 - radius),
                (600 - radius, 500 - diagonal_offset),
                (600 - radius, 450 - middle_offset),
                (450 - diagonal_offset, 300),
                (600 - radius, 150 + middle_offset),
                (600 - radius, 100 + diagonal_offset),
                (500 - diagonal_offset, radius),
                (radius, radius),
                (radius, 300),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (radius, 300),
            (450 - diagonal_offset, 300),
        )
    )

    return glyph


def build_ge_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    glyph = init_glyph("gecyrillic", "г")
    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 600 - radius),
                (600 - radius, 600 - radius)
            ]
        )
    )
    return glyph


def build_ghe_upturn_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("gheupturncyrillic", "ґ")

    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 600 - radius),
                (600 - radius, 600 - radius),
                (600 - radius, 750 - radius),
            ],
        )
    )

    return glyph


def build_de_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    # (50, 0) -> (100, 150)
    # Δx:Δy = 50:150 = 1:3
    lower_offset = radius / 3

    # (100, 150) -> (150, 600)
    # Δx:Δy = 50:450 = 1:9
    upper_offset = radius / 9

    glyph = init_glyph("decyrillic", "д")

    glyph.add(
        polyline(
            width,
            [
                (radius, -150 + radius),
                (radius, radius),
                (600 - radius, radius),
                (600 - radius, -150 + radius),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (50 + 50 + lower_offset, radius),
                (100 + 50, 150),
                (150 + 50 - upper_offset, 600 - radius),
                (500 + 50 - radius, 600 - radius),
                (500 + 50 - radius, radius),
            ],
        )
    )

    return glyph


def build_ie_cyrillic(width: float) -> GlyphDefinition:
    glyph = init_glyph("iecyrillic", "е")
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
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


def build_io_cyrillic(width: float) -> GlyphDefinition:
    glyph = init_glyph("iocyrillic", "ё")
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    dot_width = width * 1.25
    dot_radius = dot_width / 2

    
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

    glyph.add(
        dot(
            dot_width,
            (150, 800),
            # (150, 950),   
        )
    )

    glyph.add(
        dot(
            dot_width,
            (450, 800),
            # (450, 950),
        )
    )
    return glyph


def build_zhe_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    # Original diagonals:
    # (0, 600) -> (150, 300) and (150, 300) -> (0, 0)
    # Δx:Δy = 150:300 = 1:2
    #
    # With outer endpoints compensated inward by `radius`,
    # the middle junction must move by `radius / 2`
    # to preserve the original slope.
    middle_offset = radius / 2

    glyph = init_glyph("zhecyrillic", "ж")

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


def build_ze_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("zecyrillic", "з")

    glyph.add(
        polyline(
            width,
            [
                (radius, 500 - diagonal_offset),
                (100 + diagonal_offset, 600 - radius),
                (500 - diagonal_offset, 600 - radius),
                (600 - radius, 500 - diagonal_offset),
                (600 - radius, 450 - middle_offset),
                (450 - diagonal_offset, 300),
                (600 - radius, 150 + middle_offset),
                (600 - radius, 100 + diagonal_offset),
                (500 - diagonal_offset, radius),
                (100 + diagonal_offset, radius),
                (radius, 100 + diagonal_offset),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (200 + radius, 300),
            (450 - diagonal_offset, 300),
        )
    )

    return glyph


def build_ii_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    glyph = init_glyph("iicyrillic", "и")
    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (radius, radius),
                (600 - radius, 600 - radius),
                (600 - radius, radius)
            ]
        )
    )
    return glyph


def build_ii_short_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    accent_width = width * 9 / 10
    glyph = init_glyph("iishortcyrillic", "й")
    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (radius, radius),
                (600 - radius, 600 - radius),
                (600 - radius, radius)
            ]
        )
    )

    glyph.add(
        polyline(
            accent_width,
            [
                (150, 800),
                (250, 700),
                (350, 700),
                (450, 800),
            ],
        )
    )
    return glyph


def build_ka_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    notch_offset = math.sqrt(2) * radius

    glyph = init_glyph("kacyrillic", "к")
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


def build_el_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    upper_diagonal_offset = radius / 9

    glyph = init_glyph("elcyrillic", "л")

    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (150, 150),
                (200 - upper_diagonal_offset, 600 - radius),
                (600 - radius, 600 - radius),
                (600 - radius, radius),
            ],
        )
    )

    return glyph


def build_em_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    # Preserve the original 300:400 = 3:4 diagonal slope.
    valley_offset = radius / 3

    glyph = init_glyph("emcyrillic", "м")

    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 600 - radius),
                (300, 200 + valley_offset),
                (600 - radius, 600 - radius),
                (600 - radius, radius),
            ],
        )
    )

    return glyph


def build_en_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    glyph = init_glyph("encyrillic", "н")
    glyph.add(
        line(
            width,
            (radius, radius),
            (radius, 600 - radius)
        )
    )
    glyph.add(
        line(
            width,
            (600 - radius, radius),
            (600 - radius, 600 - radius)
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


def build_o_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("ocyrillic", "о")
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


def build_pe_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    glyph = init_glyph("pecyrillic", "п")
    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 600 - radius),
                (600 - radius, 600 - radius),
                (600 - radius, radius)
            ]
        )
    )
    return glyph


def build_er_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("ercyrillic", "р")
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


def build_es_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("escyrillic", "с")
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


def build_te_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    glyph = init_glyph("tecyrillic", "т")
    glyph.add(
        line(
            width,
            (radius, 600 - radius),
            (600 - radius, 600 - radius)
        )
    )
    glyph.add(
        line(
            width,
            (300, 600 - radius),
            (300, radius)
        )
    )
    return glyph


def build_u_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("ucyrillic", "у")
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


def build_u_short_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    accent_width = width * 9 / 10
    glyph = init_glyph("ushortcyrillic", "ў")
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
    glyph.add(
        polyline(
            accent_width,
            [
                (150, 800),
                (250, 700),
                (350, 700),
                (450, 800),
            ],
        )
    )
    return glyph


def build_ef_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    glyph = init_glyph("efcyrillic", "ф")
    glyph.add(
        polyline(
            width,
            [
                (radius, 300),
                (radius, 500 - diagonal_offset),
                (100 + diagonal_offset, 600 - radius),
                (500 - diagonal_offset, 600 - radius),
                (600 - radius, 500 - diagonal_offset),
                (600 - radius, 100 + diagonal_offset),
                (500 - diagonal_offset, radius),
                (100 + diagonal_offset, radius),
                (radius, 100 + diagonal_offset),
                (radius, 300),
            ],
        )
    )
    glyph.add(
        line(
            width,
            (300, 800 - radius),
            (300, -200 + radius)
        )
    )
    return glyph


def build_kha_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_y_offset = (5 / 6) * radius

    glyph = init_glyph("khacyrillic", "х")
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


def build_che_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("checyrillic", "ч")

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
        line(
            width,
            (600 - radius, 600 - radius),
            (600 - radius, radius),
        )
    )

    return glyph


def build_tse_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    glyph = init_glyph("tsecyrillic", "ц")
    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (radius, radius),
                (600 - radius, radius),
                (600 - radius, -150 + radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (550 - radius, 600 - radius),
            (550 - radius, radius),
        )
    )

    return glyph


def build_sha_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("shacyrillic", "ш")

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
            (300, 600 - radius),
            (300, radius),
        )
    )

    return glyph


def build_shcha_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    glyph = init_glyph("shchacyrillic", "щ")

    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (radius, radius),
                (600 - radius, radius),
                (600 - radius, -150 + radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (550 - radius, 600 - radius),
            (550 - radius, radius),
        )
    )

    glyph.add(
        line(
            width,
            (275, 600 - radius),
            (275, radius),
        )
    )

    return glyph


def build_soft_sign_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("softsigncyrillic", "ь")
    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (radius, radius),
                (500 - diagonal_offset, radius),
                (600 - radius, 100 + diagonal_offset),
                (600 - radius, 250 + middle_offset),
                (500 - diagonal_offset, 350),
                (radius, 350),
            ],
        )
    )
    return glyph


def build_yeri_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("yericyrillic", "ы")

    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (radius, radius),

                # Lower 45° corner
                (300 - diagonal_offset, radius),
                (400 - radius, 100 + diagonal_offset),

                # Right side of bowl
                (400 - radius, 250 + middle_offset),

                # Upper 45° corner into y = 350
                (300 - diagonal_offset, 350),

                (radius, 350),
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


def build_hard_sign_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("hardsigncyrillic", "ъ")

    glyph.add(
        polyline(
            width,
            [
                (radius, 600 - radius),
                (200, 600 - radius),
                (200, radius),

                # Lower 45° corner
                (500 - diagonal_offset, radius),
                (600 - radius, 100 + diagonal_offset),

                # Right side of bowl
                (600 - radius, 250 + middle_offset),

                # Upper 45° corner into y = 350
                (500 - diagonal_offset, 350),

                # Open terminal aligned to x = 200
                (200 + radius, 350),
            ],
        )
    )

    return glyph


def build_ukrainian_ie_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("ecyrillic", "є")
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
                (600 - radius, 100 + diagonal_offset),
                (500 - diagonal_offset, radius),
                (100 + diagonal_offset, radius),
                (radius, 100 + diagonal_offset),
                (radius, 500 - diagonal_offset),
                (100 + diagonal_offset, 600 - radius),
                (500 - diagonal_offset, 600 - radius),
                (600 - radius, 500 - diagonal_offset),
            ],
        )
    )
    return glyph


def build_e_reversed_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    glyph = init_glyph("ereversedcyrillic", "э")
    glyph.add(
        line(
            width,
            (200 + radius, 300),
            (600 - radius, 300),
        )
    )
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
            ],
        )
    )
    return glyph


def build_byelorussian_ukrainian_i_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("icyrillic", "і")
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
    


def build_yi_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    dot_width = width * 1.25
    glyph = init_glyph("yicyrillic", "ї")
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
            dot_width,
            (150, 800),
            # (150, 950),   
        )
    )

    glyph.add(
        dot(
            dot_width,
            (450, 800),
            # (450, 950),
        )
    )
    return glyph


def build_yu_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("iucyrillic", "ю")

    glyph.add(
        line(
            width,
            (radius, 600 - radius),
            (radius, radius),
        )
    )

    glyph.add(
        line(
            width,
            (radius, 300),
            (200 + radius, 300),
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (200 + radius, 300),
                (200 + radius, 500 - diagonal_offset),
                (300 + diagonal_offset, 600 - radius),
                (500 - diagonal_offset, 600 - radius),
                (600 - radius, 500 - diagonal_offset),
                (600 - radius, 100 + diagonal_offset),
                (500 - diagonal_offset, radius),
                (300 + diagonal_offset, radius),
                (200 + radius, 100 + diagonal_offset),
                (200 + radius, 300),
            ],
        )
    )

    return glyph


def build_ya_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("iacyrillic", "я")

    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 100 + diagonal_offset),
                (150 + diagonal_offset, 250),
                (radius, 400 - middle_offset),
                (radius, 500 - diagonal_offset),
                (100 + diagonal_offset, 600 - radius),
                (600 - radius, 600 - radius),
                (600 - radius, radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (150 + diagonal_offset, 250),
            (600 - radius, 250),
        )
    )

    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    "а": build_a_cyrillic,
    "б": build_be_cyrillic,
    "в": build_ve_cyrillic,
    "г": build_ge_cyrillic,
    "ґ": build_ghe_upturn_cyrillic,
    "д": build_de_cyrillic,
    "е": build_ie_cyrillic,
    "ё": build_io_cyrillic,
    "ж": build_zhe_cyrillic,
    "з": build_ze_cyrillic,
    "и": build_ii_cyrillic,
    "й": build_ii_short_cyrillic,
    "к": build_ka_cyrillic,
    "л": build_el_cyrillic,
    "м": build_em_cyrillic,
    "н": build_en_cyrillic,
    "о": build_o_cyrillic,
    "п": build_pe_cyrillic,
    "р": build_er_cyrillic,
    "с": build_es_cyrillic,
    "т": build_te_cyrillic,
    "у": build_u_cyrillic,
    "ў": build_u_short_cyrillic,
    "ф": build_ef_cyrillic,
    "х": build_kha_cyrillic,
    "ч": build_che_cyrillic,
    "ц": build_tse_cyrillic,
    "ш": build_sha_cyrillic,
    "щ": build_shcha_cyrillic,
    "ь": build_soft_sign_cyrillic,
    "ы": build_yeri_cyrillic,
    "ъ": build_hard_sign_cyrillic,
    "є": build_ukrainian_ie_cyrillic,
    "э": build_e_reversed_cyrillic,
    "і": build_byelorussian_ukrainian_i_cyrillic,
    "ї": build_yi_cyrillic,
    "ю": build_yu_cyrillic,
    "я": build_ya_cyrillic,
}


__all__ = [
    "BUILDERS",
    "build_a_cyrillic",
    "build_be_cyrillic",
    "build_byelorussian_ukrainian_i_cyrillic",
    "build_che_cyrillic",
    "build_de_cyrillic",
    "build_e_reversed_cyrillic",
    "build_ef_cyrillic",
    "build_el_cyrillic",
    "build_em_cyrillic",
    "build_en_cyrillic",
    "build_er_cyrillic",
    "build_es_cyrillic",
    "build_ge_cyrillic",
    "build_ghe_upturn_cyrillic",
    "build_hard_sign_cyrillic",
    "build_ie_cyrillic",
    "build_ii_cyrillic",
    "build_ii_short_cyrillic",
    "build_io_cyrillic",
    "build_ka_cyrillic",
    "build_kha_cyrillic",
    "build_o_cyrillic",
    "build_pe_cyrillic",
    "build_sha_cyrillic",
    "build_shcha_cyrillic",
    "build_soft_sign_cyrillic",
    "build_te_cyrillic",
    "build_tse_cyrillic",
    "build_u_cyrillic",
    "build_u_short_cyrillic",
    "build_ukrainian_ie_cyrillic",
    "build_ve_cyrillic",
    "build_ya_cyrillic",
    "build_yeri_cyrillic",
    "build_yi_cyrillic",
    "build_yu_cyrillic",
    "build_ze_cyrillic",
    "build_zhe_cyrillic",
]
