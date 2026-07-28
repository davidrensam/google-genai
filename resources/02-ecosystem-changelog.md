# Ecosystem changelog

This repository's main risk is not being wrong. It is being right, and then
quietly becoming wrong while nobody notices.

This page is the defense against that. It lists where change is announced, how
to check, and what has already changed. Read it before trusting any other page
here.

## Where change is announced

Five feeds cover the stack this repository maps. Related products keep feeds of
their own — Gemini Enterprise has
[separate release notes](00-official-documentation.md#gemini-enterprise).

| Feed | URL | Covers |
|---|---|---|
| Gemini API release notes | `ai.google.dev/gemini-api/docs/changelog` | Models, API features, parameter deprecations. History back to December 2023 |
| Gemini API migration pages | `ai.google.dev/gemini-api/docs/migrate-to-interactions` · `.../interactions-breaking-changes-may-2026` | Surface changes that never appear in release notes |
| Agent Platform release notes | `docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes` | The managed platform |
| Agent Platform deprecations | `docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations` | Shutdown dates. The table that actually breaks code |
| ADK releases | GitHub releases on `google/adk-python` | Roughly every two weeks |

The deprecations table is the one to check first. Release notes tell you what
you *could* start using; the deprecations table tells you what has already
stopped working.

The second row exists because of a gap this page had to learn the hard way. The
Interactions API became the recommended way to call a Gemini model without ever
appearing in a release-notes entry or a deprecations table — it arrived as
standalone documentation pages. **A change that deprecates nothing can still
displace everything**, and no feed built around deprecation will catch it.

## Running a check

Before writing or revising any page:

1. Open the deprecations table. Anything with a shutdown date in the past is no
   longer a warning — it is a break.
2. Scan the two release-notes feeds since the `Last verified` date on the page
   you are about to touch — then check the migration pages, which the feeds do
   not cover.
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
[configuration](../04-development-with-models/05-configuration-errors-retries-and-timeouts.md).

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

### 2026-06-18 — Gemini CLI and the Code Assist IDE extensions stopped serving requests

On this date, Gemini CLI and the Gemini Code Assist IDE extensions stopped
serving requests **for free users and Google AI Pro and Ultra subscribers**.
The replacement is **Antigravity CLI**, which carries over Agent Skills, Hooks,
Subagents, and Extensions — the last renamed to Antigravity plugins.

The qualifier matters, and most secondary coverage drops it: **Gemini Code
Assist is not discontinued.** Organizations on a Gemini Code Assist Standard or
Enterprise license keep working access, with continued access to current Gemini
models. What ended was the consumer tier of those two surfaces.

Getting this distinction wrong in either direction is easy — "Gemini CLI is
dead" and "nothing changed" are both wrong, and which one applies depends
entirely on the reader's license. See
[developer tools](../11-related-products/03-code-assistance-and-developer-tools.md).

*Source: Google Developers Blog.*

### 2026-03-31 — Gemma 4, and a licence change

Gemma 4 is released under **Apache 2.0**. Gemma 1 through 3 shipped under the
custom, non-OSI "Gemma Terms of Use", which carried a prohibited-use policy and
a clause allowing Google to restrict usage remotely.

This splits a claim that used to be simple. "Gemma is not open source, Google
calls them open models" was correct for years and is now only half true —
Google's own Gemma 4 announcement writes *"This open-source license provides a
foundation for complete developer flexibility"*, while the family is still
branded "open models" everywhere else. The branding did not change; the licence
did, and only from version 4.

Any statement about Gemma licensing has to name a generation.

### The Interactions API became the recommended call surface

`ai.google.dev/gemini-api/docs` now teaches `client.interactions.create()` in
place of `client.models.generate_content()`, and there are dedicated *"Migrate
to Interactions API"* and *"Interactions breaking changes"* pages.

`generateContent` is **not deprecated** — the official wording is that it
*"remains fully supported"*, and no shutdown date exists. This is a
recommendation moving, not an API dying, and it is this repository's worked
example of something
[supported but no longer recommended](../00-orientation/01-nomenclature-and-renames.md#every-name-has-a-state).

Undated on purpose: the shift is plain in the documentation, but no announcement
fixing a date has been verified.

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

A collision between two live products is not a change, so this page does not
track them. The side-by-side table lives in the
[glossary](../12-glossary/00-glossary.md#names-that-are-easy-to-confuse).

Worth knowing while reading the entries below: Gemini Enterprise and the Gemini
Enterprise Agent Platform are **different products**, with separate
documentation trees, separate release notes, and separate product pages. Where a
page here means the application rather than the platform, it says so.

## Open questions

Tracked here so they are not silently forgotten:

- **PaLM API**, **Generative AI Studio**, **Agentspace** — earlier names whose
  current status has not been traced. Third-party sources report that Agentspace
  became Gemini Enterprise, but the official "What is Gemini Enterprise?" page
  does not mention Agentspace at all, so nothing is claimed here yet.
- **Gemini Enterprise for CX and Dialogflow CX** — both are live, both are
  documented separately, and neither page references the other. Whether CX is
  the successor to Dialogflow CX, a parallel offering, or something else is
  unresolved. Given that Dialogflow's own documentation warns that products in
  that area are being renamed, this is the open question most likely to resolve
  itself soon.
- **Agent Platform's Optimize phase** — the one lifecycle stage not yet verified
  against its documentation.

## Related

- [Official documentation](00-official-documentation.md)
- [Reference repositories](01-reference-repositories.md)
- [Equivalences and historical names](../12-glossary/01-equivalences-and-historical-names.md)

---
_Last verified: 2026-07-28 against `ai.google.dev/gemini-api/docs/changelog`,
`ai.google.dev/gemini-api/docs/migrate-to-interactions`,
`deepmind.google/models/gemma`,
`docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations`,
`docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes`,
`adk.dev/deploy/`, and `docs.cloud.google.com/dialogflow/cx/docs/concept/version`._
