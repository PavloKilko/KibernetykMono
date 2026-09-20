"""Blank builders for the basic uppercase Cyrillic repertoire."""

from __future__ import annotations

import math

from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition, dot, init_glyph, line, polyline

def build_A_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    
    glyph = init_glyph("Acyrillic", "А")
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

def build_Be_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("Becyrillic", "Б")
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 800 - radius),
                (radius, 800 - radius),
                (radius, radius),
                (500 - diagonal_offset, radius),
                (600 - radius, 100 + diagonal_offset),
                (600 - radius, 250 + middle_offset),
                (450 - diagonal_offset, 400),
                (radius, 400),
            ],
        )
    )
    return glyph


def build_Ve_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("Vecyrillic", "В")
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


def build_Ge_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("Gecyrillic", "Г")
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
    return glyph


def build_Ghe_upturn_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("Gheupturncyrillic", "Ґ")
    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 800 - radius),
                (600 - radius, 800 - radius),
                (600 - radius, 950 - radius),
            ],
        )
    )
    return glyph


def build_De_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("Decyrillic", "Д")

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
                (50 + radius / 2, radius),
                (100, 100),
                (150, 800 - radius),
                (550 - radius, 800 - radius),
                (550 - radius, radius),
            ],
        )
    )

    return glyph


def build_Ie_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    glyph = init_glyph("Iecyrillic", "Е")
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


def build_Io_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    dot_width = width * 1.25
    dot_radius = dot_width / 2

    glyph = init_glyph("Iocyrillic", "Ё")

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

    glyph.add(
        dot(
            dot_width,
            (150, 1000),
            # (150, 950),   
        )
    )

    glyph.add(
        dot(
            dot_width,
            (450, 1000),
            # (450, 950),
        )
    )

    return glyph


def build_Zhe_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    middle_offset = (5 / 8) * radius

    glyph = init_glyph("Zhecyrillic", "Ж")

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


def build_Ze_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("Zecyrillic", "З")

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
                (600 - radius, 550 - middle_offset),
                (600 - radius, 650 - diagonal_offset),
                (450 - diagonal_offset, 800 - radius),
                (150 + diagonal_offset, 800 - radius),
                (radius, 650 - diagonal_offset),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (200 + radius, 400),
            (450 - diagonal_offset, 400),
        )
    )

    return glyph


def build_Ii_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    glyph = init_glyph("Iicyrillic", "И")
    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (radius, radius),
                (600 - radius, 800 - radius),
                (600 - radius, radius)
            ]
        )
    )
    return glyph


def build_Ii_short_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    accent_width = width * 0.9

    glyph = init_glyph("Iishortcyrillic", "Й")

    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (radius, radius),
                (600 - radius, 800 - radius),
                (600 - radius, radius),
            ],
        )
    )

    glyph.add(
        polyline(
            accent_width,
            [
                (150, 1000),
                (250, 900),
                (350, 900),
                (450, 1000),
            ],
        )
    )

    return glyph

def build_Ka_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    notch_offset = math.sqrt(2) * radius

    glyph = init_glyph("Kacyrillic", "К")
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


def build_El_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    # Preserve the original 50:650 = 1:13 slope
    # of the long diagonal after the top is lowered by radius.
    top_x_offset = radius / 13

    glyph = init_glyph("Elcyrillic", "Л")
    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (150, 150),
                (200 - top_x_offset, 800 - radius),
                (600 - radius, 800 - radius),
                (600 - radius, radius),
            ],
        )
    )
    return glyph


def build_Em_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    valley_offset = radius / 3
    glyph = init_glyph("Emcyrillic", "М")
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


def build_En_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("Encyrillic", "Н")
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


def build_O_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("Ocyrillic", "О")
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


def build_Pe_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    glyph = init_glyph("Pecyrillic", "П")
    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 800 - radius),
                (600 - radius, 800 - radius),
                (600 - radius, radius)
            ]
        )
    )
    return glyph


def build_Er_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    notch_offset = math.sqrt(2) * radius

    glyph = init_glyph("Ercyrillic", "Р")
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


def build_Es_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    glyph = init_glyph("Escyrillic", "С")
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
    return glyph


def build_Te_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("Tecyrillic", "Т")
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


def build_U_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("Ucyrillic", "У")

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
                (600 - radius, 100 + diagonal_offset),
                (500 - diagonal_offset, radius),
                (100 + diagonal_offset, radius),
                (radius, 100 + diagonal_offset),
            ],
        )
    )

    return glyph

