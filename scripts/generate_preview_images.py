"""Generate the social card and README specimen from the shipped TTFs."""

from __future__ import annotations

import json
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = ROOT / "fonts" / "ttf"
BACKGROUND = "#fcf7eb"
INK = "#000000"
ACCENTS = ("#e2393e", "#f8841e", "#fec029", "#5ab73f", "#0096d5")


@dataclass
class OutlineFont:
    path: Path

    def __post_init__(self) -> None:
        self.font = TTFont(self.path)
        self.glyphs = self.font.getGlyphSet()
        self.cmap = self.font.getBestCmap()
        self.metrics = self.font["hmtx"].metrics
        self.units_per_em = self.font["head"].unitsPerEm

    def text(self, value: str, x: float, baseline: float, size: float) -> str:
        scale = size / self.units_per_em
        paths: list[str] = []
        cursor = x

        for character in value:
            glyph_name = self.cmap.get(ord(character), ".notdef")
            pen = SVGPathPen(self.glyphs)
            self.glyphs[glyph_name].draw(pen)
            commands = pen.getCommands()
            if commands:
                paths.append(
                    f'<path d="{commands}" '
                    f'transform="translate({cursor:.3f} {baseline:.3f}) '
                    f'scale({scale:.6f} {-scale:.6f})" fill="{INK}"/>'
                )
            cursor += self.metrics[glyph_name][0] * scale

        return "".join(paths)

    def text_width(self, value: str, size: float) -> float:
        scale = size / self.units_per_em
        return sum(
            self.metrics[self.cmap.get(ord(character), ".notdef")][0] * scale
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
    ]
    return svg_document(1200, 630, "".join(parts))


def readme_preview(fonts: dict[str, OutlineFont]) -> str:
    regular = fonts["Regular"]
    bold = fonts["Bold"]
    coverage = "440 glyphs - Latin and Cyrillic core, combining marks, and symbols"
    coverage_size = 30
    coverage_x = (1600 - regular.text_width(coverage, coverage_size)) / 2
    parts = [
        regular.text("Kibernetyk", 60, 215, 200),
        regular.text("Mono", 60, 480, 200),
        color_tape(660, 305, 880, 175),
        regular.text(coverage, coverage_x, 600, coverage_size),
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

    parts.append(bold.text("7 Weights", 60, 1430, 58))
    pangram = "Cyber wizards pack my box with five dozen electric liquor jugs."
    weights = {
        "Thin": 100,
        "ExtraLight": 200,
        "Light": 300,
        "Regular": 400,
        "Medium": 500,
        "SemiBold": 600,
        "Bold": 700,
    }
    for index, (name, weight) in enumerate(weights.items()):
        baseline = 1520 + index * 68
        font = fonts[name]
        font_size = 26
        parts.append(font.text(f"{name} ({weight})", 60, baseline, font_size))
        parts.append(font.text(pangram, 400, baseline, font_size))

    return svg_document(1600, 2030, "".join(parts))

def main() -> None:
    names = ("Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold")
    fonts = {
        name: OutlineFont(FONT_DIR / f"KibernetykMono-{name}.ttf")
        for name in names
    }
    try:
        write_png(
            social_preview(fonts["Regular"]),
            ROOT / "docs" / "assets" / "site-preview.png",
        )
        write_png(
            readme_preview(fonts),
            ROOT / "assets" / "readme-preview.png",
        )
    finally:
        for font in fonts.values():
            font.close()


if __name__ == "__main__":
    main()
