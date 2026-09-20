# Kibernetyk Mono

Kibernetyk Mono is a geometric monospace typeface inspired by the pioneering
spirit of the Ukrainian Cybernetics School. Its rigid, pared-back letterforms
recall early mainframe interfaces and the ink-stamped texture of fax
transmissions. It is drawn from points and lines for clean code, dense data,
and the infrastructure that holds them together.

## Build

Create and activate the Conda environment:

```sh
conda env create -f environment.yml
conda activate font-builder
```

Build the regular TTF:

```sh
python -m kibernetyk_mono_font_builder build
```

The font is written to `build/regular/KibernetykMono-Regular.ttf`. To build a
different weight, pass `--weight` with one of `thin`, `extralight`, `light`,
`regular`, `medium`, `semibold`, or `bold`.
