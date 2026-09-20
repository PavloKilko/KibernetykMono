# Font source

`KibernetykMono.glyphs` contains all seven weights as masters and exportable
instances. It includes 440 glyphs, anchors, and the OpenType layout features
used by the Python builder.

Regenerate it from the canonical TTF files:

```sh
python scripts/export_glyphs_source.py
```

Build its seven instances with fontmake:

```sh
fontmake -g sources/KibernetykMono.glyphs -o ttf -i
```
