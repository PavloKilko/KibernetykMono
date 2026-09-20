# Kibernetyk Mono landing page

Static HTML, CSS, and JavaScript, with self-hosted Kibernetyk Mono and Geist Sans.
There is no JavaScript package manager, framework, CDN font, or backend.

## Refresh fonts and downloads

From the repository root, with the font-builder Conda environment active:

    python scripts/build_site.py

This compiles all seven Kibernetyk Mono weights from the current glyph sources,
updates the character index from the Regular TTF, and creates the font ZIP
with its license and author files. It only builds the standard family.
The font names and outlines are unchanged; the website uses a CSS family alias
and file URLs, never an installed local font.

To assemble the site from the canonical release fonts without compiling again:

    python scripts/build_site.py --font-source fonts/ttf

For a quicker preview using only Regular:

    python scripts/build_site.py --regular-only

The generated Kibernetyk copies under docs/assets/fonts are ignored by Git.
The canonical committed binaries are under fonts/ttf.

## Preview locally

Generate the local website assets, then run:

    python -m http.server 8000 --directory docs

Open http://localhost:8000/. Do not add /docs/ to this URL: docs is already
the server's root. You can also open docs/index.html directly in a browser.

## Publish on GitHub Pages

The workflow at .github/workflows/pages.yml publishes the site after pushes to
main or master, and can also be started manually. It copies the static docs
files into a temporary artifact, packages the canonical fonts from fonts/ttf,
and deploys that artifact. The duplicate website TTFs are never committed.

In the repository, open **Settings → Pages** and set **Source** to
**GitHub Actions**. The deployment URL is shown by the workflow's deploy job.

## Page contents

The character browser, weight selector, code samples, and downloads all use the
same built fonts. The glyph count includes unencoded support glyphs (currently
440 total, of which 435 are Unicode-mapped). “Scripts” means Latin and
Cyrillic, not an unverified number of supported languages.

The technical-document specimen demonstrates the font in dense interface
documentation. Its content is fictional and uses only the font's core ASCII
characters.

## Geist Sans

General text uses the self-hosted variable Geist Sans webfont from
https://github.com/vercel/geist-font (fonts/Geist/webfonts/Geist[wght].woff2),
retrieved on 2026-09-20. Its SIL Open Font License is included at
assets/fonts/Geist-OFL.txt.

SHA-256 of assets/fonts/Geist-Variable.woff2:
2ffebe993e969069a9789d15164b7715d42491b5835516c5e3b935d5f81b05f1

