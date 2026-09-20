"""Command-line interface for the modular font builder."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

from .compiler import build_ttf
from .config import (
    FAMILY_NAME,
    ROUNDED_FAMILY_NAME,
    WEIGHT_STYLE_NAMES,
    WEIGHT_WIDTHS,
)
from .preview import render_previews


def _parse_arguments(arguments: Sequence[str] | None) -> argparse.Namespace:
    # Import lazily so core modules remain reusable with other glyph registries.
    from kibernetyk_mono_font_builder.glyphs import GLYPH_REGISTRY

    parser = argparse.ArgumentParser(
        description="Render Kibernetyk Mono glyphs and compile a TrueType TTF."
    )
    parser.add_argument(
        "action",
        nargs="?",
        default="all",
        choices=("render", "build", "all"),
        help="render SVGs, build a TTF, or do both (default: all)",
    )
    parser.add_argument(
        "--weight",
        default="regular",
        choices=tuple(WEIGHT_WIDTHS),
    )
    parser.add_argument(
        "--rounded",
        action="store_true",
        help="round outline corners and build the Rounded family",
    )

    selection = parser.add_mutually_exclusive_group()
    selection.add_argument(
        "--glyph",
        dest="glyphs",
        action="append",
        choices=tuple(GLYPH_REGISTRY),
        help=(
            "build only this glyph; repeat to combine glyphs "
            "(default: all registered groups)"
        ),
    )
    selection.add_argument(
        "--group",
        dest="groups",
        action="append",
        choices=GLYPH_REGISTRY.group_names,
        help="build only this glyph group; repeat to combine groups",
    )
    parser.add_argument(
        "--list-groups",
        action="store_true",
        help="list registered glyph groups and exit",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="destination root (default: build or build-rounded)",
    )
    parser.add_argument(
        "--margin",
        type=float,
        default=50,
        help="SVG preview margin (default: 50)",
    )
    return parser.parse_args(arguments)


def main(arguments: Sequence[str] | None = None) -> int:
    from kibernetyk_mono_font_builder.glyphs import GLYPH_REGISTRY

    options = _parse_arguments(arguments)
    if options.list_groups:
        for group_name, group in GLYPH_REGISTRY.groups.items():
            selectors = " ".join(repr(selector) for selector in group.builders)
            print(f"{group_name}: {selectors}")
        return 0

    glyphs = GLYPH_REGISTRY.build(
        WEIGHT_WIDTHS[options.weight],
        names=options.glyphs,
        group_names=options.groups,
    )
    for glyph in glyphs:
        glyph.rounded = options.rounded

    output_directory = options.output_dir or Path(
        "build-rounded" if options.rounded else "build"
    )
    weight_directory = output_directory / options.weight

    if options.action in {"render", "all"}:
        for output in render_previews(
            glyphs,
            weight_directory / "svg",
            margin=options.margin,
        ):
            print(f"SVG: {output}")

    if options.action in {"build", "all"}:
        family_name = ROUNDED_FAMILY_NAME if options.rounded else FAMILY_NAME
        file_stem = family_name.replace(" ", "")
        style_name = WEIGHT_STYLE_NAMES[options.weight]
        output = weight_directory / f"{file_stem}-{style_name}.ttf"
        print(
            f"TTF: {build_ttf(glyphs, output, options.weight, options.rounded)}"
        )

    return 0
