#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
project_root="$(dirname "$script_dir")"
output_dir="${1:-$project_root/fonts/ttf}"

mkdir -p "$output_dir"
fontmake -g "$script_dir/KibernetykMono.glyphs" -o ttf -i --output-dir "$output_dir"
