"""Build the seven raw TTFs and a versioned release ZIP, independently of the site.

Run manually from the repository root: python scripts/build_fonts.py
Fonts go to fonts/ttf; the archive goes to dist/KibernetykMono-vVERSION.zip.
Release and OpenType versions come from core/config.py. This script is not
called by GitHub Actions and does not modify the site or editable Glyphs source.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import sys
from tempfile import TemporaryDirectory
from zipfile import ZIP_DEFLATED, ZipFile

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT))

from kibernetyk_mono_font_builder import build_ttf, render_glyphs
from kibernetyk_mono_font_builder.core.config import (
    FONT_FILE_STEM,
    FONT_METADATA,
    RELEASE_VERSION,
    VERSION,
    WEIGHT_STYLE_NAMES,
    WEIGHT_WIDTHS,
)

WEIGHTS = ("thin", "extralight", "light", "regular", "medium", "semibold", "bold")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path, default=PROJECT / "fonts" / "ttf",
        help="Destination for the seven raw TTFs (default: fonts/ttf)",
    )
    parser.add_argument(
        "--archive-dir", type=Path, default=PROJECT / "dist",
        help="Destination for the versioned ZIP (default: dist)",
    )
    options = parser.parse_args()
    release = f"v{RELEASE_VERSION}"
    archive_name = f"{FONT_FILE_STEM}-{release}.zip"

    # Finish all compilation and packaging before updating any release outputs.
    with TemporaryDirectory(prefix="kibernetyk-release-") as temporary:
        staging = Path(temporary)
        fonts = []
        for weight in WEIGHTS:
            filename = f"{FONT_FILE_STEM}-{WEIGHT_STYLE_NAMES[weight]}.ttf"
            glyphs = render_glyphs(WEIGHT_WIDTHS[weight], rounded=False)
            fonts.append(build_ttf(glyphs, staging / filename, weight, rounded=False))

        staged_archive = staging / archive_name
        with ZipFile(staged_archive, "w", ZIP_DEFLATED) as bundle:
            for font in fonts:
                bundle.write(font, f"{FONT_FILE_STEM}/{font.name}")
            bundle.write(PROJECT / "OFL.txt", f"{FONT_FILE_STEM}/OFL.txt")
            bundle.writestr(
                f"{FONT_FILE_STEM}/README.txt",
                f"Kibernetyk Mono {release}\n"
                f"OpenType version: {VERSION}\n"
                f"Designed by {FONT_METADATA['designer']}.\n\n"
                "Seven static weights: Thin, ExtraLight, Light, Regular, Medium, "
                "SemiBold, and Bold.\n\n"
                "Install the TTF files using your operating system's font manager.\n"
                "Select Kibernetyk Mono in your editor.\n\n"
                f"Source: {FONT_METADATA['vendorURL']}\n"
                "Licensed under the SIL Open Font License 1.1. See OFL.txt.\n",
            )

        options.output.mkdir(parents=True, exist_ok=True)
        options.archive_dir.mkdir(parents=True, exist_ok=True)
        for font in fonts:
            destination = options.output / font.name
            shutil.copyfile(font, destination)
            print(f"Font: {destination}")
        archive = options.archive_dir / archive_name
        shutil.copyfile(staged_archive, archive)
        print(f"Release: {release} / OpenType {VERSION}")
        print(f"Archive: {archive}")


if __name__ == "__main__":
    main()
