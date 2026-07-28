# Glossary

## What is in here, and what is not

This is not a glossary of AI terms. Plenty of those exist, and they are not
what makes this ecosystem hard.

A term earns a place here if **getting it wrong sends you to the wrong product
or the wrong documentation.** That is the test. "Embedding" fails it — the
generic definition is fine and no Google page means anything unusual by it.
"Open models" passes: assume it means open source and you will misjudge what you
are allowed to do. "Agent Platform" passes twice over.

So: terms Google coined, terms Google uses differently from everyone else, and
terms whose plain reading points you somewhere wrong.

For old names, see [equivalences and historical names](01-equivalences-and-historical-names.md).
For why the names move at all, see
[nomenclature and renames](../00-orientation/01-nomenclature-and-renames.md).

## Products and platforms

**Agent Platform** — short form of Gemini Enterprise Agent Platform, and the
form its own documentation uses. Formerly Vertex AI. Note that it names two
distinct things: an access path to Gemini models, and a managed runtime and
governance layer. You can use either without the other — see
[the ecosystem map](../00-orientation/00-ecosystem-map.md#one-name-two-layers).

**Agent Runtime** — the managed service that runs deployed agents on Agent
Platform. Formerly Agent Engine, a name the ADK command line still uses.

**Agent Garden** — a library of prebuilt agent samples inside Agent Platform.
Not the Agent Gallery.

**Agent Gateway** — the policy enforcement point on Agent Platform. Governs
agent-to-tool, user-to-agent, and agent-to-agent calls centrally.

**Agent Studio** — the interface for building agents on Agent Platform. Not
Google AI Studio, and not Customer Experience Agent Studio.

**ADK — Agent Development Kit** — Google's open-source, code-first framework for
building agents. Model-agnostic and deployment-agnostic: ADK does not require
Agent Runtime, and Agent Runtime does not require ADK.

**Antigravity** — Google's agent-first development platform, and the path
consumer-tier users were moved to when Gemini CLI and the Code Assist IDE
extensions stopped serving them.

**CodeMender** — an agent that finds and fixes code vulnerabilities. In preview.
A finished product that runs on the ecosystem, not a piece you build with.

**Gemini** — the flagship model family.

**Gemini API** — the API for calling Gemini models. Reachable by two different
paths that share one SDK; see [model access](../03-model-access/00-overview.md).

**Gemini Enterprise** — the application knowledge workers use: intranet search,
assistant, agent surface. **A different product from the Gemini Enterprise Agent
Platform**, with its own documentation tree and its own release notes.

**Gemma** — Google's family of downloadable models. See *open models*.

**Google AI Edge** — the on-device stack. Separate toolchain, separate packages,
separate model formats, and not reachable through the Gen AI SDK.

**Google AI Studio** — the browser tool for prototyping against the Gemini
Developer API and issuing API keys. Not Agent Studio.

**Google Gen AI SDK** — the unified SDK (`google-genai`, `@google/genai`, and
peers). One library for both access paths; a client flag chooses between them.
Spelled three different ways across Google's own documentation.

**Jules** — an autonomous coding agent, its own product line. Not part of
Antigravity, and unaffected by the Code Assist retirement.

**Memory Bank** — long-term memory for agents on Agent Platform: extracts,
stores, and retrieves information across sessions.

**SAIF — Secure AI Framework** — Google's published framework for AI security
and privacy. Explicitly *not* a description of how Google secures its own
products, and explicitly scoped away from fairness and interpretability.

**Skill Registry** — where agent skills are stored and discovered on Agent
Platform.

## Terms that mean something specific here

**Grounding** — connecting a model's output to a source of truth so answers can
be traced back to it. In Google's usage this covers both retrieval over your own
data and search-backed answering; do not assume it means only one of them.

**Interactions API** — the call surface Google now recommends for Gemini,
built around a persistent interaction rather than a single request. The older
`generateContent` remains fully supported; see
[two calls, one client](../00-orientation/01-nomenclature-and-renames.md#two-calls-one-client).

**Open models** — Google's term for Gemma. It means the weights are downloadable
and you can run them yourself. It does **not** by itself mean open source: Gemma
1 through 3 shipped under a custom, non-OSI licence. Gemma 4 is Apache 2.0. The
branding never changed; the licence did, and only from version 4 — so any claim
about Gemma licensing has to name a generation.

**Managed agent** — an agent Google runs for you, as opposed to one you deploy.

**Grounded generation, RAG, retrieval** — see
[data and grounding](../06-data-and-grounding/00-rag-design.md). The concepts are
generic; only their product names here are not.

## Names that are easy to confuse

Live products whose names are close enough to be mistaken for each other. None
of these pairs is a rename — both sides exist right now.

| This | Is not this |
|---|---|
| **Gemini Enterprise** — the application for knowledge workers | **Gemini Enterprise Agent Platform** — the developer platform, formerly Vertex AI |
| **Agent Gallery** — inside Gemini Enterprise | **Agent Garden** — inside Agent Platform |
| **Agent Studio** — building agents on Agent Platform | **Google AI Studio** — prototyping against the Gemini Developer API |
| Both of the above | **Customer Experience Agent Studio** — a third one, inside Gemini Enterprise for CX |
| **Agent Runtime** — where agents run | **Agent Engine** — the same thing, previous name, still in the CLI |
| **Antigravity** — the consumer-tier development platform | **Gemini Code Assist** — the licensed product, which still ships Gemini CLI |

The pattern is worth naming: Google reuses a small vocabulary — *agent*,
*studio*, *enterprise*, *gallery/garden* — across products built by different
teams for different audiences. Two products sharing a word tell you almost
nothing about whether they are related.

---
_Last verified: 2026-07-28 against `docs.cloud.google.com/gemini-enterprise-agent-platform`
(overview, build, scale, govern), `docs.cloud.google.com/gemini/enterprise/docs`,
`ai.google.dev/gemini-api/docs`, `adk.dev`, `deepmind.google/models/gemma`,
`developers.google.com/edge`, and `jules.google`. See
[resources](../resources/00-official-documentation.md)._