def build_U_short_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset
    # diagonal_endpoint_offset = radius / math.sqrt(2)
    endpoint_offset = radius / math.sqrt(2)
    accent_width = width * 9 / 10

    glyph = init_glyph("Ushortcyrillic", "Ў")

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
                (600 - radius, 100 + diagonal_offset),
                (500 - diagonal_offset, radius),
                (100 + diagonal_offset, radius),
                (radius, 100 + diagonal_offset),
            ],
        )
    )

    glyph.add(
        polyline(
            accent_width,
            [
                (150, 1000),
                (250, 900),
                (350, 900),
                (450, 1000),
            ],
        )
    )
    
    return glyph

def build_Ef_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("Efcyrillic", "Ф")

    glyph.add(
        polyline(
            width,
            [
                (300, 200),
                (100 + diagonal_offset, 200),
                (radius, 300 - middle_offset),
                (radius, 700 - diagonal_offset),
                (100 + diagonal_offset, 800 - radius),
                (500 - diagonal_offset, 800 - radius),
                (600 - radius, 700 - diagonal_offset),
                (600 - radius, 300 - middle_offset),
                (500 - diagonal_offset, 200),
                (300, 200),
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

    return glyph

def build_Kha_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_y_offset = (5 / 6) * radius

    glyph = init_glyph("Khacyrillic", "Х")
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


def build_Che_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("Checyrillic", "Ч")

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
        line(
            width,
            (600 - radius, 800 - radius),
            (600 - radius, radius),
        )
    )

    return glyph


def build_Tse_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("Tsecyrillic", "Ц")

    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (radius, radius),
                (600 - radius, radius),
                (600 - radius, -150 + radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (550 - radius, 800 - radius),
            (550 - radius, radius),
        )
    )

    return glyph


def build_Sha_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("Shacyrillic", "Ш")

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
            (300, 800 - radius),
            (300, radius),
        )
    )

    return glyph


def build_Shcha_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("Shchacyrillic", "Щ")

    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (radius, radius),
                (600 - radius, radius),
                (600 - radius, -150 + radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (275, 800 - radius),
            (275, radius),
        )
    )

    glyph.add(
        line(
            width,
            (550 - radius, 800 - radius),
            (550 - radius, radius),
        )
    )

    return glyph


def build_Soft_sign_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("Softsigncyrillic", "Ь")
    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (radius, radius),
                (500 - diagonal_offset, radius),
                (600 - radius, 100 + diagonal_offset),
                (600 - radius, 250 + middle_offset),
                (450 - diagonal_offset, 400),
                (radius, 400),
            ],
        )
    )
    return glyph


def build_Yeri_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("Yericyrillic", "Ы")

    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (radius, radius),

                # Lower 45° corner
                (300 - diagonal_offset, radius),
                (400 - radius, 100 + diagonal_offset),

                # Right side of bowl
                (400 - radius, 250 + middle_offset),

                # Upper 45° diagonal into y=400
                (250 - diagonal_offset, 400),

                (radius, 400),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (600 - radius, 800 - radius),
            (600 - radius, radius),
        )
    )

    return glyph


def build_Hard_sign_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("Hardsigncyrillic", "Ъ")
    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (200, 800 - radius),
                (200, radius),
                (500 - diagonal_offset, radius),
                (600 - radius, 100 + diagonal_offset),
                (600 - radius, 250 + middle_offset),
                (450 - diagonal_offset, 400),
                (200 + radius, 400),
            ],
        )
    )
    return glyph


