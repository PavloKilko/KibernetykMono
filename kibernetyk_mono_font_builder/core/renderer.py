"""Higher-level adapter around the internal geometry renderer."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Sequence

from . import graphics_renderer as PRERENDER
from .config import CORNER_CURVE_STEPS, CORNER_RADIUS_RATIO
from .model import GlyphPolygon


def _signed_area(points: Sequence[Any]) -> float:
    return sum(
        point.x * next_point.y - next_point.x * point.y
        for point, next_point in zip(points, (*points[1:], points[0]))
    ) / 2


def _rotate_points(points: list[Any], start: int) -> list[Any]:
    return [*points[start:], *points[:start]]


def _with_winding(points: list[Any], *, clockwise: bool) -> list[Any]:
    """Return a contour with a predictable non-zero-fill direction."""

    is_clockwise = _signed_area(points) < 0
    if is_clockwise != clockwise:
        return list(reversed(points))
    return points


def _round_outline(
    points: Sequence[Any],
    radius: float,
    steps: int = CORNER_CURVE_STEPS,
) -> list[Any]:
    """Replace every polygon corner with a sampled quadratic curve."""

    outline = PRERENDER.dedupe(list(points))
    if len(outline) < 3 or radius <= 0 or steps < 1:
        return outline

    rounded_outline: list[Any] = []
    for index, current in enumerate(outline):
        previous = outline[index - 1]
        following = outline[(index + 1) % len(outline)]

        previous_dx = previous.x - current.x
        previous_dy = previous.y - current.y
        following_dx = following.x - current.x
        following_dy = following.y - current.y
        previous_length = (previous_dx**2 + previous_dy**2) ** 0.5
        following_length = (following_dx**2 + following_dy**2) ** 0.5

        if previous_length <= PRERENDER.EPS or following_length <= PRERENDER.EPS:
            rounded_outline.append(current)
            continue

        cross = previous_dx * following_dy - previous_dy * following_dx
        if abs(cross) <= PRERENDER.EPS * previous_length * following_length:
            rounded_outline.append(current)
            continue

        trim = min(radius, previous_length * 0.5, following_length * 0.5)
        entry = PRERENDER.Point(
            current.x + previous_dx / previous_length * trim,
            current.y + previous_dy / previous_length * trim,
        )
        exit_point = PRERENDER.Point(
            current.x + following_dx / following_length * trim,
            current.y + following_dy / following_length * trim,
        )
        rounded_outline.append(entry)

        for step in range(1, steps + 1):
            t = step / steps
            inverse_t = 1 - t
            rounded_outline.append(
                PRERENDER.Point(
                    inverse_t**2 * entry.x
                    + 2 * inverse_t * t * current.x
                    + t**2 * exit_point.x,
                    inverse_t**2 * entry.y
                    + 2 * inverse_t * t * current.y
                    + t**2 * exit_point.y,
                )
            )

    return PRERENDER.dedupe(rounded_outline)


def _corner_radius(width: float) -> float:
    return width * CORNER_RADIUS_RATIO


def _closed_polyline_polygon(obj: Any) -> GlyphPolygon | None:
    if not isinstance(obj, PRERENDER.GlyphPolyline):
        return None
    if len(obj.points) < 4 or obj.points[0] != obj.points[-1]:
        return None
    return GlyphPolygon(width=obj.width, points=tuple(obj.points[:-1]))


def _render_polygon(obj: GlyphPolygon, *, rounded: bool) -> list[Any]:
    dots = [PRERENDER.Dot(x=x, y=y, w=obj.width) for x, y in obj.points]
    segments = [
        PRERENDER.calculate_vector_lines(dot, dots[(index + 1) % len(dots)])
        for index, dot in enumerate(dots)
    ]

    left_outline: list[Any] = []
    right_outline: list[Any] = []
    for index, dot in enumerate(dots):
        previous_segment = segments[index - 1]
        next_segment = segments[index]
        left_outline.extend(
            PRERENDER.calculate_clipped_join(
                previous_segment.top,
                next_segment.top,
                dot,
            )
        )
        right_outline.extend(
            PRERENDER.calculate_clipped_join(
                previous_segment.bottom,
                next_segment.bottom,
                dot,
            )
        )

    left_outline = PRERENDER.dedupe(left_outline)
    right_outline = PRERENDER.dedupe(right_outline)
    if abs(_signed_area(left_outline)) >= abs(_signed_area(right_outline)):
        outer_outline, inner_outline = left_outline, right_outline
    else:
        outer_outline, inner_outline = right_outline, left_outline

    if rounded:
        radius = _corner_radius(obj.width)
        outer_outline = _round_outline(outer_outline, radius)

    # Closed source paths may run in either direction. Canonical winding keeps
    # overlapping filled strokes additive under the non-zero fill rule.
    outer_outline = _with_winding(outer_outline, clockwise=True)
    if obj.fill:
        return outer_outline

    if rounded:
        inner_outline = _round_outline(inner_outline, radius)
    inner_outline = _with_winding(inner_outline, clockwise=False)

    # A zero-area bridge lets the existing SVG polygon writer represent the
    # counter. Outline overlap removal later separates both canonical contours.
    outer_index, inner_index = min(
        (
            (outer_index, inner_index)
            for outer_index in range(len(outer_outline))
            for inner_index in range(len(inner_outline))
        ),
        key=lambda indices: (
            outer_outline[indices[0]].x - inner_outline[indices[1]].x
        )
        ** 2
        + (
            outer_outline[indices[0]].y - inner_outline[indices[1]].y
        )
        ** 2,
    )
    outer_outline = _rotate_points(outer_outline, outer_index)
    inner_outline = _rotate_points(inner_outline, inner_index)

    return [
        *outer_outline,
        outer_outline[0],
        *inner_outline,
        inner_outline[0],
    ]


def render_glyph_object(obj: Any, *, rounded: bool = False) -> list[Any]:
    if not isinstance(rounded, bool):
        raise TypeError("rounded must be a boolean")
    if isinstance(obj, GlyphPolygon):
        return _render_polygon(obj, rounded=rounded)

    closed_polygon = _closed_polyline_polygon(obj) if rounded else None
    if closed_polygon is not None:
        return _render_polygon(closed_polygon, rounded=True)

    outline = PRERENDER.render_glyph_object(obj)
    if rounded:
        outline = _round_outline(outline, _corner_radius(obj.width))
    return _with_winding(outline, clockwise=True)


def write_svg(
    polygons: Sequence[Sequence[Any]],
    filename: Path,
    margin: float,
    *,
    advance_width: float = 0,
) -> None:
    """Show the advance cell's side margins without clipping any overhangs."""

    if advance_width <= 0:
        PRERENDER.write_svg(polygons, filename, margin=margin)
        return

    min_x, min_y, max_x, max_y = PRERENDER.calculate_polygon_bounds(polygons)
    min_x = min(0, min_x)
    max_x = max(advance_width, max_x)
    width = max_x - min_x + margin * 2
    height = max_y - min_y + margin * 2
    elements = [
        f'<rect x="0" y="0" width="{width:.4f}" height="{height:.4f}" fill="white"/>'
    ]
    elements.extend(
        PRERENDER.svg_polygon(polygon, min_x, max_y, margin)
        for polygon in polygons
    )
    filename.write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{width:.4f}" height="{height:.4f}" '
        f'viewBox="0 0 {width:.4f} {height:.4f}">\n'
        + "\n".join(elements)
        + "\n</svg>\n",
        encoding="utf-8",
    )
