#!/usr/bin/env python3
"""Update module README Media sections for learn_hdl_simulator."""
from __future__ import annotations

import re
from pathlib import Path

MEDIA_BLOCK = """## Media

| Artifact | Path |
|----------|------|
| Transcript | [transcript.md](transcript.md) |
| Outline | [outline.yaml](outline.yaml) |
| Slides | [slides.pptx](slides.pptx) · [slides.pdf](slides.pdf) |
| Video | [video.mp4](video.mp4) |
| Quiz | [quiz.json](quiz.json) |
"""

# Matches "Media (module-slides ready)" stub tables and "Media (planned)"
OLD_MEDIA = re.compile(
    r"## Media(?: \(module-slides ready\)| \(planned\))?\s*\n"
    r"(?:\s*\n)?"
    r"(?:\| Artifact \| Path \|\s*\n"
    r"\|[-| ]+\|\s*\n"
    r"(?:\|[^\n]+\|\s*\n)+)?",
    re.MULTILINE,
)


def main() -> None:
    course = Path(__file__).resolve().parents[1]
    updated = 0
    for readme in sorted(course.glob("module*/README.md")):
        text = readme.read_text(encoding="utf-8")
        original = text
        if "## Media" in text:
            text, n = OLD_MEDIA.subn(MEDIA_BLOCK + "\n", text, count=1)
            if n == 0 and "## Media\n\n| Artifact |" not in text:
                # Already final form or odd shape — force replace after first Media heading block
                pass
        elif readme.parent.name in ("module00-intro", "module10-wrap", "module09-offline-public-sim"):
            # Insert before checklist or at end
            if "## Checklist" in text:
                text = text.replace("## Checklist", MEDIA_BLOCK + "\n## Checklist", 1)
            elif "## Setup" in text:
                # intro: append near end before last section if no media
                text = text.rstrip() + "\n\n" + MEDIA_BLOCK + "\n"
            else:
                text = text.rstrip() + "\n\n" + MEDIA_BLOCK + "\n"
        if text != original:
            readme.write_text(text, encoding="utf-8")
            print(f"OK: {readme.parent.name}")
            updated += 1
        else:
            print(f"skip: {readme.parent.name}")
    print(f"Updated {updated} README(s)")


if __name__ == "__main__":
    main()
