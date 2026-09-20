"""Blank builders for lowercase Latin Core additions."""

from __future__ import annotations

import math

from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition, dot, init_glyph, line, polygon, polyline
from kibernetyk_mono_font_builder.core.config import COMMA_ACCENT_SCALE, COMMA_CARON_TOP
from kibernetyk_mono_font_builder.glyphs.ascii.letters.lowercase import build_d, build_e, build_g, build_k, build_l, build_n, build_t


def build_germandbls(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("germandbls", 0x00DF)

    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 700 - diagonal_offset),
                (100 + diagonal_offset, 800 - radius),
                (350 - diagonal_offset, 800 - radius),
                (450 - radius, 700 - diagonal_offset),

                # Keep this join optically stable
                (450 - radius, 550 - radius),
                (300, 400),
                (450, 400),

                # Keep this join optically stable
                (600 - radius, 250 + radius),
                (600 - radius, 100 + diagonal_offset),
                (500 - diagonal_offset, radius),
                (200 + radius, radius),
            ],
        )
    )

    return glyph


def build_agrave(width: float) -> GlyphDefinition:
    glyph = init_glyph("agrave", 0x00E0)
    return glyph


def build_aacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("aacute", 0x00E1)
    return glyph


def build_acircumflex(width: float) -> GlyphDefinition:
    glyph = init_glyph("acircumflex", 0x00E2)
    return glyph


def build_atilde(width: float) -> GlyphDefinition:
    glyph = init_glyph("atilde", 0x00E3)
    return glyph


def build_adieresis(width: float) -> GlyphDefinition:
    glyph = init_glyph("adieresis", 0x00E4)
    return glyph


def build_aring(width: float) -> GlyphDefinition:
    glyph = init_glyph("aring", 0x00E5)
    return glyph


