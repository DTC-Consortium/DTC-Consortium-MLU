#!/usr/bin/env bash
# Export the deck to PDF through PowerPoint, which ships the template's Aptos fonts.
# (LibreOffice renders it too, but substitutes the fonts.)
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
IN="$HERE/assessment-lifecycle-deck.pptx"
OUT="$HERE/assessment-lifecycle-deck.pdf"

# The words on these 28 slides are legal-approved. The standing permission is that copy may be
# REMOVED from them — never added, never reworded. verify_deck.py proves that mechanically
# against approved-deck-baseline.txt, so the gate here is a real check rather than a promise.
# It replaced an --i-have-legal-approval flag, which only recorded that someone had asserted it.
# PowerPoint writes its in-memory copy back over the .pptx when it closes, which silently
# reverts whatever build_deck.py last wrote. That happened once: two deletions on slide 2
# disappeared between the build and the export, and the only signal was the deletion count
# dropping from 8 to 6 in a line nobody reads closely. Rebuild if the source is newer.
if [ "$HERE/build_deck.py" -nt "$IN" ]; then
  echo "build_deck.py is newer than $(basename "$IN") — rebuilding first."
  echo "(PowerPoint may have written an older copy back when it closed.)"
  python3 "$HERE/build_deck.py" || exit 1
fi

echo "Checking the deck is subtractive against the approved baseline..."
if ! python3 "$HERE/verify_deck.py" --pptx "$IN"; then
  cat >&2 <<'WARN'

Refusing to export: the .pptx adds or rewords copy on legal-approved slides.

Remove the additions listed above, or clear them with legal and re-baseline deliberately.
Read DECK-APPROVAL.md first.
WARN
  exit 1
fi

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

# Verify what actually came out, not just what went in. A PDF check also catches the slide-28
# case that a .pptx check cannot see (its text lives in the template layout).
echo
echo "Verifying the exported PDF..."
python3 "$HERE/verify_deck.py" --pdf "$OUT"

# The attendee copy must stay identical to the presenter copy.
cp "$OUT" "$HERE/participant-resources/assessment-lifecycle-deck.pdf"
echo "Synced participant-resources/$(basename "$OUT")"
echo
echo "New md5 (record it in DECK-APPROVAL.md):"
md5 -q "$OUT" "$HERE/participant-resources/$(basename "$OUT")"
echo
echo "Next: python3 build_pack.py"
