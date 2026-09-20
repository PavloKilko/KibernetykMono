import ast
import math
import argparse

from pathlib import Path
from dataclasses import dataclass


EPS = 1e-9
BOUNDARY_EPS = 1e-7


# ============================================================
# Geometry
# ============================================================

@dataclass(frozen=True)
class Point:
    x: float
    y: float


@dataclass(frozen=True)
class Line:
    a: Point
    b: Point


@dataclass(frozen=True)
class Dot:
    x: float
    y: float
    w: float

    def topleft(self):
        h = self.w / 2
        return Point(
            self.x - h,
            self.y + h,
        )

    def topright(self):
        h = self.w / 2
        return Point(
            self.x + h,
            self.y + h,
        )

    def bottomright(self):
        h = self.w / 2
        return Point(
            self.x + h,
            self.y - h,
        )

    def bottomleft(self):
        h = self.w / 2
        return Point(
            self.x - h,
            self.y - h,
        )


@dataclass(frozen=True)
class VectorLines:
    top: Line
    bottom: Line


# ============================================================
# Basic helpers
# ============================================================

def add(a, b):
    return Point(
        a.x + b.x,
        a.y + b.y,
    )


def sub(a, b):
    return Point(
        a.x - b.x,
        a.y - b.y,
    )


def mul(a, value):
    return Point(
        a.x * value,
        a.y * value,
    )


def length(a):
    return math.hypot(
        a.x,
        a.y,
    )


def normalize(a):
    l = length(a)

    if l < EPS:
        raise ValueError(
            "Zero-length segment"
        )

    return Point(
        a.x / l,
        a.y / l,
    )


def same_point(a, b):
    return (
        abs(a.x - b.x) < BOUNDARY_EPS
        and
        abs(a.y - b.y) < BOUNDARY_EPS
    )


# ============================================================
# Side lines for one segment
# ============================================================

def calculate_vector_lines(a_dot, b_dot):
    center_direction = normalize(
        Point(
            b_dot.x - a_dot.x,
            b_dot.y - a_dot.y,
        )
    )

    # Left-hand normal
    normal = Point(
        -center_direction.y,
        center_direction.x,
    )

    ah = a_dot.w / 2
    bh = b_dot.w / 2

    a_top = Point(
        a_dot.x + normal.x * ah,
        a_dot.y + normal.y * ah,
    )

    b_top = Point(
        b_dot.x + normal.x * bh,
        b_dot.y + normal.y * bh,
    )

    a_bottom = Point(
        a_dot.x - normal.x * ah,
        a_dot.y - normal.y * ah,
    )

    b_bottom = Point(
        b_dot.x - normal.x * bh,
        b_dot.y - normal.y * bh,
    )

    return VectorLines(
        top=Line(
            a_top,
            b_top,
        ),
        bottom=Line(
            a_bottom,
            b_bottom,
        ),
    )


# ============================================================
# Infinite line intersection
# ============================================================

def intersect_lines(line1, line2):
    x1, y1 = line1.a.x, line1.a.y
    x2, y2 = line1.b.x, line1.b.y

    x3, y3 = line2.a.x, line2.a.y
    x4, y4 = line2.b.x, line2.b.y

    denominator = (
        (x1 - x2) * (y3 - y4)
        -
        (y1 - y2) * (x3 - x4)
    )

    if abs(denominator) < EPS:
        return None

    d1 = (
        x1 * y2
        -
        y1 * x2
    )

    d2 = (
        x3 * y4
        -
        y3 * x4
    )

    x = (
        d1 * (x3 - x4)
        -
        (x1 - x2) * d2
    ) / denominator

    y = (
        d1 * (y3 - y4)
        -
        (y1 - y2) * d2
    ) / denominator

    return Point(
        x,
        y,
    )


# ============================================================
# Square
# ============================================================

def square_bounds(dot):
    h = dot.w / 2

    return (
        dot.x - h,  # xmin
        dot.y - h,  # ymin
        dot.x + h,  # xmax
        dot.y + h,  # ymax
    )