def build_ae(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    # Compensated 45° center slope:
    # original 50 × 50, expanded by diagonal_offset
    slope = 50 + diagonal_offset

    left_x = radius
    right_x = 600 - radius
    top_y = 600 - radius
    bottom_y = radius

    upper_center_y = top_y - slope
    lower_center_y = bottom_y + slope

    glyph = init_glyph("ae", 0x00E6)

    glyph.add(
        polyline(
            width * 0.9,
            [
                # Upper-left outer slope — same size as center slope
                (left_x, top_y - slope),
                (left_x + slope, top_y),

                # Upper-center slope
                (300 - slope, top_y),
                (300, upper_center_y),

                # Lower-center slope
                (300, lower_center_y),
                (300 - slope, bottom_y),

                # Lower-left outer slope
                (left_x + slope, bottom_y),
                (left_x, bottom_y + slope),

                # Middle-left slope
                (left_x, 300 - slope),
                (left_x + slope, 300),

                (300, 300),
            ],
        )
    )

    glyph.add(
        polyline(
            width * 0.9,
            [
                # Lower-right outer slope
                (right_x, bottom_y + slope),
                (right_x - slope, bottom_y),

                # Lower-center slope
                (300 + slope, bottom_y),
                (300, lower_center_y),

                # Upper-center slope
                (300, upper_center_y),
                (300 + slope, top_y),

                # Upper-right outer slope
                (right_x - slope, top_y),
                (right_x, top_y - slope),

                (right_x, 300),
                (300, 300),
            ],
        )
    )

    return glyph

# def build_ae(width: float) -> GlyphDefinition:
#     radius = width / 2
#     diagonal_offset = (math.sqrt(2) - 1) * radius
#     middle_offset = radius - diagonal_offset

#     # Preserve the 45° diagonals into the central stem
#     upper_center_y = 550 - radius - diagonal_offset
#     lower_center_y = 50 + radius + diagonal_offset

#     glyph = init_glyph("ae", 0x00E6)

#     glyph.add(
#         polyline(
#             width,
#             [
#                 (radius, 550 - diagonal_offset),
#                 (50 + diagonal_offset, 600 - radius),
#                 (250 - diagonal_offset, 600 - radius),
#                 (300, upper_center_y),
#                 (300, lower_center_y),
#                 (250 - diagonal_offset, radius),
#                 (50 + diagonal_offset, radius),
#                 (radius, 50 + diagonal_offset),
#                 (radius, 250 + middle_offset),
#                 (50 + diagonal_offset, 300),
#                 (300, 300),
#             ],
#         )
#     )

#     glyph.add(
#         polyline(
#             width,
#             [
#                 (600 - radius, 50 + diagonal_offset),
#                 (550 - diagonal_offset, radius),
#                 (350 + diagonal_offset, radius),
#                 (300, lower_center_y),
#                 (300, upper_center_y),
#                 (350 + diagonal_offset, 600 - radius),
#                 (550 - diagonal_offset, 600 - radius),
#                 (600 - radius, 550 - diagonal_offset),
#                 (600 - radius, 300),
#                 (300, 300),
#             ],
#         )
#     )

#     return glyph


def build_ccedilla(width: float) -> GlyphDefinition:
    glyph = init_glyph("ccedilla", 0x00E7)
    return glyph


def build_egrave(width: float) -> GlyphDefinition:
    glyph = init_glyph("egrave", 0x00E8)
    return glyph


def build_eacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("eacute", 0x00E9)
    return glyph


def build_ecircumflex(width: float) -> GlyphDefinition:
    glyph = init_glyph("ecircumflex", 0x00EA)
    return glyph


def build_edieresis(width: float) -> GlyphDefinition:
    glyph = init_glyph("edieresis", 0x00EB)
    return glyph


def build_igrave(width: float) -> GlyphDefinition:
    glyph = init_glyph("igrave", 0x00EC)
    return glyph


def build_iacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("iacute", 0x00ED)
    return glyph


def build_icircumflex(width: float) -> GlyphDefinition:
    glyph = init_glyph("icircumflex", 0x00EE)
    return glyph


def build_idieresis(width: float) -> GlyphDefinition:
    glyph = init_glyph("idieresis", 0x00EF)
    return glyph


def build_eth(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    # Upper diagonal ending:
    # (450, 750) -> (250, 900) = 200:150 = 4:3
    upper_x_offset = (4 / 5) * radius
    upper_y_offset = (3 / 5) * radius

    # Cross stroke:
    # (200, 700) -> (550, 850) = 350:150 = 7:3
    cross_length = math.sqrt(350**2 + 150**2)
    cross_x_offset = (350 / cross_length) * radius
    cross_y_offset = (150 / cross_length) * radius

    glyph = init_glyph("eth", 0x00F0)

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
                (600 - radius, 400 + radius),
                (600 - radius, 500),
                (450 - radius, 750),
                (
                    250 - radius + upper_x_offset,
                    900 - upper_y_offset,
                ),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (
                200 + cross_x_offset,
                700 + cross_y_offset,
            ),
            (
                550 - cross_x_offset,
                850 - cross_y_offset,
            ),
        )
    )

    return glyph


def build_ntilde(width: float) -> GlyphDefinition:
    glyph = init_glyph("ntilde", 0x00F1)
    return glyph


def build_ograve(width: float) -> GlyphDefinition:
    glyph = init_glyph("ograve", 0x00F2)
    return glyph


def build_oacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("oacute", 0x00F3)
    return glyph


def build_ocircumflex(width: float) -> GlyphDefinition:
    glyph = init_glyph("ocircumflex", 0x00F4)
    return glyph


def build_otilde(width: float) -> GlyphDefinition:
    glyph = init_glyph("otilde", 0x00F5)
    return glyph


def build_odieresis(width: float) -> GlyphDefinition:
    glyph = init_glyph("odieresis", 0x00F6)
    return glyph


def build_oslash(width: float) -> GlyphDefinition:
    glyph = init_glyph("oslash", 0x00F8)
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    slash_length = math.sqrt(600**2 + 700**2)
    slash_x_offset = (600 / slash_length) * radius
    slash_y_offset = (700 / slash_length) * radius

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
            (
                slash_x_offset,
                -50 + slash_y_offset,
            ),
            (
                600 - slash_x_offset,
                650 - slash_y_offset,
            ),
        )
    )

    return glyph


def build_ugrave(width: float) -> GlyphDefinition:
    glyph = init_glyph("ugrave", 0x00F9)
    return glyph


def build_uacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("uacute", 0x00FA)
    return glyph


