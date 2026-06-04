#!/usr/bin/env python3
"""Validate local Markdown links in the Jarvis repository."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
EXTERNAL_PREFIXES = ("http://", "https://", "#", "mailto:")


def markdown_files() -> list[Path]:
    files = list(ROOT.glob("*.md"))
    files.extend(ROOT.joinpath("docs").rglob("*.md"))
    return sorted(files)


def main() -> int:
    failures: list[tuple[Path, str]] = []

    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(1)
            if target.startswith(EXTERNAL_PREFIXES):
                continue

            clean = target.split("#", 1)[0]
            if not clean:
                continue

            resolved = (path.parent / clean).resolve()
            if not resolved.exists():
                failures.append((path.relative_to(ROOT), target))

    if failures:
        for path, target in failures:
            print(f"{path}: broken local link: {target}")
        return 1

    print("markdown links ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
