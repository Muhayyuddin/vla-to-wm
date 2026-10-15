#!/usr/bin/env bash
# Regenerate every standalone TikZ figure; run from any working directory.
# Requires pdflatex plus the standalone, IEEEtran, TikZ, and AMS packages.
set -euo pipefail

tkz_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
project_dir="$(dirname -- "$tkz_dir")"
build_dir="$project_dir/build/tkz"
mkdir -p "$build_dir" "$project_dir/figures"

for source in "$tkz_dir"/*.tex; do
    name="$(basename -- "$source" .tex)"
    if ! pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
        -output-directory="$build_dir" "$source" > "$build_dir/$name.stdout.log" 2>&1; then
        cat "$build_dir/$name.stdout.log" >&2
        exit 1
    fi
    cp -- "$build_dir/$name.pdf" "$project_dir/figures/$name.pdf"
    printf 'Built figures/%s.pdf\n' "$name"
done
