"""Session facts that more than one build script needs.

Kept in one place because the folder link is stamped into the deck, the take-home pack, and the
printed handout. Three copies of a URL is three chances for one of them to be stale on the day.

After changing DRIVE_URL, rebuild everything and re-print the handout:

    python3 build_deck.py && ./export_pdf.sh && python3 build_pack.py
"""

# The shared folder every attendee scans into. It holds the four build prompts, the sample pack,
# the course reading, and the handout — see prompts/DRIVE-FOLDER.md for the required layout.
#
# Must be readable by "anyone with the link" WITHOUT a Google sign-in. Attendees are already
# signing into Amazon Quick in the first twelve minutes; a second sign-in wall here costs the
# session its opening. Check this in an incognito window before every delivery.
# The "?usp=sharing" suffix Google appends is analytics only — the folder opens without it —
# and it is 13 characters that push the QR code into a denser version, which costs real
# scanning distance in a big room. Dropped deliberately; do not paste it back in.
DRIVE_URL = "https://drive.google.com/drive/folders/10aipzDJD_Hpn8lVpa8eorBTFFeYjVn3D"

# This delivery. From the 2026 AWS-MLU AI Teaching & Research Symposium Know Before You Go.
EVENT = "2026 AWS-MLU AI Teaching & Research Symposium"
EVENT_DATE = "Monday, September 21, 2026"
VENUE = "Howard University · Armour J. Blackburn Center, Washington, DC"
ROOM = "Blackburn Ballroom — Educators Consortium (Faculty) track"
SLOT = "1:30 – 3:00 PM"          # 90 minutes exactly; straight after lunch (12:30 – 1:30)

# The sign-up link the Know Before You Go sent every attendee. Quick is free. Keep the campaign
# parameter — it is how AWS attributes symposium sign-ups, and this is the approved form.
QUICK_SIGNUP = "quick.aws.com/sn?utm_campaign=mlu2026"

# Shown under the QR code for anyone who cannot scan — a phone with no camera access, a back row
# too far from the screen, someone joining remotely. Keep it short enough to retype by hand.
# A Drive folder id is not retypable, so this should be a redirect you control.
DRIVE_SHORTLINK = "«FILL IN: a short, typable redirect to the folder — e.g. dsu.edu/lifecycle»"
