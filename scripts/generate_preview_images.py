"""Generate outlined social and README specimens from the current glyph sources.

Run from the repository root: python scripts/generate_preview_images.py
Use --font-source PATH to render an existing seven-weight TTF family instead.
The source build is temporary and never replaces the release fonts.
The social card is PNG; the README specimen is a font-independent SVG.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from kibernetyk_mono_font_builder import build_ttf, render_glyphs
from kibernetyk_mono_font_builder.core.config import WEIGHT_WIDTHS

BACKGROUND = "#fcf7eb"
INK = "#000000"
ACCENTS = ("#e2393e", "#f8841e", "#fec029", "#5ab73f", "#0096d5")
WEIGHTS = {
    "Thin": ("thin", 100),
    "ExtraLight": ("extralight", 200),
    "Light": ("light", 300),
    "Regular": ("regular", 400),
    "Medium": ("medium", 500),
    "SemiBold": ("semibold", 600),
    "Bold": ("bold", 700),
}
README_PREVIEW = ROOT / "assets" / "readme-preview.svg"


@dataclass
class OutlineFont:
    path: Path

    def __post_init__(self) -> None:
        self.font = TTFont(self.path)
        self.glyphs = self.font.getGlyphSet()
        self.cmap = self.font.getBestCmap()
        self.metrics = self.font["hmtx"].metrics
        self.units_per_em = self.font["head"].unitsPerEm

    def glyph_name(self, character: str) -> str:
        try:
            return self.cmap[ord(character)]
        except KeyError:
            raise ValueError(
                f"{self.path.name} is missing U+{ord(character):04X} "
                f"({character!r}). Rebuild the fonts with the current glyph sources."
            ) from None

    def text(
        self, value: str, x: float, baseline: float, size: float,
        *, color: str = INK,
    ) -> str:
        scale = size / self.units_per_em
        paths: list[str] = []
        cursor = x

        for character in value:
            glyph_name = self.glyph_name(character)
            pen = SVGPathPen(self.glyphs)
            self.glyphs[glyph_name].draw(pen)
            commands = pen.getCommands()
            if commands:
                paths.append(
                    f'<path d="{commands}" '
                    f'transform="translate({cursor:.3f} {baseline:.3f}) '
                    f'scale({scale:.6f} {-scale:.6f})" fill="{color}"/>'
                )
            cursor += self.metrics[glyph_name][0] * scale

        return "".join(paths)

    def text_width(self, value: str, size: float) -> float:
        scale = size / self.units_per_em
        return sum(
            self.metrics[self.glyph_name(character)][0] * scale
            for character in value
        )

    def shaped_text(self, value: str, x: float, baseline: float, size: float) -> str:
        result = subprocess.run(
            ["hb-shape", "--output-format=json", str(self.path), value],
            check=True,
            capture_output=True,
            text=True,
        )
        scale = size / self.units_per_em
        paths: list[str] = []
        cursor = x

        for item in json.loads(result.stdout):
            glyph_name = item["g"]
            pen = SVGPathPen(self.glyphs)
            self.glyphs[glyph_name].draw(pen)
            commands = pen.getCommands()
            if commands:
                glyph_x = cursor + item["dx"] * scale
                glyph_y = baseline - item["dy"] * scale
                paths.append(
                    f'<path d="{commands}" '
                    f'transform="translate({glyph_x:.3f} {glyph_y:.3f}) '
                    f'scale({scale:.6f} {-scale:.6f})" fill="{INK}"/>'
                )
            cursor += item["ax"] * scale

        return "".join(paths)

    def close(self) -> None:
        self.font.close()


def svg_document(width: int, height: int, content: str) -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8"?>'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
        f'height="{height}" viewBox="0 0 {width} {height}">'
        f'<rect width="{width}" height="{height}" fill="{BACKGROUND}"/>'
        f"{content}</svg>"
    )


def color_tape(x: int, y: int, width: int, height: int) -> str:
    segment = width / len(ACCENTS)
    return "".join(
        f'<rect x="{x + index * segment:.2f}" y="{y}" '
        f'width="{segment + 0.5:.2f}" height="{height}" fill="{color}"/>'
        for index, color in enumerate(ACCENTS)
    )


def text_block(
    font: OutlineFont,
    lines: tuple[str, ...],
    x: float,
    top: float,
    size: float,
    *,
    color: str = INK,
) -> str:
    """Keep box and block glyphs on contiguous 720-by-1200-unit cells."""
    return "".join(
        font.text(line, x, top + size + index * size * 1.2, size, color=color)
        for index, line in enumerate(lines)
    )


def facts_panel(font: OutlineFont, x: float, top: float, width: float) -> str:
    widths = (28, 28, 30)
    labels = (
        f"{len(font.font.getGlyphOrder())} GLYPHS",
        f"{len(WEIGHTS)} WEIGHTS",
        "LATIN + CYRILLIC CORE",
    )
    lines = (
        "┌" + "┬".join("─" * width for width in widths) + "┐",
        "│" + "│".join(" " * columns for columns in widths) + "│",
        "└" + "┴".join("─" * width for width in widths) + "┘",
    )
    size = width / font.text_width(lines[0], 1)
    cell_width = font.text_width(" ", size)
    label_size = size * 1.4
    cap_height = font.font["OS/2"].sCapHeight / font.units_per_em
    baseline = top + size * 1.8 + cap_height * label_size / 2
    parts = [text_block(font, lines, x, top, size)]
    cursor = x + cell_width
    for label, columns in zip(labels, widths):
        center = cursor + columns * cell_width / 2
        label_x = center - font.text_width(label, label_size) / 2
        parts.append(font.text(label, label_x, baseline, label_size))
        cursor += (columns + 1) * cell_width
    return "".join(parts)


def write_svg(svg: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(svg, encoding="utf-8")


def write_png(svg: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="kibernetyk-preview-") as directory:
        source = Path(directory) / "preview.svg"
        source.write_text(svg, encoding="utf-8")
        subprocess.run(
            ["sips", "-s", "format", "png", str(source), "--out", str(destination)],
            check=True,
        )


def social_preview(regular: OutlineFont) -> str:
    parts = [
        regular.text("Kibernetyk", 60, 240, 150),
        regular.text("Mono", 60, 485, 150),
        color_tape(510, 335, 630, 150),
        facts_panel(regular, 60, 545, 1080),
    ]
    return svg_document(1200, 630, "".join(parts))


def graphics_specimen() -> tuple[str, ...]:
    """Actual font characters, not SVG rules or a second drawing system."""
    diagram = (
        "┌" + "─" * 22 + "┐" + " " * 10 + "╔" + "═" * 22 + "╗" + " " * 10 + "┌" + "─" * 22 + "┐",
        "│" + "INPUT".center(22) + "│" + " " * 10 + "║" + "PROCESSOR".center(22) + "║" + " " * 10 + "│" + "OUTPUT".center(22) + "│",
        "│" + "01001101".center(22) + "├" + "─" * 10 + "╢" + "READY".center(22) + "╟" + "─" * 10 + "┤" + "10110010".center(22) + "│",
        "│" + "packets / stdin".center(22) + "│" + " " * 10 + "║" + "parse + validate".center(22) + "║" + " " * 10 + "│" + "files / stdout".center(22) + "│",
        "└" + "─" * 22 + "┘" + " " * 10 + "╚" + "═" * 22 + "╝" + " " * 10 + "└" + "─" * 22 + "┘",
    )
    widths = (28, 28, 32)
    bands = (
        "┌" + "┬".join("─" * width for width in widths) + "┐",
        "│" + "│".join(
            (f"{density}% " + character * 20).center(width)
            for density, character, width in zip((25, 50, 75), "░▒▓", widths)
        ) + "│",
        "├" + "┴".join("─" * width for width in widths) + "┤",
        "│" + (" HISTORY  " + "▁▂▃▄▅▆▇█▇▆▅▄▃▂▁▂▃▄▅▆▇█▇▆▅▄▃▂▁" * 2).ljust(90) + "│",
        "└" + "─" * 90 + "┘",
    )
    return (*diagram, "", *bands)


def readme_preview(fonts: dict[str, OutlineFont]) -> str:
    regular = fonts["Regular"]
    bold = fonts["Bold"]
    parts = [
        regular.text("Kibernetyk", 60, 215, 200),
        regular.text("Mono", 60, 480, 200),
        color_tape(660, 305, 880, 175),
        facts_panel(regular, 60, 550, 1480),
        bold.text("Regular (400)", 60, 715, 58),
    ]

    glyph_lines = (
        (False, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        (False, "abcdefghijklmnopqrstuvwxyz"),
        (False, "0123456789  ! \" # $ % & ' ( ) * + , - . /"),
        (False, ": ; < = > ? @ [ \\ ] ^ _ ` { | } ~"),
        (False, "АБВГҐДЕЄЁЖЗИІЇЙКЛМНОПРСТУЎФХЦЧШЩЪЫЬЭЮЯ"),
        (False, "абвгґдеєёжзиіїйклмнопрстуўфхцчшщъыьэюя"),
        (True, "a\u0300 a\u0301 a\u0302 a\u0303 a\u0304 a\u030C a\u0307 a\u0308 a\u030A a\u030B a\u0306 a\u0327 a\u0326 a\u0328"),
    )
    for index, (shaped, line) in enumerate(glyph_lines):
        renderer = regular.shaped_text if shaped else regular.text
        parts.append(renderer(line, 60, 810 + index * 72, 48))

    parts.append(bold.text("Box drawing + block elements", 60, 1400, 58))
    parts.append(text_block(regular, graphics_specimen(), 64, 1450, 200 / 9))

    parts.append(bold.text("7 Weights", 60, 1850, 58))
    pangram = "Cyber wizards pack my box with five dozen electric liquor jugs."
    for index, (name, (_, weight)) in enumerate(WEIGHTS.items()):
        baseline = 1940 + index * 68
        font = fonts[name]
        font_size = 26
        parts.append(font.text(f"{name} ({weight})", 60, baseline, font_size))
        parts.append(font.text(pangram, 400, baseline, font_size))

    return svg_document(1600, 2440, "".join(parts))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--font-source", type=Path,
        help="Directory containing an existing seven-weight Kibernetyk Mono TTF family",
    )
    options = parser.parse_args()

    with tempfile.TemporaryDirectory(prefix="kibernetyk-preview-fonts-") as directory:
        font_dir = options.font_source
        if font_dir is None:
            font_dir = Path(directory)
            for name, (weight, _) in WEIGHTS.items():
                glyphs = render_glyphs(WEIGHT_WIDTHS[weight], rounded=False)
                build_ttf(
                    glyphs, font_dir / f"KibernetykMono-{name}.ttf", weight,
                    rounded=False,
                )
        fonts: dict[str, OutlineFont] = {}
        try:
            for name in WEIGHTS:
                fonts[name] = OutlineFont(font_dir / f"KibernetykMono-{name}.ttf")
            # Validate both documents before replacing either preview image.
            social = social_preview(fonts["Regular"])
            readme = readme_preview(fonts)
            write_png(social, ROOT / "docs" / "assets" / "site-preview.png")
            write_svg(readme, README_PREVIEW)
        finally:
            for font in fonts.values():
                font.close()


if __name__ == "__main__":
    main()
