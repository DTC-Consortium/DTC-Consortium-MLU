#!/usr/bin/env bash
# Copy the sample pack into this workspace, at the paths the Kiro prompts refer to.
# Run once before the session:  ./seed.sh
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/../activities/sample-pack"
mkdir -p "$HERE/data/papers"
cp "$SRC/rubric-golden.json"               "$HERE/data/rubric.json"
cp "$SRC/roster.csv"                       "$HERE/data/roster.csv"
cp "$SRC/persona2_cs_data_structures.pdf"  "$HERE/data/course-reading.pdf"
cp "$SRC"/papers/*.txt                     "$HERE/data/papers/"
echo "Seeded $HERE/data — now open this folder in Kiro."
