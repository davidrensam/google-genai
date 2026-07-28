# Equivalences and historical names

You found an old name. This page tells you what it is now, and whether the old
one still works.

Arrows here mean one thing: **B replaced A, for everybody.** If a name's state
depends on your licence, your billing tier, or which access path you took, it is
not a rename and it does not get an arrow — those live in
[not a rename](#not-renames-conditional-states) at the bottom.

## Products

| Old name | Current name | Does the old one still work? |
|---|---|---|
| Vertex AI | Gemini Enterprise Agent Platform ("Agent Platform") | Documentation URLs yes, the brand no |
| Agent Engine | Agent Runtime | Yes — the ADK CLI subcommand is still `agent_engine` |
| Dialogflow CX console | Conversational Agents console | Dialogflow CX itself remains a live product |
| TensorFlow Lite | LiteRT | Renamed 2024-09-04 |
| `ai-edge-torch` | LiteRT Torch | **Undocumented rename.** No announcement, no date — detected only because the GitHub repository silently resolves to the new name |

## Libraries

| Old | Current | State |
|---|---|---|
| `google-generativeai` (Python) | `google-genai` | **Switched off** — support ended 2025-11-30 |
| `@google/generative-ai` (JS) | `@google/genai` | **Switched off** — same date |
| Generative AI module of the Vertex AI SDK (`import vertexai`) | `google-genai` | **Switched off** — deprecated 2025-06-24, shut down 2026-06-24 |

All three now fail rather than warn. A tutorial built on any of them is not
outdated, it is broken.

## Code and configuration

| Old spelling | Current spelling | Still accepted? |
|---|---|---|
| `vertexai=True` | `enterprise=True` | Yes — documented as *"Legacy flag for `enterprise`"* |
| `GOOGLE_GENAI_USE_VERTEXAI` | `GOOGLE_GENAI_USE_ENTERPRISE` | Yes — both are read; on conflict the newer wins and the SDK warns |

The SDK keeping both spellings alive is the clearest evidence of the platform
rename that exists anywhere — see
[the rename, visible in code](../00-orientation/01-nomenclature-and-renames.md#the-rename-visible-in-code).

## URLs

Every one of these still resolves, which is exactly why stale links survive.

| Old URL | Redirects to |
|---|---|
| `cloud.google.com/vertex-ai/...` (documentation) | `docs.cloud.google.com/vertex-ai/...` |
| `ai.google.dev/gemma` | `deepmind.google/models/gemma` |
| `ai.google.dev/edge` | `developers.google.com/edge` |
| `ai.google.dev/gemini-api/docs/quickstart` | `ai.google.dev/gemini-api/docs/get-started` |

The `ai.google.dev/edge` move is worth more than a redirect. Google AI Edge was
physically separated from the Gemini API developer site while
`/gemini-api/docs` stayed — a structural statement about what belongs to which
stack, made entirely through URLs and never announced.

## Not renames: conditional states

These look like renames and are not. Both sides are live; which one applies
depends on the reader.

| Name | Why it has no single answer |
|---|---|
| **Gemini CLI** | Stopped serving free, AI Pro and AI Ultra users on 2026-06-18, who move to Antigravity CLI. Still shipped with Gemini Code Assist Standard and Enterprise licences. Simultaneously current and retired, by licence |
| **`generateContent`** | Not deprecated, no shutdown date, officially *"remains fully supported"* — but the Interactions API is now what the documentation recommends for new development |
| **Gemma on the Gemini API** | Available on the free tier only, and absent from both the models catalog and the rate-limits page |

Full treatment in
[nomenclature and renames](../00-orientation/01-nomenclature-and-renames.md).

## Close but different

Not history — collisions between products that all exist right now. The table
lives in the [glossary](00-glossary.md#names-that-are-easy-to-confuse), because a
collision is not a change.

## Unresolved

Named here so they are not mistaken for settled.

| Name | Status |
|---|---|
| **Agentspace** | Third-party sources report it became Gemini Enterprise. The official *"What is Gemini Enterprise?"* page does not mention Agentspace at all, so nothing is claimed here |
| **PaLM API** | Superseded by the Gemini API; the transition has not been traced against an official source |
| **Generative AI Studio** | Current status untraced |
| **Model Garden** | A Vertex AI-era name whose survival past the rename is unverified |
| **Gemini Enterprise for CX vs. Dialogflow CX** | Both live, documented separately, and neither page references the other. Whether one succeeds the other is unresolved |

Empty rows are not an oversight. A guide about renames that guesses at renames
is worse than one that admits the gap.

## How to use this page

**Trust the breadcrumb over the prose.** When a documentation page's navigation
and its body text disagree on a name, the navigation is regenerated on publish
and the prose is edited by hand. The navigation is newer.

**Check whether the tooling agrees with the product.** `adk deploy agent_engine`
under documentation that says Agent Runtime is not a bug in either — it dates
the rename.

**Old URL working is not evidence the old name is current.** Every redirect in
the table above still resolves.

---
_Last verified: 2026-07-28 against `docs.cloud.google.com/gemini-enterprise-agent-platform`,
`ai.google.dev/gemini-api/docs`, `github.com/google-gemini/deprecated-generative-ai-python`,
`adk.dev/deploy/`, `deepmind.google/models/gemma`, `developers.google.com/edge`,
the `googleapis/python-genai` client source, and the Google Developers Blog for
the CLI transition. See [resources](../resources/00-official-documentation.md)._
