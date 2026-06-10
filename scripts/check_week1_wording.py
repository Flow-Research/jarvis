#!/usr/bin/env python3
"""Reject wording that drifts away from the Jarvis protocol boundary."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
FILES = [*ROOT.glob("*.md"), *ROOT.joinpath("docs").rglob("*.md")]
NORMATIVE_TERMS = {"MUST", "MUST NOT", "SHOULD", "SHOULD NOT", "MAY"}

PATTERNS = [
    r"personal agent harness",
    r"Garden POC active work",
    r"schema-first contract",
    r"demo-first plan",
    r"host owns Jarvis",
    r"Jarvis owns auth",
    r"Jarvis owns runtime",
    r"Jarvis owns database",
    r"Jarvis owns cloud",
    r"Jarvis owns product UI",
    r"\bmaybe\b",
    r"\bprobably\b",
    r"\bcould\b",
    r"\bshould\b",
    r"\bcan\b",
    r"\bwould\b",
    r"\bmight\b",
    r"\brecommend\b",
    r"\brecommended\b",
    r"\bconsider\b",
    r"\bsuggest\b",
    r"\badvice\b",
    r"\bcandidate\b",
    r"implementation concerns",
    r"those are implementation concerns",
    r"if accepted",
    r"if this is approved",
]


def main() -> int:
    compiled = [re.compile(pattern, re.IGNORECASE) for pattern in PATTERNS]
    failures: list[tuple[Path, int, str]] = []

    for path in sorted(FILES):
        text = path.read_text(encoding="utf-8")
        in_code_block = False
        for line_number, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue
            if path.name == "check_week1_wording.py":
                continue
            if any(f"`{term}`" in line for term in NORMATIVE_TERMS):
                continue
            for pattern in compiled:
                if pattern.search(line):
                    failures.append((path.relative_to(ROOT), line_number, line))
                    break

    if failures:
        for path, line_number, line in failures:
            print(f"{path}:{line_number}: rejected wording: {line}")
        return 1

    print("week1 wording ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