def point_inside_square(point, dot):
    xmin, ymin, xmax, ymax = square_bounds(
        dot
    )

    return (
        xmin - BOUNDARY_EPS
        <= point.x
        <= xmax + BOUNDARY_EPS
        and
        ymin - BOUNDARY_EPS
        <= point.y
        <= ymax + BOUNDARY_EPS
    )


# ============================================================
# Starting from a point inside square, move toward target
# until the square boundary is reached.
# ============================================================

def ray_exit_square(origin, target, dot):
    xmin, ymin, xmax, ymax = square_bounds(
        dot
    )

    dx = target.x - origin.x
    dy = target.y - origin.y

    candidates = []

    # --------------------------------------------------------
    # Vertical square sides
    # --------------------------------------------------------

    if dx > EPS:
        t = (
            xmax - origin.x
        ) / dx

        if t >= -EPS:
            y = origin.y + t * dy

            if (
                ymin - BOUNDARY_EPS
                <= y
                <= ymax + BOUNDARY_EPS
            ):
                candidates.append(
                    (
                        t,
                        Point(
                            xmax,
                            y,
                        ),
                    )
                )

    elif dx < -EPS:
        t = (
            xmin - origin.x
        ) / dx

        if t >= -EPS:
            y = origin.y + t * dy

            if (
                ymin - BOUNDARY_EPS
                <= y
                <= ymax + BOUNDARY_EPS
            ):
                candidates.append(
                    (
                        t,
                        Point(
                            xmin,
                            y,
                        ),
                    )
                )

    # --------------------------------------------------------
    # Horizontal square sides
    # --------------------------------------------------------

    if dy > EPS:
        t = (
            ymax - origin.y
        ) / dy

        if t >= -EPS:
            x = origin.x + t * dx

            if (
                xmin - BOUNDARY_EPS
                <= x
                <= xmax + BOUNDARY_EPS
            ):
                candidates.append(
                    (
                        t,
                        Point(
                            x,
                            ymax,
                        ),
                    )
                )

    elif dy < -EPS:
        t = (
            ymin - origin.y
        ) / dy

        if t >= -EPS:
            x = origin.x + t * dx

            if (
                xmin - BOUNDARY_EPS
                <= x
                <= xmax + BOUNDARY_EPS
            ):
                candidates.append(
                    (
                        t,
                        Point(
                            x,
                            ymin,
                        ),
                    )
                )

    if not candidates:
        raise RuntimeError(
            "Could not find square boundary intersection"
        )

    candidates.sort(
        key=lambda item: item[0]
    )

    return candidates[0][1]


# ============================================================
# Square perimeter representation
#
# Counter-clockwise:
#
#   TL <-------- TR
#   |            ^
#   |            |
#   v            |
#   BL --------> BR
# ============================================================

def square_perimeter_position(point, dot):
    xmin, ymin, xmax, ymax = square_bounds(
        dot
    )

    side = dot.w

    # bottom
    if abs(
        point.y - ymin
    ) < BOUNDARY_EPS:
        return (
            point.x - xmin
        )

    # right
    if abs(
        point.x - xmax
    ) < BOUNDARY_EPS:
        return (
            side
            +
            point.y - ymin
        )

    # top
    if abs(
        point.y - ymax
    ) < BOUNDARY_EPS:
        return (
            side * 2
            +
            xmax - point.x
        )

    # left
    if abs(
        point.x - xmin
    ) < BOUNDARY_EPS:
        return (
            side * 3
            +
            ymax - point.y
        )

    raise ValueError(
        f"Point {point} is not on square boundary"
    )


def square_point_at_perimeter(s, dot):
    xmin, ymin, xmax, ymax = square_bounds(
        dot
    )

    side = dot.w
    perimeter = side * 4

    s %= perimeter

    # bottom
    if s <= side:
        return Point(
            xmin + s,
            ymin,
        )

    # right
    if s <= side * 2:
        return Point(
            xmax,
            ymin + (
                s - side
            ),
        )

    # top
    if s <= side * 3:
        return Point(
            xmax - (
                s - side * 2
            ),
            ymax,
        )

    # left
    return Point(
        xmin,
        ymax - (
            s - side * 3
        ),
    )


