"""Validated constructors for the geometric glyph primitives."""

from __future__ import annotations

import math
import unicodedata
from typing import Any, Sequence

from .config import ADVANCE_WIDTH, CAP_HEIGHT, GLYPH_CENTER_X, X_HEIGHT
from .model import GlyphDefinition, GlyphPolygon
from .renderer import PRERENDER


def _number(value: float, label: str) -> float:
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"{label} must be finite")
    return number


def _width(value: float) -> float:
    width = _number(value, "width")
    if width <= 0:
        raise ValueError("width must be positive")
    return width


def _point(value: Sequence[float]) -> tuple[float, float]:
    if len(value) != 2:
        raise ValueError(f"Expected point (x, y), got {value!r}")
    return (_number(value[0], "x"), _number(value[1], "y"))


def dot(width: float, point: Sequence[float]) -> Any:
    return PRERENDER.GlyphDot(width=_width(width), point=_point(point))


def line(
    width: float,
    start: Sequence[float],
    end: Sequence[float],
) -> Any:
    return PRERENDER.GlyphLine(
        width=_width(width),
        a=_point(start),
        b=_point(end),
    )


def polyline(width: float, points: Sequence[Sequence[float]]) -> Any:
    normalized = tuple(_point(point) for point in points)
    if len(normalized) < 2:
        raise ValueError("A polyline requires at least two points")
    if any(start == end for start, end in zip(normalized, normalized[1:])):
        raise ValueError("Consecutive polyline points must be distinct")
    return PRERENDER.GlyphPolyline(width=_width(width), points=normalized)


def polygon(
    width: float,
    points: Sequence[Sequence[float]],
    fill: bool = False,
) -> GlyphPolygon:
    """Create a closed stroked polygon, optionally filled inside."""

    normalized = tuple(_point(point) for point in points)
    if len(normalized) > 1 and normalized[0] == normalized[-1]:
        normalized = normalized[:-1]
    if len(normalized) < 3:
        raise ValueError("A polygon requires at least three points")
    if any(start == end for start, end in zip(normalized, normalized[1:])):
        raise ValueError("Consecutive polygon points must be distinct")
    if not isinstance(fill, bool):
        raise TypeError("fill must be a boolean")
    return GlyphPolygon(width=_width(width), points=normalized, fill=fill)


def init_glyph(
    name: str,
    character: str | int | None,
    advance_width: int | None = None,
) -> GlyphDefinition:
    if not name or name == ".notdef":
        raise ValueError(f"Invalid glyph name: {name!r}")
    if isinstance(character, str):
        if len(character) != 1:
            raise ValueError("A glyph character must contain exactly one character")
        codepoint = ord(character)
    else:
        codepoint = character
    if codepoint is not None and not 0 <= codepoint <= 0x10FFFF:
        raise ValueError(f"Invalid Unicode codepoint: {codepoint!r}")
    category = (
        unicodedata.category(chr(codepoint))
        if codepoint is not None
        else None
    )
    if advance_width is None:
        advance_width = (
            0 if category is not None and category.startswith("M")
            else ADVANCE_WIDTH
        )
    if advance_width < 0:
        raise ValueError("advance_width cannot be negative")

    glyph = GlyphDefinition(name, codepoint, advance_width)
    if category == "Ll":
        glyph.set_anchor("top", (GLYPH_CENTER_X, X_HEIGHT))
    elif category == "Lu":
        glyph.set_anchor("top", (GLYPH_CENTER_X, CAP_HEIGHT))
    if category in {"Ll", "Lu"}:
        glyph.set_anchor("bottom", (GLYPH_CENTER_X, 0))
    return glyph
