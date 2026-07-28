#!/usr/bin/env python3
"""Report pages whose `Last verified` date has gone stale, or is missing.

This repository's main risk is not being wrong — it is being right and then
quietly becoming wrong while nobody notices. Every page making factual claims
carries a `Last verified: YYYY-MM-DD` line; this script is what stops those
dates from becoming decoration.

Run it locally:

    python3 .github/scripts/check_freshness.py            # human-readable
    python3 .github/scripts/check_freshness.py --markdown # for an issue body

Always exits 0. Staleness is a prompt to recheck, not a build failure — a page
does not stop being correct on the day it turns three months old.
"""

from __future__ import annotations

import argparse
import re
from datetime import date, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__", ".github"}

# Files that make no factual claims about the ecosystem and need no date.
EXEMPT = {"README.md", "CONTRIBUTING.md"}

STALE_AFTER_DAYS = 90
MARKER = re.compile(r"Last verified:\s*(\d{4}-\d{2}-\d{2})")


def content_pages() -> list[Path]:
    pages = []
    for p in sorted(REPO.rglob("*.md")):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if p.parent == REPO and p.name in EXEMPT:
            continue
        if p.stat().st_size == 0:  # scaffold placeholder, not yet written
            continue
        pages.append(p)
    return pages


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--markdown", action="store_true")
    ap.add_argument("--days", type=int, default=STALE_AFTER_DAYS)
    args = ap.parse_args()

    today = date.today()
    stale: list[tuple[Path, date, int]] = []
    missing: list[Path] = []

    for page in content_pages():
        m = MARKER.search(page.read_text(encoding="utf-8"))
        if not m:
            missing.append(page)
            continue
        try:
            verified = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        except ValueError:
            # A typo'd date (2026-13-01) must not crash a never-fails check;
            # report the page as needing a date instead.
            missing.append(page)
            continue
        age = (today - verified).days
        if age > args.days:
            stale.append((page, verified, age))

    stale.sort(key=lambda row: row[2], reverse=True)

    if args.markdown:
        if not stale and not missing:
            print(f"All pages verified within the last {args.days} days.")
            return 0
        if stale:
            print(f"### Pages to recheck ({args.days}+ days old)\n")
            print("| Page | Last verified | Days |")
            print("|---|---|---|")
            for page, verified, age in stale:
                print(f"| `{page.relative_to(REPO)}` | {verified} | {age} |")
            print()
        if missing:
            print("### Pages with no `Last verified` line\n")
            for page in missing:
                print(f"- `{page.relative_to(REPO)}`")
            print()
        print(
            "Rechecking means: confirm the product names still match the "
            "documentation breadcrumbs, scan the feeds listed in "
            "`resources/02-ecosystem-changelog.md`, then update the date — "
            "**even if nothing changed**. A confirmed date is information."
        )
        return 0

    if not stale and not missing:
        print(f"OK — all pages verified within the last {args.days} days.")
        return 0
    for page, verified, age in stale:
        print(f"STALE   {page.relative_to(REPO)}  ({verified}, {age} days)")
    for page in missing:
        print(f"NO DATE {page.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
