# Reference repositories

Source code and sample code, sorted by how much authority each carries.

The distinction on this page is not pedantry. Three of the most useful
repositories in this ecosystem live under Google-owned GitHub organizations and
state in their own README that they are **not an officially supported Google
product**. They are worth your time. They are not worth your citation.

See the [five tiers](00-official-documentation.md#the-five-tiers) for the full
scale.

## Tier 2 — official

Maintained by Google, no disclaimer. The code is authoritative even when the
README lags.

### SDKs

The unified Google Gen AI SDK is the only recommended way to call Gemini models.
One SDK covers both the Gemini Developer API and the Gemini API on Agent
Platform; you switch backends with a client flag, not a different library.

| Language | Repository | Package |
|---|---|---|
| Python | `googleapis/python-genai` | `google-genai` |
| JavaScript / TypeScript | `googleapis/js-genai` | `@google/genai` |
| Java | `googleapis/java-genai` | — |
| .NET | `googleapis/dotnet-genai` | — |
| Go | `pkg.go.dev/google.golang.org/genai` | — |

### Agent Development Kit

| Repository | What it is |
|---|---|
| `google/adk-python` | ADK for Python. `pip install google-adk`. Apache-2.0, releases roughly every two weeks |
| `google/adk-java` | ADK for Java |
| `google/adk-web` | The development UI: event tracking, tracing, artifacts, evaluations |

### Deprecated, kept for evidence

| Repository | Why it still matters |
|---|---|
| `google-gemini/deprecated-generative-ai-python` | The old Python SDK. Its README states: *"All support for this repository ended permanently on November 30, 2025."* The repository was renamed to carry `deprecated-` in its own name |

That renaming is worth seeing once. It is as blunt as Google gets about the SDK
consolidation, and it is why any tutorial importing `google.generativeai`
should be treated as expired rather than merely old.

## Tier 3 — under Google organizations, not officially supported

All three carry the disclaimer *"Not an officially supported Google product"*.
Use them to learn, to see working code, and to find out what exists. Do not use
them to establish that something is true.

| Repository | What it is | Notes |
|---|---|---|
| `GoogleCloudPlatform/generative-ai` | Notebooks and samples for GenAI on Google Cloud | The largest of the three. Covers agents, search, RAG and grounding, vision, audio, embeddings. Actively maintained |
| `google/adk-samples` | Runnable ADK "recipes" | Python, TypeScript, Go, Java, Kotlin. `core/` holds canonical patterns — OAuth flows, session memory, guardrails, RAG. `contrib/` is community-contributed |
| `Google-Cloud-AI/agent-platform` | Curated index of agent-building resources | Smaller and newer. Linked from the README of `GoogleCloudPlatform/generative-ai`, which lends it credibility it does not claim for itself |

`google/adk-samples` adds a second warning worth repeating: its recipes are
*"for demonstration and as starting points, not production use"*. If you lift
code from it into [`09-projects/`](../09-projects/) work, the error handling,
auth, and resource cleanup are yours to write.

## How to use a repository as a source

**Read the code before the README.** READMEs are marketing surfaces that get
updated on release cadence; code gets updated on merge. When they disagree, the
code is right.

**Deprecated parameters are documented in docstrings, not in guides.** The
hardest evidence of the platform rename is not on any documentation page — it
is in the SDK's own client constructor, where the old flag survives, described
as legacy, alongside the new one. Renames are visible in code long before the
prose catches up.

**Check whether a CLI command matches its product name.** When a product is
renamed, the documentation changes first and the command-line interface changes
last, if ever. A mismatch between the two tells you a rename happened and
roughly how recently.

**Star counts measure popularity, not authority.**

## Related

- [Official documentation](00-official-documentation.md) — the tier system
- [Ecosystem changelog](02-ecosystem-changelog.md) — release feeds to watch
- [`04-development-with-models/`](../04-development-with-models/00-overview.md) — using the SDKs
- [`05-agent-development/`](../05-agent-development/02-google-adk.md) — using ADK

---
_Last verified: 2026-07-28 against the GitHub pages for `googleapis/python-genai`,
`googleapis/js-genai`, `google/adk-python`, `google/adk-samples`,
`GoogleCloudPlatform/generative-ai`, `Google-Cloud-AI/agent-platform`, and
`google-gemini/deprecated-generative-ai-python`._