# ============================================================
# Travel along square boundary between two points.
# Chooses the shorter perimeter path.
# ============================================================

def square_boundary_path(a, b, dot):
    if same_point(
        a,
        b,
    ):
        return [a]

    side = dot.w
    perimeter = side * 4

    sa = square_perimeter_position(
        a,
        dot,
    )

    sb = square_perimeter_position(
        b,
        dot,
    )

    ccw_distance = (
        sb - sa
    ) % perimeter

    cw_distance = (
        sa - sb
    ) % perimeter

    # --------------------------------------------------------
    # CCW
    # --------------------------------------------------------

    if ccw_distance <= cw_distance:
        result = [a]

        end = (
            sa + ccw_distance
        )

        corner = (
            math.floor(
                sa / side
            )
            +
            1
        ) * side

        while (
            corner
            <
            end - BOUNDARY_EPS
        ):
            result.append(
                square_point_at_perimeter(
                    corner,
                    dot,
                )
            )

            corner += side

        result.append(
            b
        )

        return result

    # --------------------------------------------------------
    # CW
    # --------------------------------------------------------

    result = [a]

    end = (
        sa - cw_distance
    )

    corner = (
        math.ceil(
            sa / side
        )
        -
        1
    ) * side

    if (
        abs(
            corner - sa
        )
        <
        BOUNDARY_EPS
    ):
        corner -= side

    while (
        corner
        >
        end + BOUNDARY_EPS
    ):
        result.append(
            square_point_at_perimeter(
                corner,
                dot,
            )
        )

        corner -= side

    result.append(
        b
    )

    return result


# ============================================================
# Internal join
#
# If offset line intersection is inside middle square:
#     keep exact intersection.
#
# If it is outside:
#     clip incoming + outgoing line to square and walk along
#     square edge between the two intersection points.
# ============================================================

def calculate_clipped_join(
    previous_line,
    next_line,
    dot,
):
    miter = intersect_lines(
        previous_line,
        next_line,
    )

    # --------------------------------------------------------
    # Straight / parallel
    # --------------------------------------------------------

    if miter is None:
        a = previous_line.b
        b = next_line.a

        return [
            Point(
                (
                    a.x + b.x
                ) / 2,
                (
                    a.y + b.y
                ) / 2,
            )
        ]

    # --------------------------------------------------------
    # Exact miter is inside square
    # --------------------------------------------------------

    if point_inside_square(
        miter,
        dot,
    ):
        return [
            miter
        ]

    # --------------------------------------------------------
    # Miter outside square: clip both lines
    # --------------------------------------------------------

    incoming_origin = (
        previous_line.b
    )

    outgoing_origin = (
        next_line.a
    )

    incoming_hit = ray_exit_square(
        incoming_origin,
        miter,
        dot,
    )

    outgoing_hit = ray_exit_square(
        outgoing_origin,
        miter,
        dot,
    )

    return square_boundary_path(
        incoming_hit,
        outgoing_hit,
        dot,
    )


# ============================================================
# Endpoint caps
# ============================================================

def calculate_start_cap(
    segment_lines,
    dot,
):
    top_line = (
        segment_lines.top
    )

    bottom_line = (
        segment_lines.bottom
    )

    # Extend backwards from first point
    top_target = Point(
        top_line.a.x
        +
        (
            top_line.a.x
            -
            top_line.b.x
        ),

        top_line.a.y
        +
        (
            top_line.a.y
            -
            top_line.b.y
        ),
    )

    bottom_target = Point(
        bottom_line.a.x
        +
        (
            bottom_line.a.x
            -
            bottom_line.b.x
        ),

        bottom_line.a.y
        +
        (
            bottom_line.a.y
            -
            bottom_line.b.y
        ),
    )

    top_hit = ray_exit_square(
        top_line.a,
        top_target,
        dot,
    )

    bottom_hit = ray_exit_square(
        bottom_line.a,
        bottom_target,
        dot,
    )

    # bottom -> top
    return square_boundary_path(
        bottom_hit,
        top_hit,
        dot,
    )


