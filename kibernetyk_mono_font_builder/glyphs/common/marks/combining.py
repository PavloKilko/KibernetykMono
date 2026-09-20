"""Blank builders for combining accent marks."""

from __future__ import annotations

import math

from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition, dot, init_glyph, line, polyline
from kibernetyk_mono_font_builder.core.config import ADVANCE_WIDTH, COMMA_ACCENT_SCALE


def build_gravecomb(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph(
        "gravecomb",
        0x0300,
        advance_width=0,
    )

    glyph.add(
        line(
            accent_width,
            (-100, 250),
            (0, 150),
        )
    )

    glyph.mark_class = "top"
    glyph.mark_anchor = (0, 0)

    return glyph

def build_acutecomb(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph(
        "acutecomb",
        0x0301,
        advance_width=0,
    )

    glyph.add(
        line(
            accent_width,
            (0, 150),
            (100, 250),
        )
    )

    glyph.mark_class = "top"
    glyph.mark_anchor = (0, 0)

    return glyph


def build_circumflexcomb(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph(
        "circumflexcomb",
        0x0302,
        advance_width=0,
    )

    glyph.add(
        polyline(
            accent_width,
            [
                (-100, 100),
                (0, 200),
                (100, 100),
            ],
        )
    )

    glyph.mark_class = "top"
    glyph.mark_anchor = (0, 0)

    return glyph


def build_tildecomb(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph(
        "tildecomb",
        0x0303,
        advance_width=0,
    )

    glyph.add(
        polyline(
            accent_width,
            [
                (-150, 200),
                (-100, 250),
                (-50, 250),
                (50, 200),
                (100, 200),
                (150, 250),
            ],
        )
    )

    glyph.mark_class = "top"
    glyph.mark_anchor = (0, 0)

    return glyph


def build_macroncomb(width: float) -> GlyphDefinition:
    radius = width / 2
    accent_width = width * 0.9

    glyph = init_glyph(
        "macroncomb",
        0x0304,
        advance_width=0,
    )

    glyph.add(
        line(
            accent_width,
            (-150 + radius, 200),
            (150 - radius, 200),
        )
    )

    glyph.mark_class = "top"
    glyph.mark_anchor = (0, 0)

    return glyph


def build_brevecomb(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph(
        "brevecomb",
        0x0306,
        advance_width=0,
    )

    glyph.add(
        polyline(
            accent_width,
            [
                (-150, 250),
                (-50, 150),
                (50, 150),
                (150, 250),
            ],
        )
    )

    glyph.mark_class = "top"
    glyph.mark_anchor = (0, 0)

    return glyph


def build_dotaccentcomb(width: float) -> GlyphDefinition:
    dot_width = width * 1.25

    glyph = init_glyph(
        "dotaccentcomb",
        0x0307,
        advance_width=0,
    )

    glyph.add(
        dot(
            dot_width,
            (0, 200),
        )
    )

    glyph.mark_class = "top"
    glyph.mark_anchor = (0, 0)

    return glyph


def build_dieresiscomb(width: float) -> GlyphDefinition:
    dot_width = width * 1.25

    glyph = init_glyph(
        "dieresiscomb",
        0x0308,
        advance_width=0,
    )

    glyph.add(
        dot(
            dot_width,
            (-150, 200),
        )
    )

    glyph.add(
        dot(
            dot_width,
            (150, 200),
        )
    )

    glyph.mark_class = "top"
    glyph.mark_anchor = (0, 0)

    return glyph


def build_ringcomb(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph(
        "ringcomb",
        0x030A,
        advance_width=0,
    )

    glyph.add(
        polyline(
            accent_width,
            [
                (-100, 200),
                (-100, 250),
                (-50, 300),
                (50, 300),
                (100, 250),
                (100, 150),
                (50, 100),
                (-50, 100),
                (-100, 150),
                (-100, 200),
            ],
        )
    )

    glyph.mark_class = "top"
    glyph.mark_anchor = (0, 0)

    return glyph


def build_hungarumlautcomb(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph(
        "hungarumlautcomb",
        0x030B,
        advance_width=0,
    )

    glyph.add(
        line(
            accent_width,
            (-150, 150),
            (-50, 250),
        )
    )

    glyph.add(
        line(
            accent_width,
            (100, 150),
            (200, 250),
        )
    )

    glyph.mark_class = "top"
    glyph.mark_anchor = (0, 0)

    return glyph

def build_caroncomb(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph(
        "caroncomb",
        0x030C,
        advance_width=0,
    )

    glyph.add(
        polyline(
            accent_width,
            [
                (-100, 200),
                (0, 100),
                (100, 200),
            ],
        )
    )

    glyph.mark_class = "top"
    glyph.mark_anchor = (0, 0)

    return glyph


def build_commaaccentcomb(width: float) -> GlyphDefinition:
    dot_width = width * 1.5 * COMMA_ACCENT_SCALE
    dot_radius = dot_width / 2

    tail_width = dot_radius
    tail_radius = tail_width / 2

    # Relative to bottom anchor (300, 0),
    # then move the whole comma down by 200.
    tail_x = dot_radius - tail_radius
    y_offset = -200

    glyph = init_glyph(
        "commaaccentcomb",
        0x0326,
        advance_width=0,
    )

    glyph.add(
        dot(
            dot_width,
            (0, dot_radius + y_offset),
        )
    )

    glyph.add(
        polyline(
            tail_width,
            [
                (tail_x, dot_radius + y_offset),
                (tail_x, -100 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
                (tail_x - 50 * COMMA_ACCENT_SCALE, -150 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
                (-dot_radius + tail_radius, -150 * COMMA_ACCENT_SCALE + tail_radius + y_offset),
            ],
        )
    )

    glyph.mark_class = "bottom"
    glyph.mark_anchor = (0, 0)

    return glyph


def build_cedillacomb(width: float) -> GlyphDefinition:
    accent_width = width * 0.9
    x_offset = ADVANCE_WIDTH - 300
    glyph = init_glyph(
        "cedillacomb",
        0x0327,
        advance_width=0,
    )

    glyph.add(
        polyline(
            accent_width,
            [
                (0, 0),
                (0, -50),
                (100, -100),
                (100, -150),
                (50, -200),
                (-100, -200),
                (-150, -150),
            ],
        )
    )

    glyph.mark_class = "bottom"
    glyph.mark_anchor = (0, 0)

    return glyph


def build_ogonekcomb(width: float) -> GlyphDefinition:
    accent_width = width
    radius = width / 2
    glyph = init_glyph(
        "ogonekcomb",
        0x0328,
        advance_width=0,
    )

    glyph.add(
        polyline(
            accent_width,
            [
                (300 - radius, 0),
                (200 - radius, -100),
                (200 - radius, -150),
                (250 - radius, -200),
                (300 - radius, -200),
            ],
        )
    )

    glyph.mark_class = "bottom"
    glyph.mark_anchor = (0, 0)

    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    "\u0300": build_gravecomb,
    "\u0301": build_acutecomb,
    "\u0302": build_circumflexcomb,
    "\u0303": build_tildecomb,
    "\u0304": build_macroncomb,
    "\u0306": build_brevecomb,
    "\u0307": build_dotaccentcomb,
    "\u0308": build_dieresiscomb,
    "\u030A": build_ringcomb,
    "\u030B": build_hungarumlautcomb,
    "\u030C": build_caroncomb,
    "\u0326": build_commaaccentcomb,
    "\u0327": build_cedillacomb,
    "\u0328": build_ogonekcomb,
}


__all__ = [
    "BUILDERS",
    "build_gravecomb",
    "build_acutecomb",
    "build_circumflexcomb",
    "build_tildecomb",
    "build_macroncomb",
    "build_brevecomb",
    "build_dotaccentcomb",
    "build_dieresiscomb",
    "build_ringcomb",
    "build_hungarumlautcomb",
    "build_caroncomb",
    "build_commaaccentcomb",
    "build_cedillacomb",
    "build_ogonekcomb",
]