def build_Ukrainian_Ie_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("Ecyrillic", "Є")

    glyph.add(
        polyline(
            width,
            [
                (600 - radius, 650 - diagonal_offset),
                (450 - diagonal_offset, 800 - radius),
                (150 + diagonal_offset, 800 - radius),
                (radius, 650 - diagonal_offset),
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
            (radius, 400),
            (400 - radius, 400),
        )
    )

    return glyph


def build_E_reversed_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("Ereversedcyrillic", "Э")

    glyph.add(
        polyline(
            width,
            [
                (radius, 150 + diagonal_offset),
                (150 + diagonal_offset, radius),
                (450 - diagonal_offset, radius),
                (600 - radius, 150 + diagonal_offset),
                (600 - radius, 650 - diagonal_offset),
                (450 - diagonal_offset, 800 - radius),
                (150 + diagonal_offset, 800 - radius),
                (radius, 650 - diagonal_offset),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (600 - radius, 400),
            (200 + radius, 400),
        )
    )

    return glyph


def build_Byelorussian_Ukrainian_I_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    glyph = init_glyph("Icyrillic", "І")
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


def build_Yi_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    dot_width = width * 1.25
    dot_radius = dot_width / 2
    glyph = init_glyph("Yicyrillic", "Ї")
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

    glyph.add(
        dot(
            dot_width,
            (150, 1000),
            # (150, 950),   
        )
    )

    glyph.add(
        dot(
            dot_width,
            (450, 1000),
            # (450, 950),
        )
    )
    
    return glyph


def build_Yu_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("IUcyrillic", "Ю")

    glyph.add(
        polyline(
            width,
            [
                (200 + radius, 300),
                (200 + radius, 700 - diagonal_offset),
                (300 + diagonal_offset, 800 - radius),
                (500 - diagonal_offset, 800 - radius),
                (600 - radius, 700 - diagonal_offset),
                (600 - radius, 100 + diagonal_offset),
                (500 - diagonal_offset, radius),
                (300 + diagonal_offset, radius),
                (200 + radius, 100 + diagonal_offset),
                (200 + radius, 300),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (radius, 800 - radius),
            (radius, radius),
        )
    )

    glyph.add(
        line(
            width,
            (radius, 400),
            (200 + radius, 400),
        )
    )

    return glyph


def build_Ya_cyrillic(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    glyph = init_glyph("IAcyrillic", "Я")

    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 200 + middle_offset),
                (200 + diagonal_offset, 400),
                (radius, 600 - middle_offset),
                (radius, 700 - diagonal_offset),
                (100 + diagonal_offset, 800 - radius),
                (600 - radius, 800 - radius),
                (600 - radius, radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (
                200 + radius,
                400,
            ),
            (
                600 - radius,
                400,
            ),
        )
    )

    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    "А": build_A_cyrillic,
    "Б": build_Be_cyrillic,
    "В": build_Ve_cyrillic,
    "Г": build_Ge_cyrillic,
    "Ґ": build_Ghe_upturn_cyrillic,
    "Д": build_De_cyrillic,
    "Е": build_Ie_cyrillic,
    "Ё": build_Io_cyrillic,
    "Ж": build_Zhe_cyrillic,
    "З": build_Ze_cyrillic,
    "И": build_Ii_cyrillic,
    "Й": build_Ii_short_cyrillic,
    "К": build_Ka_cyrillic,
    "Л": build_El_cyrillic,
    "М": build_Em_cyrillic,
    "Н": build_En_cyrillic,
    "О": build_O_cyrillic,
    "П": build_Pe_cyrillic,
    "Р": build_Er_cyrillic,
    "С": build_Es_cyrillic,
    "Т": build_Te_cyrillic,
    "У": build_U_cyrillic,
    "Ў": build_U_short_cyrillic,
    "Ф": build_Ef_cyrillic,
    "Х": build_Kha_cyrillic,
    "Ч": build_Che_cyrillic,
    "Ц": build_Tse_cyrillic,
    "Ш": build_Sha_cyrillic,
    "Щ": build_Shcha_cyrillic,
    "Ь": build_Soft_sign_cyrillic,
    "Ы": build_Yeri_cyrillic,
    "Ъ": build_Hard_sign_cyrillic,
    "Є": build_Ukrainian_Ie_cyrillic,
    "Э": build_E_reversed_cyrillic,
    "І": build_Byelorussian_Ukrainian_I_cyrillic,
    "Ї": build_Yi_cyrillic,
    "Ю": build_Yu_cyrillic,
    "Я": build_Ya_cyrillic,
}


__all__ = [
    "BUILDERS",
    "build_A_cyrillic",
    "build_Be_cyrillic",
    "build_Byelorussian_Ukrainian_I_cyrillic",
    "build_Che_cyrillic",
    "build_De_cyrillic",
    "build_E_reversed_cyrillic",
    "build_Ef_cyrillic",
    "build_El_cyrillic",
    "build_Em_cyrillic",
    "build_En_cyrillic",
    "build_Er_cyrillic",
    "build_Es_cyrillic",
    "build_Ge_cyrillic",
    "build_Ghe_upturn_cyrillic",
    "build_Hard_sign_cyrillic",
    "build_Ie_cyrillic",
    "build_Ii_cyrillic",
    "build_Ii_short_cyrillic",
    "build_Io_cyrillic",
    "build_Ka_cyrillic",
    "build_Kha_cyrillic",
    "build_O_cyrillic",
    "build_Pe_cyrillic",
    "build_Sha_cyrillic",
    "build_Shcha_cyrillic",
    "build_Soft_sign_cyrillic",
    "build_Te_cyrillic",
    "build_Tse_cyrillic",
    "build_U_cyrillic",
    "build_U_short_cyrillic",
    "build_Ukrainian_Ie_cyrillic",
    "build_Ve_cyrillic",
    "build_Ya_cyrillic",
    "build_Yeri_cyrillic",
    "build_Yi_cyrillic",
    "build_Yu_cyrillic",
    "build_Ze_cyrillic",
    "build_Zhe_cyrillic",
]