def calculate_end_cap(
    segment_lines,
    dot,
):
    top_line = (
        segment_lines.top
    )

    bottom_line = (
        segment_lines.bottom
    )

    # Extend forward beyond last point
    top_target = Point(
        top_line.b.x
        +
        (
            top_line.b.x
            -
            top_line.a.x
        ),

        top_line.b.y
        +
        (
            top_line.b.y
            -
            top_line.a.y
        ),
    )

    bottom_target = Point(
        bottom_line.b.x
        +
        (
            bottom_line.b.x
            -
            bottom_line.a.x
        ),

        bottom_line.b.y
        +
        (
            bottom_line.b.y
            -
            bottom_line.a.y
        ),
    )

    top_hit = ray_exit_square(
        top_line.b,
        top_target,
        dot,
    )

    bottom_hit = ray_exit_square(
        bottom_line.b,
        bottom_target,
        dot,
    )

    # top -> bottom
    return square_boundary_path(
        top_hit,
        bottom_hit,
        dot,
    )


# ============================================================
# Remove duplicate consecutive points
# ============================================================

def dedupe(points):
    if not points:
        return []

    output = [
        points[0]
    ]

    for point in points[1:]:
        if not same_point(
            point,
            output[-1],
        ):
            output.append(
                point
            )

    if (
        len(output) > 1
        and
        same_point(
            output[0],
            output[-1],
        )
    ):
        output.pop()

    return output


# ============================================================
# FINAL POLYLINE
#
# Works for:
#
#   2 dots
#   3 dots
#   4 dots
#   ...
#
# Returns one polygon.
# ============================================================

def render_polyline(dots):
    if len(dots) < 2:
        raise ValueError(
            "Polyline requires at least 2 dots"
        )

    # --------------------------------------------------------
    # Offset lines for every segment
    # --------------------------------------------------------

    segments = []

    for i in range(
        len(dots) - 1
    ):
        segments.append(
            calculate_vector_lines(
                dots[i],
                dots[i + 1],
            )
        )

    # ========================================================
    # TOP / LEFT outline
    # ========================================================

    top_outline = []

    start_cap = calculate_start_cap(
        segments[0],
        dots[0],
    )

    end_cap = calculate_end_cap(
        segments[-1],
        dots[-1],
    )

    top_outline.append(
        start_cap[-1]
    )

    # --------------------------------------------------------
    # Internal top joins
    # --------------------------------------------------------

    for i in range(
        1,
        len(dots) - 1,
    ):
        previous_line = (
            segments[i - 1].top
        )

        next_line = (
            segments[i].top
        )

        join = calculate_clipped_join(
            previous_line,
            next_line,
            dots[i],
        )

        top_outline.extend(
            join
        )

    top_outline.append(
        end_cap[0]
    )

    # ========================================================
    # BOTTOM / RIGHT outline
    # ========================================================

    bottom_outline = []

    bottom_outline.append(
        start_cap[0]
    )

    for i in range(
        1,
        len(dots) - 1,
    ):
        previous_line = (
            segments[i - 1].bottom
        )

        next_line = (
            segments[i].bottom
        )

        join = calculate_clipped_join(
            previous_line,
            next_line,
            dots[i],
        )

        bottom_outline.extend(
            join
        )

    bottom_outline.append(
        end_cap[-1]
    )

    # ========================================================
    # One final contour
    # ========================================================

    polygon = []

    polygon.extend(
        top_outline
    )

    polygon.extend(
        end_cap[1:]
    )

    reversed_bottom = list(
        reversed(
            bottom_outline
        )
    )

    polygon.extend(
        reversed_bottom[1:]
    )

    polygon.extend(
        start_cap[1:]
    )

    return dedupe(
        polygon
    )


