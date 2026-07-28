# Ecosystem changelog

This repository's main risk is not being wrong. It is being right, and then
quietly becoming wrong while nobody notices.

This page is the defense against that. It lists where change is announced, how
to check, and what has already changed. Read it before trusting any other page
here.

## Where change is announced

Four feeds cover the ecosystem. Nothing important lands outside them.

| Feed | URL | Covers |
|---|---|---|
| Gemini API release notes | `ai.google.dev/gemini-api/docs/changelog` | Models, API features, parameter deprecations. History back to December 2023 |
| Agent Platform release notes | `docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes` | The managed platform |
| Agent Platform deprecations | `docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations` | Shutdown dates. The table that actually breaks code |
| ADK releases | GitHub releases on `google/adk-python` | Roughly every two weeks |

The deprecations table is the one to check first. Release notes tell you what
you *could* start using; the deprecations table tells you what has already
stopped working.

## Running a check

Before writing or revising any page:

1. Open the deprecations table. Anything with a shutdown date in the past is no
   longer a warning — it is a break.
2. Scan the two release-notes feeds since the `Last verified` date on the page
   you are about to touch.
3. Confirm the product name in the documentation breadcrumb still matches the
   name used in the page.
4. Update the `Last verified` line, even when nothing changed. A confirmed date
   is information.

Any page whose `Last verified` date is more than about three months old should
be treated as suspect until rechecked.

## Confirmed changes

Chronological, most recent first. For a lookup table of old name to new name,
see [equivalences and historical names](../12-glossary/01-equivalences-and-historical-names.md).

### 2026-07-21 — Sampling parameters deprecated

`temperature`, `top_p`, and `top_k` are deprecated on the Gemini API.

This one is easy to miss and hard to overstate. Effectively every prompting
tutorial written before this date sets at least one of them, which means the
generic advice you will find elsewhere is now teaching a deprecated interface.
Relevant to [prompting](../01-foundations/03-prompting.md) and to
[configuration](../04-development-with-models/04-configuration-errors-retries-and-timeouts.md).

*Source: Gemini API release notes.*

### 2026-07-21 — Gemini 3.6 Flash and 3.5 Flash-Lite reach GA

*Source: Gemini API release notes.*

### 2026-06-24 — Vertex AI SDK generative AI module shut down

Deprecated on 2025-06-24 and shut down exactly one year later. Not a pending
removal — it is gone.

Any tutorial that reaches a Gemini model through `import vertexai` is broken
today, not soon. Because that pattern was standard for years, a large fraction
of the sample code on the open web is now dead. Migration path is the unified
`google-genai` SDK.

*Source: Agent Platform deprecations table.*

### Vertex AI became the Gemini Enterprise Agent Platform

The platform's own documentation now uses **Agent Platform** as the short form,
and `cloud.google.com/products/gemini-enterprise-agent-platform` is the product
page. `GoogleCloudPlatform/generative-ai` describes it as "the latest evolution
of Vertex AI".

Existing services continue to work; this was a consolidation and a rename, not
a migration. The exact announcement date is not yet confirmed against an
official source and is deliberately omitted here.

Two visible consequences:

- **Documentation moved domain.** `cloud.google.com/...` now redirects to
  `docs.cloud.google.com/...` with a `301`. Old links keep working, which is
  why so many of them are still circulating.
- **The SDK carries both names.** The client parameter is now `enterprise`,
  with `vertexai` retained and documented as a legacy flag. Both
  `GOOGLE_GENAI_USE_ENTERPRISE` and `GOOGLE_GENAI_USE_VERTEXAI` are read; when
  they conflict, the newer one wins and the SDK emits a warning.

### Agent Engine became Agent Runtime

ADK documentation consistently uses **Agent Runtime** for the managed service,
and serves it under `adk.dev/deploy/agent-runtime/`.

The CLI has not followed:

```bash
adk deploy agent_engine --project=... --region=... my_agent
```

Product renamed, subcommand not. This is the clearest single illustration of
why this repository exists — and a reminder that when documentation and tooling
disagree about a name, both are telling you the truth about different moments
in time.

### Dialogflow CX console superseded

The Dialogflow CX console is marked as a deprecated user interface, replaced by
the **Conversational Agents console**. Dialogflow CX itself remains active and
separately documented.

Its documentation carries a standing notice that *"some products and features
are in the process of being renamed"* — treat everything in that product area
as in motion.

### 2025-11-30 — Legacy Gemini SDKs end of support

`google-generativeai` (Python) and `@google/generative-ai` (JavaScript) reached
end of support. The Python repository was renamed to
`google-gemini/deprecated-generative-ai-python` and its README states that all
support ended permanently on this date.

### 2025-05 — The unified Gen AI SDK reaches GA

`google-genai` became generally available across Python, JavaScript/TypeScript,
Go, Java, and C#, and is the recommended way to reach Gemini models on both the
Developer API and Agent Platform.

## Names that are easy to confuse

Not changes, but collisions — pairs of live products whose names are close
enough to be mistaken for each other. Full definitions live in the
[glossary](../12-glossary/00-glossary.md).

| These are different things | |
|---|---|
| **Gemini Enterprise** — an intranet search, AI assistant, and agentic platform for knowledge workers | **Gemini Enterprise Agent Platform** — the developer platform, formerly Vertex AI |
| **Agent Gallery** — inside Gemini Enterprise | **Agent Garden** — inside Agent Platform, a library of prebuilt agent samples |
| **Agent Studio** — building agents on Agent Platform | **Google AI Studio** — prototyping against the Gemini Developer API |

Gemini Enterprise and Agent Platform have separate documentation trees, separate
release notes, and separate product pages. Whenever a page here means the
application rather than the platform, it says so explicitly. See
[related products](../11-related-products/00-gemini-enterprise-app.md).

## Open questions

Tracked here so they are not silently forgotten:

- **PaLM API**, **Generative AI Studio**, **Agentspace** — earlier names whose
  current status has not been traced. Third-party sources report that Agentspace
  became Gemini Enterprise, but the official "What is Gemini Enterprise?" page
  does not mention Agentspace at all, so nothing is claimed here yet.
- **Gemini Enterprise for Customer Experience** — a third product carrying the
  Gemini Enterprise name. Relationship to Dialogflow CX unverified.
- **Antigravity** — a development tool referenced by CodeMender's documentation,
  not yet covered here.

## Related

- [Official documentation](00-official-documentation.md)
- [Reference repositories](01-reference-repositories.md)
- [Equivalences and historical names](../12-glossary/01-equivalences-and-historical-names.md)

---
_Last verified: 2026-07-28 against `ai.google.dev/gemini-api/docs/changelog`,
`docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations`,
`docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes`,
`adk.dev/deploy/`, and `docs.cloud.google.com/dialogflow/cx/docs/concept/version`._
