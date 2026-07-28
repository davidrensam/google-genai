#!/usr/bin/env python3
"""Check every relative Markdown link in the repository.

Verifies that the target file exists and, when the link carries a `#fragment`,
that a matching heading exists in that file.

Run it locally the same way CI does:

    python3 .github/scripts/check_links.py

Exits non-zero if anything is broken. External (http/https) links are not
checked here — see the freshness workflow for why that is deliberate.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__"}

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*$")


def markdown_files() -> list[Path]:
    return sorted(
        p
        for p in REPO.rglob("*.md")
        if not any(part in SKIP_DIRS for part in p.parts)
    )


def slug(text: str) -> str:
    """Approximate GitHub's heading-anchor algorithm.

    Two details matter and are easy to get wrong: GitHub keeps underscores,
    and it converts EACH whitespace character to a hyphen without collapsing
    runs — so "Agent Engine → Agent Runtime" (arrow removed, two spaces left)
    becomes "agent-engine--agent-runtime", double hyphen included.
    """
    text = re.sub(r"`|\*", "", text)            # strip inline formatting
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links -> their text
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s", "-", text)


def strip_fences(text: str) -> str:
    """Drop fenced code blocks — a `# comment` inside one is not a heading,
    and a link-looking string inside one is not a link."""
    kept: list[str] = []
    fenced = False
    for line in text.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
            continue
        if not fenced:
            kept.append(line)
    return "\n".join(kept)


def anchors(path: Path) -> set[str]:
    found: set[str] = set()
    for line in strip_fences(path.read_text(encoding="utf-8")).splitlines():
        m = HEADING.match(line)
        if m:
            found.add(slug(m.group(1)))
    return found


def main() -> int:
    problems: list[str] = []
    checked = 0

    for md in markdown_files():
        for link in LINK.findall(strip_fences(md.read_text(encoding="utf-8"))):
            if link.startswith(("http://", "https://", "mailto:")):
                continue
            checked += 1

            target_part, _, fragment = link.partition("#")
            target = (md.parent / target_part).resolve() if target_part else md

            rel = md.relative_to(REPO)
            if not target.exists():
                problems.append(f"{rel}: missing target -> {link}")
                continue
            if fragment and target.suffix == ".md":
                if fragment not in anchors(target):
                    problems.append(f"{rel}: missing anchor -> {link}")

    if problems:
        print(f"{len(problems)} broken link(s) out of {checked} checked:\n")
        for p in problems:
            print(f"  {p}")
        return 1

    print(f"OK — {checked} relative links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
