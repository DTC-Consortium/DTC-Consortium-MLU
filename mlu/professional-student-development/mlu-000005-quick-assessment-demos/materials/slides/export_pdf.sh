#!/usr/bin/env bash
# Export the deck to PDF through PowerPoint, which ships the template's Aptos fonts.
# (LibreOffice renders it too, but substitutes the fonts.)
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
IN="$HERE/assessment-lifecycle-deck.pptx"
OUT="$HERE/assessment-lifecycle-deck.pdf"

# If the deck is already open, PowerPoint's `open` returns the copy in memory rather than
# re-reading the rebuilt file, and the PDF silently comes out stale. Stop instead of
# closing it, which could discard edits made in PowerPoint.
OPEN=$(osascript -e 'tell application "System Events" to (name of processes) contains "Microsoft PowerPoint"' 2>/dev/null)
if [ "$OPEN" = "true" ] && osascript -e 'tell application "Microsoft PowerPoint" to get name of every presentation' 2>/dev/null \
    | grep -q "$(basename "$IN")"; then
  echo "$(basename "$IN") is open in PowerPoint — save or close it there, then re-run." >&2
  exit 1
fi

osascript <<OSA
tell application "Microsoft PowerPoint"
  open (POSIX file "$IN")
  set thePres to active presentation
  save thePres in (POSIX file "$OUT") as save as PDF
  close thePres saving no
end tell
OSA
echo "Saved $(basename "$OUT")"
