# Official documentation

Where the authoritative answers live, and how much weight each source carries.

Read this before citing anything. In an ecosystem this volatile, knowing *how
current* a source is matters as much as what it says.

## Two domain rules

**1. Google Cloud documentation lives on `docs.cloud.google.com`.**

`cloud.google.com/vertex-ai/...` returns a `301` to
`docs.cloud.google.com/vertex-ai/...`. The redirect works, so nothing breaks —
which is exactly why stale links survive for years. Every link in this
repository uses the current domain.

**2. `cloud.google.com/products/...` is marketing, not documentation.**

Product pages did not move. They are useful for "what is this" and useless for
"how do I use it". Never cite a product page for behavior.

## The five tiers

| Tier | What it is | How to use it |
|---|---|---|
| **1** | Official documentation | Cite freely. The only source for normative claims. |
| **2** | Official Google repositories | Cite freely. The **code** is more reliable than the README, which often lags. |
| **3** | Repositories under Google orgs that disclaim official status | Learn from them. **Do not cite them as authority.** If you link one, say it is unofficial. |
| **4** | Google and Google Cloud blogs | Useful only to *date* a change. Never as a technical reference. |
| **5** | Everything else | Not citable here. |

Tier 3 deserves attention. Several of the most useful resources in this
ecosystem sit under Google-owned GitHub organizations and still state, in their
own README, that they are *not an officially supported Google product*. They
are excellent starting points and poor citations. See
[reference repositories](01-reference-repositories.md) for which is which.

## Tier 1 — official documentation

### Gemini Enterprise Agent Platform

The managed platform on Google Cloud. Formerly Vertex AI; the platform's own
documentation now uses **Agent Platform** as the short form.

| What | URL |
|---|---|
| Documentation root | `docs.cloud.google.com/gemini-enterprise-agent-platform` |
| Release notes | `docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes` |
| Deprecations | `docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations` |
| Product page | `cloud.google.com/products/gemini-enterprise-agent-platform` |

The documentation root is organized into: Overview · Studio · Agents · Models ·
Notebooks · CodeMender · API Reference · gcloud CLI Reference · Client
Libraries · Pricing · Engineering Blog.

The platform's own documentation is then organized by agent lifecycle, and the
URLs follow it: `/build/`, `/scale`, `/govern/`, and `/optimize`.
[Module 07](../07-agent-platform-google-cloud/00-overview.md) mirrors that
structure, so a page there maps onto its official source without translation.

Note that `/vertex-ai/generative-ai/docs` paths still resolve. They are the
compatibility route, not the canonical one — prefer
`/gemini-enterprise-agent-platform`.

### Gemini API

The developer-facing API, reachable with an API key and no Google Cloud project.

| What | URL |
|---|---|
| Documentation root | `ai.google.dev` |
| Release notes | `ai.google.dev/gemini-api/docs/changelog` |
| Client libraries | `ai.google.dev/gemini-api/docs/libraries` |
| Migration to the unified SDK | `ai.google.dev/gemini-api/docs/migrate` |

These two products have separate documentation sites, separate release notes,
and separate versioning. That split is the single most common source of
confusion for newcomers, and the reason
[`03-model-access/`](../03-model-access/00-overview.md) exists as its own module.

### Agent Development Kit

| What | URL |
|---|---|
| Documentation | `adk.dev` (also served at `google.github.io/adk-docs`) |
| Deployment guide | `adk.dev/deploy/` |

### Gemini Enterprise

A **separate product** from the Agent Platform, despite the shared name. It is
the application knowledge workers use; the Agent Platform is what developers
build on. Separate documentation tree, separate release notes.

| What | URL |
|---|---|
| Documentation | `docs.cloud.google.com/gemini/enterprise/docs` |
| Release notes | `docs.cloud.google.com/gemini/enterprise/docs/release-notes` |
| Product page | `cloud.google.com/gemini-enterprise` |

See [related products](../11-related-products/00-gemini-enterprise-app.md), and
the [name collisions](02-ecosystem-changelog.md#names-that-are-easy-to-confuse)
this creates.

### Other products

| What | URL |
|---|---|
| Google AI Studio | `aistudio.google.com` |
| Google Antigravity | `antigravity.google` |
| Gemini Enterprise for CX | `docs.cloud.google.com/customer-engagement-ai` |
| Dialogflow CX | `docs.cloud.google.com/dialogflow/cx/docs` |
| CodeMender | `docs.cloud.google.com/gemini-enterprise-agent-platform/codemender` |

## How to read a documentation page critically

**Check the product name in the breadcrumb, not in the body.** Navigation is
regenerated on every publish; prose is edited by hand and lags behind. When the
breadcrumb and the body disagree, the breadcrumb is newer.

**Treat a URL path as historical evidence.** A page served under
`/vertex-ai/` while its title says "Agent Platform" is telling you when it was
written and when it was renamed. That gap is
[glossary](../12-glossary/01-equivalences-and-historical-names.md) material.

**Prices, quotas, rate limits, regions, and per-model availability are never
reproduced in this repository.** They change without notice and a confidently
wrong number is worse than no number. Those pages are linked, and the
surrounding text explains how to read them and what the numbers imply for your
decision.

**When two official pages contradict each other, do not average them.** It
almost always means something changed recently and one page has not caught up.
Document the contradiction — that discrepancy is precisely what this repository
exists to capture.

## Related

- [Reference repositories](01-reference-repositories.md) — source code and samples
- [Ecosystem changelog](02-ecosystem-changelog.md) — where change is announced
- [Sources by module](03-sources-by-module.md) — which sources feed which chapter

---
_Last verified: 2026-07-28 against `docs.cloud.google.com/gemini-enterprise-agent-platform`,
`ai.google.dev/gemini-api/docs/libraries`, and `adk.dev/deploy/`._
