"""Builders for the unencoded Google Fonts support glyphs."""

from __future__ import annotations

from kibernetyk_mono_font_builder.core import (
    GLYPH_CENTER_X,
    GlyphBuilder,
    GlyphDefinition,
    dot,
    init_glyph,
    line,
    polyline,
)
from kibernetyk_mono_font_builder.core.config import (
    COMMA_ACCENT_SCALE,
    COMMA_CARON_TOP,
)
from kibernetyk_mono_font_builder.glyphs.ascii.letters.lowercase import build_i


def build_notdef(width: float) -> GlyphDefinition:
    radius = width / 2

    # `.notdef` is the one reserved glyph name that cannot go through
    # init_glyph(). The compiler recognizes this definition and installs it
    # in glyph slot zero.
    glyph = GlyphDefinition(".notdef", None)

    # Outer box
    glyph.add(
        polyline(
            width,
            [
                (radius, 400),
                (radius, 800 - radius),
                (600 - radius, 800 - radius),
                (600 - radius, radius),
                (radius, radius),
                (radius, 400),
            ],
        )
    )

    # Diagonals share the compensated box corners
    glyph.add(
        line(
            width,
            (radius, radius),
            (600 - radius, 800 - radius),
        )
    )

    glyph.add(
        line(
            width,
            (radius, 800 - radius),
            (600 - radius, radius),
        )
    )

    return glyph


def build_periodcentered_loclCAT(width: float) -> GlyphDefinition:
    glyph = init_glyph(
        "periodcentered.loclCAT",
        None,
        advance_width=0,
    )
    glyph.add(dot(width * 1.5, (-100, 400)))
    
    
    return glyph


def build_periodcentered_loclCAT_case(width: float) -> GlyphDefinition:
    glyph = init_glyph(
        "periodcentered.loclCAT.case",
        None,
        advance_width=0,
    )
    glyph.add(dot(width * 1.5, (-300, 400)))
    return glyph


def build_caroncomb_alt(width: float) -> GlyphDefinition:
    glyph = init_glyph(
        "caroncomb.alt", 
        None,
        advance_width=0,
    )

    # Use dcaron's comma design and visible top alignment, centered in this
    # standalone support glyph instead of inheriting dcaron's right-side x.
    dot_width = width * 1.5 * COMMA_ACCENT_SCALE
    dot_radius = dot_width / 2
    tail_width = dot_radius
    tail_radius = tail_width / 2
    comma_x, comma_y = (
        25 - dot_radius,
        COMMA_CARON_TOP - dot_radius,
    )
    tail_x = comma_x + dot_radius - tail_radius
    y_offset = comma_y - dot_radius

    glyph.add(dot(dot_width, (comma_x, comma_y)))
    glyph.add(
        polyline(
            tail_width,
            [
                (tail_x, comma_y),
                (
                    tail_x,
                    -100 * COMMA_ACCENT_SCALE + tail_radius + y_offset,
                ),
                (
                    tail_x - 50 * COMMA_ACCENT_SCALE,
                    -150 * COMMA_ACCENT_SCALE + tail_radius + y_offset,
                ),
                (
                    comma_x - dot_radius + tail_radius,
                    -150 * COMMA_ACCENT_SCALE + tail_radius + y_offset,
                ),
            ],
        )
    )
    return glyph


def build_idotaccent(width: float) -> GlyphDefinition:
    glyph = init_glyph("idotaccent", None)
    # This is a complete localized i because `locl` replaces the whole base
    # glyph. Reusing build_i also keeps its square dot exactly identical.
    glyph.objects.extend(build_i(width).objects)
    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    ".notdef": build_notdef,
    "periodcentered.loclCAT": build_periodcentered_loclCAT,
    "periodcentered.loclCAT.case": build_periodcentered_loclCAT_case,
    "caroncomb.alt": build_caroncomb_alt,
    "idotaccent": build_idotaccent,
}


__all__ = [
    "BUILDERS",
    "build_notdef",
    "build_periodcentered_loclCAT",
    "build_periodcentered_loclCAT_case",
    "build_caroncomb_alt",
    "build_idotaccent",
]
