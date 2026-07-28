# Nomenclature and renames

Half the difficulty of this ecosystem is not technical. It is that the names
move: products get renamed while their URLs survive, SDKs get replaced while
the old ones keep importing, and every tutorial ever written keeps teaching
whatever things were called on its publication day.

This page is the decoder. It covers the renames that are confirmed, what still
answers to each old name, and how to date any tutorial at a glance.

## Every name has a state

A name in this ecosystem is never just right or wrong. It is in one of three
states, and knowing which changes what you do with it:

- **Current** — what the documentation breadcrumbs say today.
- **Legacy** — superseded but still working: an old flag, an old URL, an old
  subcommand. Safe to encounter, unwise to write.
- **Switched off** — the code path behind the name is gone. Following a
  tutorial built on it does not produce deprecation warnings; it produces
  errors.

The dangerous state is the third one, because nothing about a tutorial's page
tells you its imports died.

## The renames that matter

### Vertex AI → Gemini Enterprise Agent Platform

The platform formerly called Vertex AI is now the **Gemini Enterprise Agent
Platform** — its own documentation shortens it to **Agent Platform**, and its
product page carries "(formerly Vertex AI)" in the title.

What still answers to the old name:

- **Documentation URLs.** Paths under `/vertex-ai/` still resolve, and
  `cloud.google.com/...` documentation links return a `301` to
  `docs.cloud.google.com/...`. Old links keep working, which is exactly why so
  many stale ones are still circulating.
- **The SDK's internals** — see
  [the rename, visible in code](#the-rename-visible-in-code) below.

The exact announcement date is deliberately not stated here; it has not been
confirmed against an official source. The
[ecosystem changelog](../resources/02-ecosystem-changelog.md) records what is
confirmed.

### Agent Engine → Agent Runtime

The managed service for running agents is now **Agent Runtime**. ADK's
documentation uses the new name throughout — and its CLI does not:

```bash
adk deploy agent_engine --project=your-project --region=us-central1 my_agent
```

Product renamed, subcommand not. This is the general pattern in miniature:
marketing changes first, documentation second, command-line surfaces last, if
ever. A name mismatch between a product's docs and its tooling is not a bug in
either — it is a rename caught mid-flight.

### The SDK consolidation

Three libraries used to reach Gemini models. One does now.

| Library | State |
|---|---|
| `google-genai` (Python) · `@google/genai` (JS) — one SDK, five languages | **Current.** GA since May 2025 |
| `google-generativeai` (Python) · `@google/generative-ai` (JS) | **Switched off.** Support ended permanently on 2025-11-30 |
| The generative AI module of the Vertex AI SDK | **Switched off.** Deprecated 2025-06-24, shut down 2026-06-24 |

The second row's Python repository was literally renamed to
`deprecated-generative-ai-python`, and its README states: *"All support for
this repository ended permanently on November 30, 2025."*

The third row is the one that breaks the most tutorials. Reaching Gemini
through `import vertexai` was the standard Google Cloud pattern for years, so a
large fraction of the sample code on the open web now fails — not with a
warning, with an error.

### Gemini CLI → Antigravity CLI

On 2026-06-18, Gemini CLI and the Gemini Code Assist IDE extensions stopped
serving requests **for free users and Google AI Pro and Ultra subscribers**.
The replacement is **Antigravity CLI**, part of the Antigravity development
platform.

The qualifier is the content here: **Gemini Code Assist is not discontinued.**
Organizations on a Standard or Enterprise license keep working access. "Gemini
CLI is dead" and "nothing changed" are both wrong, and which applies to you
depends entirely on your license. See
[developer tools](../11-related-products/03-antigravity-and-developer-tools.md).

## The rename, visible in code

The platform rename is easiest to see not in any documentation page but in the
current SDK's client constructor, which accepts both spellings:

```python
from google import genai

# Current spelling
client = genai.Client(
    enterprise=True, project="your-project", location="us-central1"
)

# Previous spelling — still accepted, documented as "Legacy flag for `enterprise`"
client = genai.Client(
    vertexai=True, project="your-project", location="us-central1"
)
```

The SDK also reads both environment variables, `GOOGLE_GENAI_USE_ENTERPRISE`
and `GOOGLE_GENAI_USE_VERTEXAI`; if they conflict, the newer one wins and the
SDK emits a warning saying so.

This is worth internalizing beyond the specific case: **code is where a rename
stays visible longest.** Prose gets edited in place and loses the history;
working code has to keep both names alive for compatibility, so it shows you
the before and the after at once.

## Dating a tutorial at a glance

| Signal in the tutorial | What it tells you |
|---|---|
| `import google.generativeai` | Expired SDK — support ended 2025-11-30. Do not follow |
| `import vertexai` for model calls | Switched off 2026-06-24. Do not follow |
| `from google import genai` with `vertexai=True` | Current SDK, pre-rename idiom. Works; write `enterprise=True` instead |
| `enterprise=True` | Current |
| Links under `cloud.google.com/vertex-ai/...` | Written before the documentation host moved. Follow the redirect |
| "Vertex AI" in the text, "Agent Platform" in the breadcrumb | A page caught mid-rename. Trust the breadcrumb |
| Instructions to install Gemini CLI | Predates 2026-06-18 — Antigravity CLI now, unless you are on an enterprise license |

## Close names, different things

Renames are one hazard; collisions are the other — live products whose names
are nearly identical. Gemini Enterprise is not the Gemini Enterprise Agent
Platform; Agent Gallery is not Agent Garden; there are three products with
"Studio" in the name. The
[collision table](../resources/02-ecosystem-changelog.md#names-that-are-easy-to-confuse)
lists them side by side, and the
[glossary](../12-glossary/01-equivalences-and-historical-names.md) will hold
the full old-name-to-new-name lookup.

## How this repository writes names

- Names are written as the current documentation breadcrumbs write them.
- The first mention of a renamed product notes the old name once, in
  parentheses, then drops it.
- Factual pages end with a `Last verified` date. Older than about three months
  means recheck before trusting.
- When two official pages disagree on a name, the disagreement is documented,
  not averaged — it almost always means the change is recent and one page has
  not caught up.

---
_Last verified: 2026-07-28 against `docs.cloud.google.com/gemini-enterprise-agent-platform`,
`ai.google.dev/gemini-api/docs/libraries`,
`github.com/google-gemini/deprecated-generative-ai-python`, `adk.dev/deploy/`,
the `googleapis/python-genai` client source, and the Google Developers Blog for
the CLI transition. See [resources](../resources/00-official-documentation.md)._