# ============================================================
# Single dot
# ============================================================

def render_dot(dot):
    return [
        dot.topleft(),
        dot.topright(),
        dot.bottomright(),
        dot.bottomleft(),
    ]


# ============================================================
# .glyph AST representation
# ============================================================

@dataclass(frozen=True)
class GlyphDot:
    width: float
    point: tuple


@dataclass(frozen=True)
class GlyphLine:
    width: float
    a: tuple
    b: tuple


@dataclass(frozen=True)
class GlyphPolyline:
    width: float
    points: tuple


# ============================================================
# AST parser helpers
# ============================================================

def parse_number(
    value,
    line_number,
):
    # bool is subclass of int, so reject it explicitly
    if (
        isinstance(
            value,
            bool,
        )
        or
        not isinstance(
            value,
            (int, float),
        )
    ):
        raise ValueError(
            f"Line {line_number}: "
            f"expected a number, got {value!r}"
        )

    value = float(
        value
    )

    if not math.isfinite(
        value
    ):
        raise ValueError(
            f"Line {line_number}: "
            f"number must be finite"
        )

    return value


def parse_width(
    value,
    line_number,
):
    width = parse_number(
        value,
        line_number,
    )

    if width <= 0:
        raise ValueError(
            f"Line {line_number}: "
            f"width must be > 0"
        )

    return width


def parse_point(
    value,
    line_number,
):
    if (
        not isinstance(
            value,
            (tuple, list),
        )
        or
        len(value) != 2
    ):
        raise ValueError(
            f"Line {line_number}: "
            f"expected point (x, y), "
            f"got {value!r}"
        )

    x = parse_number(
        value[0],
        line_number,
    )

    y = parse_number(
        value[1],
        line_number,
    )

    return (
        x,
        y,
    )


def parse_point_list(
    value,
    line_number,
):
    if not isinstance(
        value,
        (tuple, list),
    ):
        raise ValueError(
            f"Line {line_number}: "
            f"polyline points must be a list"
        )

    if len(value) < 2:
        raise ValueError(
            f"Line {line_number}: "
            f"polyline requires at least 2 points"
        )

    points = tuple(
        parse_point(
            point,
            line_number,
        )
        for point in value
    )

    # Reject zero-length consecutive segments.
    for i in range(
        len(points) - 1
    ):
        if points[i] == points[i + 1]:
            raise ValueError(
                f"Line {line_number}: "
                f"points {i} and {i + 1} are identical"
            )

    return points


# ============================================================
# Parse one .glyph source line
#
# Supported:
#
# dot(w, (x, y))
#
# line(
#     w,
#     (x1, y1),
#     (x2, y2)
# )
#
# polyline(
#     w,
#     [(x1, y1), (x2, y2), ...]
# )
#
# But syntax must physically remain on ONE line.
# ============================================================

