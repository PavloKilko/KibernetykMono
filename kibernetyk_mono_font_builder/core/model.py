"""Glyph-domain models shared by every script and character group."""

from __future__ import annotations

import math
from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import Any

from .config import ADVANCE_WIDTH, GLYPH_CENTER_X


@dataclass(frozen=True)
class GlyphPolygon:
    width: float
    points: tuple[tuple[float, float], ...]
    fill: bool = False


@dataclass
class GlyphDefinition:
    name: str
    codepoint: int | None
    advance_width: int = ADVANCE_WIDTH
    objects: list[Any] = field(default_factory=list)
    rounded: bool = False
    anchors: dict[str, tuple[float, float]] = field(default_factory=dict)
    mark_class: str | None = None
    mark_anchor: tuple[float, float] | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.rounded, bool):
            raise TypeError("rounded must be a boolean")
        if self.advance_width < 0:
            raise ValueError("advance_width cannot be negative")
        self.anchors = {
            name: self._anchor_point(point)
            for name, point in self.anchors.items()
        }
        if self.mark_anchor is not None:
            self.mark_anchor = self._anchor_point(self.mark_anchor)

    @staticmethod
    def _anchor_point(point: Sequence[float]) -> tuple[float, float]:
        if len(point) != 2:
            raise ValueError(f"Expected anchor point (x, y), got {point!r}")
        x, y = float(point[0]), float(point[1])
        if not math.isfinite(x) or not math.isfinite(y):
            raise ValueError("Anchor coordinates must be finite")
        return (x, y)

    def add(self, glyph_object: Any) -> None:
        self.objects.append(glyph_object)

    def set_anchor(self, name: str, point: Sequence[float]) -> None:
        if not name or name.startswith("_"):
            raise ValueError("A base anchor needs a name without a leading '_'")
        self.anchors[name] = self._anchor_point(point)

    def set_mark_anchor(self, mark_class: str, point: Sequence[float]) -> None:
        if not mark_class or mark_class.startswith("_"):
            raise ValueError("A mark class needs a name without a leading '_'")
        self.mark_class = mark_class
        self.mark_anchor = self._anchor_point(point)

    def horizontal_offset(self, rounded: bool | None = None) -> float:
        """Place the shared design origin inside the fixed-width advance cell.

        The offset is independent of ink bounds, accents, weight, and rounding,
        so adding a mark never shifts a letter relative to its unaccented base.
        """

        if rounded is not None and not isinstance(rounded, bool):
            raise TypeError("rounded must be a boolean")
        if not isinstance(self.rounded, bool):
            raise TypeError("glyph.rounded must be a boolean")
        # Combining marks keep their own attachment coordinate system.
        if self.advance_width == 0 or self.mark_class is not None:
            return 0.0
        return self.advance_width / 2 - GLYPH_CENTER_X

    def render_anchors(
        self, rounded: bool | None = None,
    ) -> dict[str, tuple[float, float]]:
        """Place base anchors with the outline, keeping stored anchors local."""

        offset = self.horizontal_offset(rounded)
        return {name: (x + offset, y) for name, (x, y) in self.anchors.items()}

    def render(
        self,
        rounded: bool | None = None,
        *,
        positioned: bool = True,
    ) -> list[list[Any]]:
        """Render local geometry, then apply the shared horizontal origin offset.

        Set positioned=False to inspect the original design coordinates.
        Translation happens after rounding and never mutates source objects.
        """

        # Imported lazily to keep the model independent from renderer startup.
        from .renderer import PRERENDER, render_glyph_object

        if rounded is not None and not isinstance(rounded, bool):
            raise TypeError("rounded must be a boolean")
        if not isinstance(self.rounded, bool):
            raise TypeError("glyph.rounded must be a boolean")
        if not isinstance(positioned, bool):
            raise TypeError("positioned must be a boolean")
        use_rounded = self.rounded if rounded is None else rounded
        polygons = [
            render_glyph_object(obj, rounded=use_rounded)
            for obj in self.objects
        ]
        offset = self.horizontal_offset(use_rounded) if positioned else 0.0
        if offset == 0:
            return polygons
        return [
            [PRERENDER.Point(point.x + offset, point.y) for point in polygon]
            for polygon in polygons
        ]
