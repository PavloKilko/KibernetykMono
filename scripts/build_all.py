"""Build release fonts, Glyphs sources, site assets, and preview images."""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys


def main() -> int:
    argparse.ArgumentParser(description=__doc__).parse_args()

    scripts_dir = Path(__file__).resolve().parent
    project_dir = scripts_dir.parent
    font_dir = project_dir / "fonts" / "ttf"
    steps = (
        ("build_fonts.py", ()),
        ("export_glyphs_source.py", ("--font-dir", str(font_dir))),
        ("build_site.py", ()),
        ("generate_preview_images.py", ("--font-source", str(font_dir))),
    )

    for script, arguments in steps:
        print(f"Running {script}", flush=True)
        try:
            subprocess.run(
                [sys.executable, str(scripts_dir / script), *arguments],
                cwd=project_dir,
                check=True,
            )
        except subprocess.CalledProcessError as error:
            print(f"{script} failed with exit code {error.returncode}.", file=sys.stderr)
            return error.returncode

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