def parse_glyph_line(
    source,
    line_number,
):
    try:
        expression = ast.parse(
            source,
            mode="eval",
        )
    except SyntaxError as exc:
        raise ValueError(
            f"Line {line_number}: "
            f"invalid syntax:\n"
            f"    {source}"
        ) from exc

    node = expression.body

    if not isinstance(
        node,
        ast.Call,
    ):
        raise ValueError(
            f"Line {line_number}: "
            f"expected dot(...), line(...) "
            f"or polyline(...)"
        )

    # Only plain names:
    #
    # dot(...)
    #
    # Not:
    #
    # object.dot(...)
    #
    if not isinstance(
        node.func,
        ast.Name,
    ):
        raise ValueError(
            f"Line {line_number}: "
            f"invalid command"
        )

    command = (
        node.func.id
    )

    if node.keywords:
        raise ValueError(
            f"Line {line_number}: "
            f"keyword arguments are not supported"
        )

    # --------------------------------------------------------
    # Safely turn each AST expression into literals.
    #
    # ast.literal_eval DOES NOT execute arbitrary Python.
    # --------------------------------------------------------

    try:
        args = [
            ast.literal_eval(
                argument
            )
            for argument in node.args
        ]
    except (
        ValueError,
        SyntaxError,
    ) as exc:
        raise ValueError(
            f"Line {line_number}: "
            f"arguments may contain only "
            f"numbers, tuples and lists"
        ) from exc

    # ========================================================
    # dot(w, (x, y))
    # ========================================================

    if command == "dot":
        if len(args) != 2:
            raise ValueError(
                f"Line {line_number}: "
                f"expected:\n"
                f"    dot(w, (x, y))"
            )

        width = parse_width(
            args[0],
            line_number,
        )

        point = parse_point(
            args[1],
            line_number,
        )

        return GlyphDot(
            width=width,
            point=point,
        )

    # ========================================================
    # line(w, (x1, y1), (x2, y2))
    # ========================================================

    if command == "line":
        if len(args) != 3:
            raise ValueError(
                f"Line {line_number}: "
                f"expected:\n"
                f"    line(w, (x1, y1), (x2, y2))"
            )

        width = parse_width(
            args[0],
            line_number,
        )

        a = parse_point(
            args[1],
            line_number,
        )

        b = parse_point(
            args[2],
            line_number,
        )

        if a == b:
            raise ValueError(
                f"Line {line_number}: "
                f"line endpoints cannot be identical"
            )

        return GlyphLine(
            width=width,
            a=a,
            b=b,
        )

    # ========================================================
    # polyline(w, [(x1, y1), ...])
    # ========================================================

    if command == "polyline":
        if len(args) != 2:
            raise ValueError(
                f"Line {line_number}: "
                f"expected:\n"
                f"    polyline(w, [(x1, y1), ...])"
            )

        width = parse_width(
            args[0],
            line_number,
        )

        points = parse_point_list(
            args[1],
            line_number,
        )

        return GlyphPolyline(
            width=width,
            points=points,
        )

    raise ValueError(
        f"Line {line_number}: "
        f"unknown command {command!r}"
    )


# ============================================================
# Read complete .glyph file
#
# One expression per physical line.
#
# Empty lines allowed.
# # comments allowed.
# ============================================================

def read_glyph_file(
    filename,
):
    objects = []

    with open(
        filename,
        "r",
        encoding="utf-8",
    ) as file:
        for (
            line_number,
            raw_line,
        ) in enumerate(
            file,
            start=1,
        ):
            # Strip comments
            source = raw_line.split(
                "#",
                1,
            )[0].strip()

            # Ignore blank lines
            if not source:
                continue

            obj = parse_glyph_line(
                source,
                line_number,
            )

            objects.append(
                obj
            )

    if not objects:
        raise ValueError(
            f"{filename}: file contains no glyph objects"
        )

    return objects


# ============================================================
# Parsed primitive -> final polygon
# ============================================================

def render_glyph_object(
    obj,
):
    # --------------------------------------------------------
    # dot
    # --------------------------------------------------------

    if isinstance(
        obj,
        GlyphDot,
    ):
        x, y = obj.point

        return render_dot(
            Dot(
                x=x,
                y=y,
                w=obj.width,
            )
        )

    # --------------------------------------------------------
    # line
    #
    # A line is just a 2-point polyline.
    # --------------------------------------------------------

    if isinstance(
        obj,
        GlyphLine,
    ):
        x1, y1 = obj.a
        x2, y2 = obj.b

        dots = [
            Dot(
                x=x1,
                y=y1,
                w=obj.width,
            ),
            Dot(
                x=x2,
                y=y2,
                w=obj.width,
            ),
        ]

        return render_polyline(
            dots
        )

    # --------------------------------------------------------
    # polyline
    # --------------------------------------------------------

    if isinstance(
        obj,
        GlyphPolyline,
    ):
        dots = [
            Dot(
                x=x,
                y=y,
                w=obj.width,
            )
            for x, y in obj.points
        ]

        return render_polyline(
            dots
        )

    raise TypeError(
        f"Unsupported glyph object: {obj!r}"
    )


