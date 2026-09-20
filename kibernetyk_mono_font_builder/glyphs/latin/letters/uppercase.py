"""Blank builders for uppercase Latin Core additions."""

from __future__ import annotations

import math

from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition, dot, init_glyph, line, polygon, polyline
from kibernetyk_mono_font_builder.core.config import COMMA_ACCENT_SCALE, COMMA_CARON_TOP
from kibernetyk_mono_font_builder.glyphs.ascii.letters.uppercase import build_G, build_K, build_L, build_N, build_U

def build_Agrave(width: float) -> GlyphDefinition:
    glyph = init_glyph("Agrave", 0x00C0)
    return glyph


def build_Aacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("Aacute", 0x00C1)
    return glyph


def build_Acircumflex(width: float) -> GlyphDefinition:
    glyph = init_glyph("Acircumflex", 0x00C2)
    return glyph


def build_Atilde(width: float) -> GlyphDefinition:
    glyph = init_glyph("Atilde", 0x00C3)
    return glyph


def build_Adieresis(width: float) -> GlyphDefinition:
    glyph = init_glyph("Adieresis", 0x00C4)
    return glyph


def build_Aring(width: float) -> GlyphDefinition:
    glyph = init_glyph("Aring", 0x00C5)
    return glyph


def build_AE(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("AE", 0x00C6)

    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 650 - diagonal_offset),
                (150 + diagonal_offset, 800 - radius),
                (600 - radius, 800 - radius),
            ],
        )
    )

    glyph.add(
        polyline(
            width,
            [
                (325, 800 - radius),
                (325, radius),
                (600 - radius, radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (radius, 400),
            (550 - radius, 400),
        )
    )

    return glyph


def build_Ccedilla(width: float) -> GlyphDefinition:
    glyph = init_glyph("Ccedilla", 0x00C7)
    return glyph


def build_Egrave(width: float) -> GlyphDefinition:
    glyph = init_glyph("Egrave", 0x00C8)
    return glyph


def build_Eacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("Eacute", 0x00C9)
    return glyph


def build_Ecircumflex(width: float) -> GlyphDefinition:
    glyph = init_glyph("Ecircumflex", 0x00CA)
    return glyph


def build_Edieresis(width: float) -> GlyphDefinition:
    glyph = init_glyph("Edieresis", 0x00CB)
    return glyph


def build_Igrave(width: float) -> GlyphDefinition:
    glyph = init_glyph("Igrave", 0x00CC)
    return glyph


def build_Iacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("Iacute", 0x00CD)
    return glyph


def build_Icircumflex(width: float) -> GlyphDefinition:
    glyph = init_glyph("Icircumflex", 0x00CE)
    return glyph


def build_Idieresis(width: float) -> GlyphDefinition:
    glyph = init_glyph("Idieresis", 0x00CF)
    return glyph


def build_Eth(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    glyph = init_glyph("Eth", 0x00D0)
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
    glyph.add(
        line(
            width,
            (-100 + radius, 400),
            (300 - radius, 400)
        )
    )
    return glyph


def build_Ntilde(width: float) -> GlyphDefinition:
    glyph = init_glyph("Ntilde", 0x00D1)
    return glyph


def build_Ograve(width: float) -> GlyphDefinition:
    glyph = init_glyph("Ograve", 0x00D2)
    return glyph


def build_Oacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("Oacute", 0x00D3)
    return glyph


def build_Ocircumflex(width: float) -> GlyphDefinition:
    glyph = init_glyph("Ocircumflex", 0x00D4)
    return glyph


def build_Otilde(width: float) -> GlyphDefinition:
    glyph = init_glyph("Otilde", 0x00D5)
    return glyph


def build_Odieresis(width: float) -> GlyphDefinition:
    glyph = init_glyph("Odieresis", 0x00D6)
    return glyph


def build_Oslash(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    slash_length = math.sqrt(600**2 + 900**2)
    slash_x_offset = (600 / slash_length) * radius
    slash_y_offset = (900 / slash_length) * radius

    glyph = init_glyph("Oslash", 0x00D8)

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
        line(
            width,
            (
                slash_x_offset,
                -50 + slash_y_offset,
            ),
            (
                600 - slash_x_offset,
                850 - slash_y_offset,
            ),
        )
    )

    return glyph


def build_Ugrave(width: float) -> GlyphDefinition:
    glyph = init_glyph("Ugrave", 0x00D9)
    return glyph


def build_Uacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("Uacute", 0x00DA)
    return glyph


def build_Ucircumflex(width: float) -> GlyphDefinition:
    glyph = init_glyph("Ucircumflex", 0x00DB)
    return glyph


def build_Udieresis(width: float) -> GlyphDefinition:
    glyph = init_glyph("Udieresis", 0x00DC)
    return glyph


def build_Yacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("Yacute", 0x00DD)
    return glyph


def build_Thorn(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius

    glyph = init_glyph("Thorn", 0x00DE)

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
                (radius, 150 + radius),
                (450 - diagonal_offset, 150 + radius),
                (600 - radius, 300 + diagonal_offset),
                (600 - radius, 500 - diagonal_offset),
                (450 - diagonal_offset, 650 - radius),
                (radius, 650 - radius),
            ],
        )
    )

    return glyph


def build_Amacron(width: float) -> GlyphDefinition:
    glyph = init_glyph("Amacron", 0x0100)
    return glyph


def build_Abreve(width: float) -> GlyphDefinition:
    glyph = init_glyph("Abreve", 0x0102)
    return glyph


def build_Aogonek(width: float) -> GlyphDefinition:
    glyph = init_glyph("Aogonek", 0x0104)
    return glyph


def build_Cacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("Cacute", 0x0106)
    return glyph


def build_Cdotaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("Cdotaccent", 0x010A)
    return glyph


def build_Ccaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("Ccaron", 0x010C)
    return glyph


def build_Dcaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("Dcaron", 0x010E)
    return glyph


def build_Dcroat(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    glyph = init_glyph("Dcroat", 0x0110)
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
    glyph.add(
        line(
            width,
            (-100 + radius, 400),
            (300 - radius, 400)
        )
    )
    return glyph
    
    return glyph


def build_Emacron(width: float) -> GlyphDefinition:
    glyph = init_glyph("Emacron", 0x0112)
    return glyph


def build_Edotaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("Edotaccent", 0x0116)
    return glyph


def build_Eogonek(width: float) -> GlyphDefinition:
    glyph = init_glyph("Eogonek", 0x0118)
    return glyph


def build_Ecaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("Ecaron", 0x011A)
    return glyph


def build_Gbreve(width: float) -> GlyphDefinition:
    glyph = init_glyph("Gbreve", 0x011E)
    return glyph


def build_Gdotaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("Gdotaccent", 0x0120)
    return glyph


def build_Gcommaaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("Gcommaaccent", 0x0122)
    glyph.objects.extend(build_G(width).objects)

    # Draw commaaccentcomb explicitly at the bottom anchor. Having outlines
    # prevents the automatic Unicode decomposition from selecting a cedilla.
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


def build_Hbar(width: float) -> GlyphDefinition:
    radius = width / 2

    glyph = init_glyph("Hbar", 0x0126)
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
    glyph.add(
        line(
            width,
            (-100 + radius, 650),
            (700 - radius, 650)
        )
    )
    return glyph

def build_Imacron(width: float) -> GlyphDefinition:
    glyph = init_glyph("Imacron", 0x012A)
    return glyph


def build_Iogonek(width: float) -> GlyphDefinition:
    glyph = init_glyph("Iogonek", 0x012E)
    return glyph


def build_Idotaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("Idotaccent", 0x0130)
    return glyph


def build_Kcommaaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("Kcommaaccent", 0x0136)
    glyph.objects.extend(build_K(width).objects)

    # Draw commaaccentcomb explicitly at the bottom anchor.
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


def build_Lacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("Lacute", 0x0139)
    glyph.objects.extend(build_L(width).objects)

    # Align the lower endpoint of acutecomb over the L stem's top terminal.
    # Keep acutecomb's shape and its usual height above the cap-height anchor.
    stem_x = width / 2
    cap_height = glyph.anchors["top"][1]
    glyph.add(
        line(
            width * 0.9,
            (stem_x, cap_height + 150),
            (stem_x + 100, cap_height + 250),
        )
    )
    return glyph


def build_Lcommaaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("Lcommaaccent", 0x013B)
    glyph.objects.extend(build_L(width).objects)

    # Draw commaaccentcomb explicitly at the bottom anchor.
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


def build_Lcaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("Lcaron", 0x013D)
    glyph.objects.extend(build_L(width).objects)

    # Keep the comma centered at x=300 and align its visible top with d/l/tcaron.
    dot_width = width * 1.5 * COMMA_ACCENT_SCALE
    dot_radius = dot_width / 2
    tail_width = dot_radius
    tail_radius = tail_width / 2
    comma_x, comma_y = (300, COMMA_CARON_TOP - dot_radius)
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


def build_Lslash(width: float) -> GlyphDefinition:
    radius = width / 2

    slash_length = math.sqrt(400**2 + 200**2)
    slash_x_offset = (400 / slash_length) * radius
    slash_y_offset = (200 / slash_length) * radius

    glyph = init_glyph("Lslash", 0x0141)

    glyph.add(
        polyline(
            width,
            [
                (radius, 800 - radius),
                (radius, radius),
                (600 - radius, radius),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (
                -100 + slash_x_offset,
                300 + slash_y_offset,
            ),
            (
                300 - slash_x_offset,
                500 - slash_y_offset,
            ),
        )
    )

    return glyph


def build_Nacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("Nacute", 0x0143)
    return glyph


def build_Ncommaaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("Ncommaaccent", 0x0145)
    glyph.objects.extend(build_N(width).objects)

    # Draw commaaccentcomb explicitly at the bottom anchor.
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


def build_Ncaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("Ncaron", 0x0147)
    return glyph


def build_Ohungarumlaut(width: float) -> GlyphDefinition:
    glyph = init_glyph("Ohungarumlaut", 0x0150)
    return glyph


def build_OE(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    # Use compensated left-side 100×100 chamfer as master
    slope = 100 - middle_offset

    left_x = radius
    center_x = 350
    top_y = 800 - radius
    bottom_y = radius

    upper_center_y = top_y - slope
    lower_center_y = bottom_y + slope

    glyph = init_glyph("OE", 0x0152)

    # O
    glyph.add(
        polyline(
            width,
            [
                (left_x, 400),

                # Upper-left master slope
                (left_x, top_y - slope),
                (left_x + slope, top_y),

                # Upper-center slope, same size
                (center_x - slope, top_y),
                (center_x, upper_center_y),

                (center_x, lower_center_y),

                # Lower-center slope, same size
                (center_x - slope, bottom_y),

                # Lower-left slope, same size
                (left_x + slope, bottom_y),
                (left_x, bottom_y + slope),

                (left_x, 400),
            ],
        )
    )

    # E
    glyph.add(
        polyline(
            width,
            [
                (600 - radius, top_y),
                (center_x, top_y),
                (center_x, bottom_y),
                (600 - radius, bottom_y),
            ],
        )
    )

    glyph.add(
        line(
            width,
            (center_x, 400),
            (550 - radius, 400),
        )
    )

    return glyph


def build_Racute(width: float) -> GlyphDefinition:
    glyph = init_glyph("Racute", 0x0154)
    return glyph


def build_Rcaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("Rcaron", 0x0158)
    return glyph


def build_Sacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("Sacute", 0x015A)
    return glyph


def build_Scedilla(width: float) -> GlyphDefinition:
    glyph = init_glyph("Scedilla", 0x015E)
    return glyph


def build_Scaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("Scaron", 0x0160)
    return glyph


def build_Tcaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("Tcaron", 0x0164)
    return glyph


def build_Umacron(width: float) -> GlyphDefinition:
    glyph = init_glyph("Umacron", 0x016A)
    return glyph


def build_Uring(width: float) -> GlyphDefinition:
    glyph = init_glyph("Uring", 0x016E)
    return glyph


def build_Uhungarumlaut(width: float) -> GlyphDefinition:
    glyph = init_glyph("Uhungarumlaut", 0x0170)
    return glyph


def build_Uogonek(width: float) -> GlyphDefinition:
    glyph = init_glyph("Uogonek", 0x0172)
    glyph.objects.extend(build_U(width).objects)

    # Attach the ogonek's first point to the center of U's baseline.
    glyph.add(
        polyline(
            width * 0.9,
            [
                (300, 0),
                (200, -100),
                (200, -150),
                (250, -200),
                (300, -200),
            ],
        )
    )
    return glyph


def build_Wcircumflex(width: float) -> GlyphDefinition:
    glyph = init_glyph("Wcircumflex", 0x0174)
    return glyph


def build_Ycircumflex(width: float) -> GlyphDefinition:
    glyph = init_glyph("Ycircumflex", 0x0176)
    return glyph


def build_Ydieresis(width: float) -> GlyphDefinition:
    glyph = init_glyph("Ydieresis", 0x0178)
    return glyph


def build_Zacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("Zacute", 0x0179)
    return glyph


def build_Zdotaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("Zdotaccent", 0x017B)
    return glyph


def build_Zcaron(width: float) -> GlyphDefinition:
    glyph = init_glyph("Zcaron", 0x017D)
    return glyph


def build_Scommaaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("Scommaaccent", 0x0218)
    return glyph


def build_Tcommaaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("Tcommaaccent", 0x021A)
    return glyph


def build_Wgrave(width: float) -> GlyphDefinition:
    glyph = init_glyph("Wgrave", 0x1E80)
    return glyph


def build_Wacute(width: float) -> GlyphDefinition:
    glyph = init_glyph("Wacute", 0x1E82)
    return glyph


def build_Wdieresis(width: float) -> GlyphDefinition:
    glyph = init_glyph("Wdieresis", 0x1E84)
    return glyph


def build_Germandbls(width: float) -> GlyphDefinition:
    radius = width / 2
    diagonal_offset = (math.sqrt(2) - 1) * radius
    middle_offset = radius - diagonal_offset

    # Preserve the 3:4 slope of (600, 800) -> (300, 400)
    top_middle_x_offset = radius / 4

    glyph = init_glyph("Germandbls", 0x1E9E)

    glyph.add(
        polyline(
            width,
            [
                (radius, radius),
                (radius, 650 - diagonal_offset),
                (150 + diagonal_offset, 800 - radius),
                (600 - radius, 800 - radius),
                (300 - top_middle_x_offset, 400),
                (450 - diagonal_offset, 400),
                (600 - radius, 250 + middle_offset),
                (600 - radius, 100 + diagonal_offset),
                (500 - diagonal_offset, radius),
                (200 + radius, radius),
            ],
        )
    )

    return glyph


def build_Ygrave(width: float) -> GlyphDefinition:
    glyph = init_glyph("Ygrave", 0x1EF2)
    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    "\u00C0": build_Agrave,
    "\u00C1": build_Aacute,
    "\u00C2": build_Acircumflex,
    "\u00C3": build_Atilde,
    "\u00C4": build_Adieresis,
    "\u00C5": build_Aring,
    "\u00C6": build_AE,
    "\u00C7": build_Ccedilla,
    "\u00C8": build_Egrave,
    "\u00C9": build_Eacute,
    "\u00CA": build_Ecircumflex,
    "\u00CB": build_Edieresis,
    "\u00CC": build_Igrave,
    "\u00CD": build_Iacute,
    "\u00CE": build_Icircumflex,
    "\u00CF": build_Idieresis,
    "\u00D0": build_Eth,
    "\u00D1": build_Ntilde,
    "\u00D2": build_Ograve,
    "\u00D3": build_Oacute,
    "\u00D4": build_Ocircumflex,
    "\u00D5": build_Otilde,
    "\u00D6": build_Odieresis,
    "\u00D8": build_Oslash,
    "\u00D9": build_Ugrave,
    "\u00DA": build_Uacute,
    "\u00DB": build_Ucircumflex,
    "\u00DC": build_Udieresis,
    "\u00DD": build_Yacute,
    "\u00DE": build_Thorn,
    "\u0100": build_Amacron,
    "\u0102": build_Abreve,
    "\u0104": build_Aogonek,
    "\u0106": build_Cacute,
    "\u010A": build_Cdotaccent,
    "\u010C": build_Ccaron,
    "\u010E": build_Dcaron,
    "\u0110": build_Dcroat,
    "\u0112": build_Emacron,
    "\u0116": build_Edotaccent,
    "\u0118": build_Eogonek,
    "\u011A": build_Ecaron,
    "\u011E": build_Gbreve,
    "\u0120": build_Gdotaccent,
    "\u0122": build_Gcommaaccent,
    "\u0126": build_Hbar,
    "\u012A": build_Imacron,
    "\u012E": build_Iogonek,
    "\u0130": build_Idotaccent,
    "\u0136": build_Kcommaaccent,
    "\u0139": build_Lacute,
    "\u013B": build_Lcommaaccent,
    "\u013D": build_Lcaron,
    "\u0141": build_Lslash,
    "\u0143": build_Nacute,
    "\u0145": build_Ncommaaccent,
    "\u0147": build_Ncaron,
    "\u0150": build_Ohungarumlaut,
    "\u0152": build_OE,
    "\u0154": build_Racute,
    "\u0158": build_Rcaron,
    "\u015A": build_Sacute,
    "\u015E": build_Scedilla,
    "\u0160": build_Scaron,
    "\u0164": build_Tcaron,
    "\u016A": build_Umacron,
    "\u016E": build_Uring,
    "\u0170": build_Uhungarumlaut,
    "\u0172": build_Uogonek,
    "\u0174": build_Wcircumflex,
    "\u0176": build_Ycircumflex,
    "\u0178": build_Ydieresis,
    "\u0179": build_Zacute,
    "\u017B": build_Zdotaccent,
    "\u017D": build_Zcaron,
    "\u0218": build_Scommaaccent,
    "\u021A": build_Tcommaaccent,
    "\u1E80": build_Wgrave,
    "\u1E82": build_Wacute,
    "\u1E84": build_Wdieresis,
    "\u1E9E": build_Germandbls,
    "\u1EF2": build_Ygrave,
}


__all__ = [
    "BUILDERS",
    "build_Agrave",
    "build_Aacute",
    "build_Acircumflex",
    "build_Atilde",
    "build_Adieresis",
    "build_Aring",
    "build_AE",
    "build_Ccedilla",
    "build_Egrave",
    "build_Eacute",
    "build_Ecircumflex",
    "build_Edieresis",
    "build_Igrave",
    "build_Iacute",
    "build_Icircumflex",
    "build_Idieresis",
    "build_Eth",
    "build_Ntilde",
    "build_Ograve",
    "build_Oacute",
    "build_Ocircumflex",
    "build_Otilde",
    "build_Odieresis",
    "build_Oslash",
    "build_Ugrave",
    "build_Uacute",
    "build_Ucircumflex",
    "build_Udieresis",
    "build_Yacute",
    "build_Thorn",
    "build_Amacron",
    "build_Abreve",
    "build_Aogonek",
    "build_Cacute",
    "build_Cdotaccent",
    "build_Ccaron",
    "build_Dcaron",
    "build_Dcroat",
    "build_Emacron",
    "build_Edotaccent",
    "build_Eogonek",
    "build_Ecaron",
    "build_Gbreve",
    "build_Gdotaccent",
    "build_Gcommaaccent",
    "build_Hbar",
    "build_Imacron",
    "build_Iogonek",
    "build_Idotaccent",
    "build_Kcommaaccent",
    "build_Lacute",
    "build_Lcommaaccent",
    "build_Lcaron",
    "build_Lslash",
    "build_Nacute",
    "build_Ncommaaccent",
    "build_Ncaron",
    "build_Ohungarumlaut",
    "build_OE",
    "build_Racute",
    "build_Rcaron",
    "build_Sacute",
    "build_Scedilla",
    "build_Scaron",
    "build_Tcaron",
    "build_Umacron",
    "build_Uring",
    "build_Uhungarumlaut",
    "build_Uogonek",
    "build_Wcircumflex",
    "build_Ycircumflex",
    "build_Ydieresis",
    "build_Zacute",
    "build_Zdotaccent",
    "build_Zcaron",
    "build_Scommaaccent",
    "build_Tcommaaccent",
    "build_Wgrave",
    "build_Wacute",
    "build_Wdieresis",
    "build_Germandbls",
    "build_Ygrave",
]
