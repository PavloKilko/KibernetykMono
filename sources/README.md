# Font source

`KibernetykMono.glyphs` is an interoperability export generated from the raw TTFs for Google Fonts review. It contains seven weight masters and exportable instances. This export may be removed in the future.

Kibernetyk Mono is built procedurally in Python using `fontTools` and `fontmake`. For normal font builds, use `python scripts/build_fonts.py`.

Regenerate it from the canonical TTF files:

```sh
python scripts/export_glyphs_source.py
```

Build its seven instances with fontmake:

```sh
fontmake -g sources/KibernetykMono.glyphs -o ttf -i
```