# ============================================================
# Render entire .glyph file
# ============================================================

def render_glyph_file(
    filename,
):
    objects = read_glyph_file(
        filename
    )

    polygons = []

    for obj in objects:
        polygon = render_glyph_object(
            obj
        )

        polygons.append(
            polygon
        )

    return polygons


# ============================================================
# SVG
# ============================================================

def calculate_polygon_bounds(
    polygons,
):
    points = [
        point
        for polygon in polygons
        for point in polygon
    ]

    if not points:
        raise ValueError(
            "Nothing to render"
        )

    min_x = min(
        p.x
        for p in points
    )

    max_x = max(
        p.x
        for p in points
    )

    min_y = min(
        p.y
        for p in points
    )

    max_y = max(
        p.y
        for p in points
    )

    return (
        min_x,
        min_y,
        max_x,
        max_y,
    )


def svg_polygon(
    points,
    min_x,
    max_y,
    margin,
):
    # Cartesian:
    #
    #     +Y up
    #
    # SVG:
    #
    #     +Y down
    #
    # Also shift everything so negative source coordinates
    # work correctly.

    converted = [
        Point(
            point.x
            -
            min_x
            +
            margin,

            max_y
            -
            point.y
            +
            margin,
        )
        for point in points
    ]

    coordinates = " ".join(
        f"{point.x:.4f},{point.y:.4f}"
        for point in converted
    )

    return (
        f'<polygon '
        f'points="{coordinates}" '
        f'fill="black" '
        f'/>'
    )


def write_svg(
    polygons,
    filename,
    margin=50,
):
    (
        min_x,
        min_y,
        max_x,
        max_y,
    ) = calculate_polygon_bounds(
        polygons
    )

    width = (
        max_x
        -
        min_x
        +
        margin * 2
    )

    height = (
        max_y
        -
        min_y
        +
        margin * 2
    )

    elements = [
        (
            f'<rect '
            f'x="0" '
            f'y="0" '
            f'width="{width:.4f}" '
            f'height="{height:.4f}" '
            f'fill="white" '
            f'/>'
        )
    ]

    for polygon in polygons:
        elements.append(
            svg_polygon(
                polygon,
                min_x,
                max_y,
                margin,
            )
        )

    svg = f"""<svg
    xmlns="http://www.w3.org/2000/svg"
    width="{width:.4f}"
    height="{height:.4f}"
    viewBox="0 0 {width:.4f} {height:.4f}">
    {"".join(elements)}
</svg>
"""

    with open(
        filename,
        "w",
        encoding="utf-8",
    ) as file:
        file.write(
            svg
        )

    return (
        width,
        height,
    )


# ============================================================
# CLI
#
# Usage:
#
#     python render.py example.glyph
#
# or:
#
#     python render.py example.glyph output.svg
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Render .glyph geometry into SVG"
        )
    )

    parser.add_argument(
        "input",
        help="Input .glyph file",
    )

    parser.add_argument(
        "output",
        nargs="?",
        help=(
            "Output SVG file. "
            "Defaults to input filename with .svg extension."
        ),
    )

    parser.add_argument(
        "--margin",
        type=float,
        default=50,
        help="SVG margin (default: 50)",
    )

    args = parser.parse_args()

    input_path = Path(
        args.input
    )

    if args.output:
        output_path = Path(
            args.output
        )
    else:
        output_path = (
            input_path.with_suffix(
                ".svg"
            )
        )

    polygons = render_glyph_file(
        input_path
    )

    width, height = write_svg(
        polygons,
        output_path,
        margin=args.margin,
    )

    print(
        f"Read:   {input_path}"
    )

    print(
        f"Shapes: {len(polygons)}"
    )

    print(
        f"SVG:    {output_path}"
    )

    print(
        f"Size:   {width:.2f} x {height:.2f}"
    )


if __name__ == "__main__":
    main()