def build_ucircumflex(width: float) -> GlyphDefinition:
    glyph = init_glyph("ucircumflex", 0x00FB)
    return glyph


def build_udieresis(width: float) -> GlyphDefinition:
    glyph = init_glyph("udieresis", 0x00FC)
    return glyph


def build_yacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("yacute", 0x00FD)
    return glyph


def build_thorn(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("thorn", 0x00FE)

    glyph.add(
        line(
            width,
            (radius, 800 - radius),
            (radius, -200 + radius),
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (radius, 150 + diagonal_offset),
                (150 + diagonal_offset, radius),
                (450 - diagonal_offset, radius),
                (600 - radius, 150 + diagonal_offset),
                (600 - radius, 450 - diagonal_offset),
                (450 - diagonal_offset, 600 - radius),
                (150 + diagonal_offset, 600 - radius),
                (radius, 450 - diagonal_offset),
            ],
        )
    )

    return glyph


def build_ydieresis(width: float) -> GlyphDefinition:
    glyph = init_glyph("ydieresis", 0x00FF)
    return glyph


def build_amacron(width: float) -> GlyphDefinition:
    glyph = init_glyph("amacron", 0x0101)
    return glyph


def build_abreve(width: float) -> GlyphDefinition:
    glyph = init_glyph("abreve", 0x0103)
    return glyph


def build_aogonek(width: float) -> GlyphDefinition:
    glyph = init_glyph("aogonek", 0x0105)
    return glyph


def build_cacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("cacute", 0x0107)
    return glyph


def build_cdotaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("cdotaccent", 0x010B)
    return glyph


def build_ccaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("ccaron", 0x010D)
    return glyph


