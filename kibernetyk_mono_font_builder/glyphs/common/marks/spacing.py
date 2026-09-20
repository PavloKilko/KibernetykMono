"""Blank builders for spacing accent marks."""

from __future__ import annotations

import math

from kibernetyk_mono_font_builder.core import GlyphBuilder, GlyphDefinition, dot, init_glyph, line, polyline

def build_dieresis(width: float) -> GlyphDefinition:
    dot_width = width * 1.25
    glyph = init_glyph("dieresis", 0x00A8)

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


def build_macron(width: float) -> GlyphDefinition:
    radius = width / 2
    glyph = init_glyph("macron", 0x00AF)
    glyph.add(
        line(
            width * 0.9,
            (150 + radius, 800),
            (450 - radius, 800)
        )
    )
    return glyph


def build_acute(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph("acute", 0x00B4)

    glyph.add(
        line(
            accent_width,
            (300, 750),
            (400, 850),
        )
    )

    return glyph


def build_cedilla(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph("cedilla", 0x00B8)

    glyph.add(
        polyline(
            accent_width,
            [
                (300, 0),
                (300, -50),
                (400, -100),
                (400, -150),
                (350, -200),
                (200, -200),
                (150, -150),
            ],
        )
    )

    return glyph


def build_circumflex(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph("circumflex", 0x02C6)

    glyph.add(
        polyline(
            accent_width,
            [
                (200, 700),
                (300, 800),
                (400, 700),
            ],
        )
    )

    return glyph


def build_caron(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph("caron", 0x02C7)

    glyph.add(
        polyline(
            accent_width,
            [
                (200, 800),
                (300, 700),
                (400, 800),
            ],
        )
    )

    return glyph


def build_breve(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph("breve", 0x02D8)

    glyph.add(
        polyline(
            accent_width,
            [
                (150, 850),
                (250, 750),
                (350, 750),
                (450, 850),
            ],
        )
    )

    return glyph


def build_dotaccent(width: float) -> GlyphDefinition:
    dot_width = width * 1.25
    glyph = init_glyph("dotaccent", 0x02D9)

    glyph.add(
        dot(
            dot_width,
            (300, 800),
            # (150, 950),   
        )
    )
    
    return glyph


def build_ring(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph("ring", 0x02DA)

    glyph.add(
        polyline(
            accent_width,
            [
                (200, 800),
                (200, 850),
                (250, 900),
                (350, 900),
                (400, 850),
                (400, 750),
                (350, 700),
                (250, 700),
                (200, 750),
                (200, 800),
            ],
        )
    )

    return glyph


def build_ogonek(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph("ogonek", 0x02DB)

    glyph.add(
        polyline(
            accent_width,
            [
                (600, 0),
                (500, -100),
                (500, -150),
                (550, -200),
                (600, -200),
            ],
        )
    )

    return glyph


def build_tilde(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph("tilde", 0x02DC)

    glyph.add(
        polyline(
            accent_width,
            [
                (150, 800),
                (200, 850),
                (250, 850),
                (350, 800),
                (400, 800),
                (450, 850),
            ],
        )
    )

    return glyph


def build_hungarumlaut(width: float) -> GlyphDefinition:
    accent_width = width * 0.9

    glyph = init_glyph("hungarumlaut", 0x02DD)

    glyph.add(
        line(
            accent_width,
            (150, 750),
            (250, 850),
        )
    )

    glyph.add(
        line(
            accent_width,
            (400, 750),
            (500, 850),
        )
    )

    return glyph


BUILDERS: dict[str, GlyphBuilder] = {
    "\u00A8": build_dieresis,
    "\u00AF": build_macron,
    "\u00B4": build_acute,
    "\u00B8": build_cedilla,
    "\u02C6": build_circumflex,
    "\u02C7": build_caron,
    "\u02D8": build_breve,
    "\u02D9": build_dotaccent,
    "\u02DA": build_ring,
    "\u02DB": build_ogonek,
    "\u02DC": build_tilde,
    "\u02DD": build_hungarumlaut,
}


__all__ = [
    "BUILDERS",
    "build_dieresis",
    "build_macron",
    "build_acute",
    "build_cedilla",
    "build_circumflex",
    "build_caron",
    "build_breve",
    "build_dotaccent",
    "build_ring",
    "build_ogonek",
    "build_tilde",
    "build_hungarumlaut",
]
