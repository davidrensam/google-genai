# Contributing

The most valuable contribution to this repository is telling it that it is
wrong.

Google renames products, moves documentation, and retires SDKs faster than any
one person can track. A guide to a moving ecosystem decays by default, and the
thing that keeps it honest is people arriving with "this changed."

## What helps most

**A correction with a source.** You found a name, a link, or a claim that no
longer matches Google's documentation. Open an issue with the page here, what it
says, and a link to the current official source. This is the highest-value
contribution and it takes two minutes.

**A gap you hit.** You went looking for something that should be here and was
not. Say what you were trying to do — the missing page matters less than the
question that sent you looking.

**A sample that does not run.** Every code sample is meant to run as-is with
nothing but an API key in the environment. If one does not, that is a bug, and
the error message is enough of a report.

**A page that is confidently unclear.** If a page reads fine but leaves you
unsure what to actually do, that is worth reporting even without a fix.

## Before you write a page

Read [the conventions section of the README](README.md#conventions) first. Three
rules matter more than the rest:

**Cite tier 1 or tier 2 sources.** The
[source hierarchy](resources/00-official-documentation.md#the-five-tiers) is not
decoration. Official documentation and official repository code are citable;
repositories that disclaim official support are worth reading and must be
labelled unofficial when linked; blogs are for dating a change, never for
establishing behaviour.

**Never transcribe volatile data.** Prices, quotas, rate limits, region lists,
per-model availability — link them, do not copy them. They change without notice,
and a guide that is confidently wrong is worse than no guide. Explain how to read
the page and what the numbers imply; leave the numbers on Google's side.

**One concept, one home.** Several topics legitimately appear in more than one
module. Each is explained once, in its canonical home, and the other pages link
to it and add only what is specific to their context. If you are about to explain
something a second time, link instead. The axis is documented in
[the ecosystem map](00-orientation/00-ecosystem-map.md).

## Page requirements

- File names are `NN-kebab-case.md`. The number encodes reading order, not
  hierarchy.
- Any page making factual claims ends with a `Last verified: YYYY-MM-DD` line
  and the sources it was checked against.
- Internal links are relative.
- Write in English, in the present tense, addressing the reader directly. No
  marketing. If something is confusing or badly designed, say so.
- If you cannot verify a claim against an official source, do not make it. Mark
  the gap instead — there are several such marks in this repository on purpose,
  and they are more useful than a confident guess.

## Naming

Write product names the way the current documentation *breadcrumbs* write them,
not the way the body prose does — navigation is regenerated on publish and the
prose is edited by hand, so the breadcrumb is newer.

When you mention a renamed product for the first time on a page, note the old
name once in parentheses, then drop it. Renames themselves belong in
[the glossary](12-glossary/01-equivalences-and-historical-names.md), and a rename
is only a rename when the new name replaced the old one **for everybody** — if
it depends on the reader's licence or billing tier, it is a conditional state and
it is documented differently.

## Running the code

```bash
uv sync
```

Python 3.12+, managed with [uv](https://docs.astral.sh/uv/). Code lives next to
the module that explains it, not in a separate examples tree.

Never commit an API key, and never write one into a sample — not even a
plausible-looking fake.

## Automated checks

Two run for you, both standard library only:

```bash
python3 .github/scripts/check_links.py      # relative links and anchors
python3 .github/scripts/check_freshness.py  # Last verified dates
```

The link check runs on every push and pull request, and fails the build — a
broken internal link is a mechanical error with no judgement involved.

The freshness check runs weekly and never fails anything. It opens a single
tracking issue listing pages whose `Last verified` date has passed ninety days,
and closes it when they are all current again. Staleness is a prompt to
recheck, not a defect: a page does not stop being correct on the day it turns
three months old.

External links are deliberately not checked automatically. Google's pages
redirect constantly and serve 403s to bots, so the check would cry wolf often
enough to be ignored — which is worse than not having it.

## Pull requests

Commits follow [Conventional Commits](https://www.conventionalcommits.org/):
`docs(orientation): ...`, `fix: ...`, `chore: ...`.

Small and single-purpose beats large and comprehensive. A pull request that
corrects one stale name is easier to verify — and therefore more likely to be
merged quickly — than one that reorganises a module.

For anything structural, open an issue first. The module layout encodes
decisions that are not always obvious from the file tree, and it is better to
disagree about them before the work than after.

## Scope

This repository is a map of Google's GenAI ecosystem: what each piece is, how the
pieces relate, which one you need, and what things used to be called.

It is **not** a replacement for Google's documentation, a Python tutorial, an API
reference, or a price catalogue. Contributions that duplicate Google's own pages
will be declined, however well written — the value here is in the mapping, not
the restatement.

## License

Contributions are accepted under the [MIT License](LICENSE).