def build_dcaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("dcaron", 0x010F)
    glyph.objects.extend(build_d(width).objects)

    # Keep the right-side placement and align the comma's visible top edge.
    dot_width = width * 1.5 * COMMA_ACCENT_SCALE
    dot_radius = dot_width / 2
    tail_width = dot_radius
    tail_radius = tail_width / 2
    comma_x, comma_y = (725, COMMA_CARON_TOP - dot_radius)
    tail_x = comma_x + dot_radius - tail_radius
    y_offset = comma_y - dot_radius

    glyph.add(dot(dot_width, (comma_x, comma_y)))
    glyph.add(
        polyline(
            tail_width,
            [
                (tail_x, comma_y),
                (tail_x, -100 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
                (tail_x - 50 * COMMA_ACCENT_SCALE, -150 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
                (comma_x - dot_radius + tail_radius, -150 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
            ],
        )
    )
    return glyph


def build_dcroat(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("dcroat", 0x0111)

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
            (600 - radius, 875 - radius),
            (600 - radius, radius),
        )
    )

    glyph.add(
        line(
            width,
            (350 + radius, 725),
            (700 - radius, 725),
        )
    )

    return glyph


def build_emacron(width: float) -> GlyphDefinition:
    glyph = init_glyph("emacron", 0x0113)
    return glyph


def build_edotaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("edotaccent", 0x0117)
    return glyph


def build_eogonek(width: float) -> GlyphDefinition:
    glyph = init_glyph("eogonek", 0x0119)
    base = build_e(width)
    glyph.objects.extend(base.objects)

    # Attach at the baseline with the visible right edge at x=450.
    # Control points are stroke centers, so compensate by half the width.
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    end_x, end_y = (500 - diagonal_offset, radius)
    glyph.add(
        polyline(
            width,
            [
                (end_x, end_y),
                (end_x - 100, end_y - 100),
                (end_x - 100, end_y - 150),
                (end_x - 50, end_y - 200),
                (end_x, end_y - 200),
            ],
        )
    )
    return glyph


def build_ecaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("ecaron", 0x011B)
    return glyph


def build_gbreve(width: float) -> GlyphDefinition:
    glyph = init_glyph("gbreve", 0x011F)
    return glyph


def build_gdotaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("gdotaccent", 0x0121)
    return glyph


def build_gcommaaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("gcommaaccent", 0x0123)
    glyph.objects.extend(build_g(width).objects)

    # Rotate the comma 180 degrees, centering its dot at the dotaccent position.
    dot_width = width * 1.5 * COMMA_ACCENT_SCALE
    dot_radius = dot_width / 2
    tail_width = dot_radius
    tail_radius = tail_width / 2
    comma_x, comma_y = (300, 800)
    tail_x = comma_x - dot_radius + tail_radius
    y_offset = comma_y + dot_radius

    glyph.add(dot(dot_width, (comma_x, comma_y)))
    glyph.add(
        polyline(
            tail_width,
            [
                (tail_x, comma_y),
                (tail_x, 100 * COMMA_ACCENT_SCALE - tail_radius + y_offset),
                (tail_x + 50 * COMMA_ACCENT_SCALE, 150 * COMMA_ACCENT_SCALE - tail_radius + y_offset),
                (comma_x + dot_radius - tail_radius, 150 * COMMA_ACCENT_SCALE - tail_radius + y_offset),
            ],
        )
    )
    return glyph


def build_hbar(width: float) -> GlyphDefinition:
    glyph = init_glyph("hbar", 0x0127)
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph.add(
        line(
            width,
            (radius, radius),
            (radius, 875 - radius),
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

    glyph.add(
        line(
            width,
            (-100 + radius, 725),
            (250 - radius, 725)
        )
    )
    
    return glyph


def build_imacron(width: float) -> GlyphDefinition:
    glyph = init_glyph("imacron", 0x012B)
    return glyph


def build_iogonek(width: float) -> GlyphDefinition:
    glyph = init_glyph("iogonek", 0x012F)
    return glyph


def build_idotless(width: float) -> GlyphDefinition:
    glyph = init_glyph("idotless", 0x0131)
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    junction_offset = radius - diagonal_offset

    # glyph = init_glyph("i", "i")
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
    # glyph.add(
    #     dot(
    #         width * 1.25,
    #         (300, 800),
    #     )
    # )
    return glyph


def build_kcommaaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("kcommaaccent", 0x0137)
    glyph.objects.extend(build_k(width).objects)

    # Match Kcommaaccent's comma shape and placement at the bottom anchor.
    dot_width = width * 1.5 * COMMA_ACCENT_SCALE
    dot_radius = dot_width / 2
    tail_width = dot_radius
    tail_radius = tail_width / 2
    anchor_x, anchor_y = glyph.anchors["bottom"]
    tail_x = anchor_x + dot_radius - tail_radius
    y_offset = anchor_y - 200

    glyph.add(dot(dot_width, (anchor_x, dot_radius + y_offset)))
    glyph.add(
        polyline(
            tail_width,
            [
                (tail_x, dot_radius + y_offset),
                (tail_x, -100 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
                (tail_x - 50 * COMMA_ACCENT_SCALE, -150 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
                (anchor_x - dot_radius + tail_radius, -150 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
            ],
        )
    )
    return glyph


def build_lacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("lacute", 0x013A)
    glyph.objects.extend(build_l(width).objects)

    # Lowercase l reaches cap height, so use the uppercase top anchor.
    glyph.set_anchor("top", (300, 800))
    anchor_x, anchor_y = glyph.anchors["top"]
    glyph.add(
        line(
            width * 0.9,
            (anchor_x, anchor_y + 150),
            (anchor_x + 100, anchor_y + 250),
        )
    )
    return glyph


def build_lcommaaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("lcommaaccent", 0x013C)
    glyph.objects.extend(build_l(width).objects)

    # Match kcommaaccent's comma shape and placement at the bottom anchor.
    dot_width = width * 1.5 * COMMA_ACCENT_SCALE
    dot_radius = dot_width / 2
    tail_width = dot_radius
    tail_radius = tail_width / 2
    anchor_x, anchor_y = glyph.anchors["bottom"]
    tail_x = anchor_x + dot_radius - tail_radius
    y_offset = anchor_y - 200

    glyph.add(dot(dot_width, (anchor_x, dot_radius + y_offset)))
    glyph.add(
        polyline(
            tail_width,
            [
                (tail_x, dot_radius + y_offset),
                (tail_x, -100 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
                (tail_x - 50 * COMMA_ACCENT_SCALE, -150 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
                (anchor_x - dot_radius + tail_radius, -150 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
            ],
        )
    )
    return glyph


def build_lcaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("lcaron", 0x013E)
    glyph.objects.extend(build_l(width).objects)

    # Match dcaron's right-side comma, including top-edge compensation.
    dot_width = width * 1.5 * COMMA_ACCENT_SCALE
    dot_radius = dot_width / 2
    tail_width = dot_radius
    tail_radius = tail_width / 2
    comma_x, comma_y = (600 - dot_radius, COMMA_CARON_TOP - dot_radius)
    tail_x = comma_x + dot_radius - tail_radius
    y_offset = comma_y - dot_radius

    glyph.add(dot(dot_width, (comma_x, comma_y)))
    glyph.add(
        polyline(
            tail_width,
            [
                (tail_x, comma_y),
                (tail_x, -100 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
                (tail_x - 50 * COMMA_ACCENT_SCALE, -150 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
                (comma_x - dot_radius + tail_radius, -150 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
            ],
        )
    )
    return glyph


def build_lslash(width: float) -> GlyphDefinition:
    radius = width / 2

    slash_length = math.sqrt(400**2 + 200**2)
    slash_x_offset = (400 / slash_length) * radius
    slash_y_offset = (200 / slash_length) * radius

    glyph = init_glyph("lslash", 0x0142)

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
                (300, radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (
                100 + slash_x_offset,
                300 + slash_y_offset,
            ),
            (
                500 - slash_x_offset,
                500 - slash_y_offset,
            ),
        )
    )

    return glyph


def build_nacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("nacute", 0x0144)
    return glyph


def build_ncommaaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("ncommaaccent", 0x0146)
    glyph.objects.extend(build_n(width).objects)

    # Match lcommaaccent's comma shape and placement at the bottom anchor.
    dot_width = width * 1.5 * COMMA_ACCENT_SCALE
    dot_radius = dot_width / 2
    tail_width = dot_radius
    tail_radius = tail_width / 2
    anchor_x, anchor_y = glyph.anchors["bottom"]
    tail_x = anchor_x + dot_radius - tail_radius
    y_offset = anchor_y - 200

    glyph.add(dot(dot_width, (anchor_x, dot_radius + y_offset)))
    glyph.add(
        polyline(
            tail_width,
            [
                (tail_x, dot_radius + y_offset),
                (tail_x, -100 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
                (tail_x - 50 * COMMA_ACCENT_SCALE, -150 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
                (anchor_x - dot_radius + tail_radius, -150 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
            ],
        )
    )
    return glyph


def build_ncaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("ncaron", 0x0148)
    return glyph


def build_ohungarumlaut(width: float) -> GlyphDefinition:
    glyph = init_glyph("ohungarumlaut", 0x0151)
    return glyph


def build_oe(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    # Use the center-slope compensation as the master.
    # All 45° chamfers are made equal to the compensated center slope.
    slope = 50 + diagonal_offset

    left_x = radius
    right_x = 600 - radius
    top_y = 600 - radius
    bottom_y = radius

    upper_center_y = top_y - slope
    lower_center_y = bottom_y + slope

    glyph = init_glyph("oe", 0x0153)

    # o
    glyph.add(
        polyline(
            width * 0.9,
            [
                (300, upper_center_y),
                (300 - slope, top_y),
                (left_x + slope, top_y),
                (left_x, top_y - slope),
                (left_x, bottom_y + slope),
                (left_x + slope, bottom_y),
                (300 - slope, bottom_y),
                (300, lower_center_y),
            ],
        )
    )

    # e
    glyph.add(
        polyline(
            width * 0.9,
            [
                (right_x, bottom_y + slope),
                (right_x - slope, bottom_y),
                (300 + slope, bottom_y),
                (300, lower_center_y),
                (300, upper_center_y),
                (300 + slope, top_y),
                (right_x - slope, top_y),
                (right_x, top_y - slope),
                (right_x, 300),
                (300, 300),
            ],
        )
    )

    return glyph


def build_racute(width: float) -> GlyphDefinition:
    glyph = init_glyph("racute", 0x0155)
    return glyph


def build_rcaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("rcaron", 0x0159)
    return glyph


def build_sacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("sacute", 0x015B)
    return glyph


def build_scedilla(width: float) -> GlyphDefinition:
    glyph = init_glyph("scedilla", 0x015F)
    return glyph


def build_scaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("scaron", 0x0161)
    return glyph


def build_tcaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("tcaron", 0x0165)
    glyph.objects.extend(build_t(width).objects)

    # Match lcaron's right-side comma and top-edge compensation.
    dot_width = width * 1.5 * COMMA_ACCENT_SCALE
    dot_radius = dot_width / 2
    tail_width = dot_radius
    tail_radius = tail_width / 2
    comma_x, comma_y = (600 - dot_radius, COMMA_CARON_TOP - dot_radius)
    tail_x = comma_x + dot_radius - tail_radius
    y_offset = comma_y - dot_radius

    glyph.add(dot(dot_width, (comma_x, comma_y)))
    glyph.add(
        polyline(
            tail_width,
            [
                (tail_x, comma_y),
                (tail_x, -100 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
                (tail_x - 50 * COMMA_ACCENT_SCALE, -150 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
                (comma_x - dot_radius + tail_radius, -150 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
            ],
        )
    )
    return glyph


def build_umacron(width: float) -> GlyphDefinition:
    glyph = init_glyph("umacron", 0x016B)
    return glyph


def build_uring(width: float) -> GlyphDefinition:
    glyph = init_glyph("uring", 0x016F)
    return glyph


def build_uhungarumlaut(width: float) -> GlyphDefinition:
    glyph = init_glyph("uhungarumlaut", 0x0171)
    return glyph


def build_uogonek(width: float) -> GlyphDefinition:
    glyph = init_glyph("uogonek", 0x0173)
    return glyph


def build_wcircumflex(width: float) -> GlyphDefinition:
    glyph = init_glyph("wcircumflex", 0x0175)
    return glyph


def build_ycircumflex(width: float) -> GlyphDefinition:
    glyph = init_glyph("ycircumflex", 0x0177)
    return glyph


def build_zacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("zacute", 0x017A)
    return glyph


def build_zdotaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("zdotaccent", 0x017C)
    return glyph


def build_zcaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("zcaron", 0x017E)
    return glyph


def build_scommaaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("scommaaccent", 0x0219)
    return glyph


def build_tcommaaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("tcommaaccent", 0x021B)
    return glyph


def build_jdotless(width: float) -> GlyphDefinition:
    glyph = init_glyph("jdotless", 0x0237)
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    # glyph = init_glyph("j", "j")
    # glyph.add(
    #     dot(
    #         width * 1.25,
    #         (400, 800),
    #     )
    # )
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


def build_wgrave(width: float) -> GlyphDefinition:
    glyph = init_glyph("wgrave", 0x1E81)
    return glyph


def build_wacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("wacute", 0x1E83)
    return glyph


def build_wdieresis(width: float) -> GlyphDefinition:
    glyph = init_glyph("wdieresis", 0x1E85)
    return glyph


def build_ygrave(width: float) -> GlyphDefinition:
    glyph = init_glyph("ygrave", 0x1EF3)
    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    "\u00DF": build_germandbls,
    "\u00E0": build_agrave,
    "\u00E1": build_aacute,
    "\u00E2": build_acircumflex,
    "\u00E3": build_atilde,
    "\u00E4": build_adieresis,
    "\u00E5": build_aring,
    "\u00E6": build_ae,
    "\u00E7": build_ccedilla,
    "\u00E8": build_egrave,
    "\u00E9": build_eacute,
    "\u00EA": build_ecircumflex,
    "\u00EB": build_edieresis,
    "\u00EC": build_igrave,
    "\u00ED": build_iacute,
    "\u00EE": build_icircumflex,
    "\u00EF": build_idieresis,
    "\u00F0": build_eth,
    "\u00F1": build_ntilde,
    "\u00F2": build_ograve,
    "\u00F3": build_oacute,
    "\u00F4": build_ocircumflex,
    "\u00F5": build_otilde,
    "\u00F6": build_odieresis,
    "\u00F8": build_oslash,
    "\u00F9": build_ugrave,
    "\u00FA": build_uacute,
    "\u00FB": build_ucircumflex,
    "\u00FC": build_udieresis,
    "\u00FD": build_yacute,
    "\u00FE": build_thorn,
    "\u00FF": build_ydieresis,
    "\u0101": build_amacron,
    "\u0103": build_abreve,
    "\u0105": build_aogonek,
    "\u0107": build_cacute,
    "\u010B": build_cdotaccent,
    "\u010D": build_ccaron,
    "\u010F": build_dcaron,
    "\u0111": build_dcroat,
    "\u0113": build_emacron,
    "\u0117": build_edotaccent,
    "\u0119": build_eogonek,
    "\u011B": build_ecaron,
    "\u011F": build_gbreve,
    "\u0121": build_gdotaccent,
    "\u0123": build_gcommaaccent,
    "\u0127": build_hbar,
    "\u012B": build_imacron,
    "\u012F": build_iogonek,
    "\u0131": build_idotless,
    "\u0137": build_kcommaaccent,
    "\u013A": build_lacute,
    "\u013C": build_lcommaaccent,
    "\u013E": build_lcaron,
    "\u0142": build_lslash,
    "\u0144": build_nacute,
    "\u0146": build_ncommaaccent,
    "\u0148": build_ncaron,
    "\u0151": build_ohungarumlaut,
    "\u0153": build_oe,
    "\u0155": build_racute,
    "\u0159": build_rcaron,
    "\u015B": build_sacute,
    "\u015F": build_scedilla,
    "\u0161": build_scaron,
    "\u0165": build_tcaron,
    "\u016B": build_umacron,
    "\u016F": build_uring,
    "\u0171": build_uhungarumlaut,
    "\u0173": build_uogonek,
    "\u0175": build_wcircumflex,
    "\u0177": build_ycircumflex,
    "\u017A": build_zacute,
    "\u017C": build_zdotaccent,
    "\u017E": build_zcaron,
    "\u0219": build_scommaaccent,
    "\u021B": build_tcommaaccent,
    "\u0237": build_jdotless,
    "\u1E81": build_wgrave,
    "\u1E83": build_wacute,
    "\u1E85": build_wdieresis,
    "\u1EF3": build_ygrave,
}


__all__ = [
    "BUILDERS",
    "build_germandbls",
    "build_agrave",
    "build_aacute",
    "build_acircumflex",
    "build_atilde",
    "build_adieresis",
    "build_aring",
    "build_ae",
    "build_ccedilla",
    "build_egrave",
    "build_eacute",
    "build_ecircumflex",
    "build_edieresis",
    "build_igrave",
    "build_iacute",
    "build_icircumflex",
    "build_idieresis",
    "build_eth",
    "build_ntilde",
    "build_ograve",
    "build_oacute",
    "build_ocircumflex",
    "build_otilde",
    "build_odieresis",
    "build_oslash",
    "build_ugrave",
    "build_uacute",
    "build_ucircumflex",
    "build_udieresis",
    "build_yacute",
    "build_thorn",
    "build_ydieresis",
    "build_amacron",
    "build_abreve",
    "build_aogonek",
    "build_cacute",
    "build_cdotaccent",
    "build_ccaron",
    "build_dcaron",
    "build_dcroat",
    "build_emacron",
    "build_edotaccent",
    "build_eogonek",
    "build_ecaron",
    "build_gbreve",
    "build_gdotaccent",
    "build_gcommaaccent",
    "build_hbar",
    "build_imacron",
    "build_iogonek",
    "build_idotless",
    "build_kcommaaccent",
    "build_lacute",
    "build_lcommaaccent",
    "build_lcaron",
    "build_lslash",
    "build_nacute",
    "build_ncommaaccent",
    "build_ncaron",
    "build_ohungarumlaut",
    "build_oe",
    "build_racute",
    "build_rcaron",
    "build_sacute",
    "build_scedilla",
    "build_scaron",
    "build_tcaron",
    "build_umacron",
    "build_uring",
    "build_uhungarumlaut",
    "build_uogonek",
    "build_wcircumflex",
    "build_ycircumflex",
    "build_zacute",
    "build_zdotaccent",
    "build_zcaron",
    "build_scommaaccent",
    "build_tcommaaccent",
    "build_jdotless",
    "build_wgrave",
    "build_wacute",
    "build_wdieresis",
    "build_ygrave",
]
