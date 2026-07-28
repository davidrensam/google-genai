# Google GenAI Integration Guide

Google's AI ecosystem keeps evolving quickly. New products, SDKs, repositories,
APIs, and documentation pages appear constantly, and the result can feel harder
to navigate than it should be.

This repository is a practical guide for developers who want to understand and
integrate with the Google GenAI ecosystem without spending most of their time
figuring out where to start. The goal is to organize the most relevant
documentation, clarify the naming and tooling, and define implementation paths
for different use cases.

It is not a replacement for Google's documentation. It is the map that sits on
top of it: what each piece is, how the pieces relate, which one you actually
need, and what a thing used to be called before it was renamed.

> **Status: early.** The structure below is complete and stable. Most pages are
> still empty — this repository is being written in the open, module by module.
> See [Roadmap](#roadmap) for what is being worked on.

## Start here

| If you… | Go to |
|---|---|
| Have no idea how the pieces fit together | [`00-orientation/00-ecosystem-map.md`](00-orientation/00-ecosystem-map.md) |
| Keep hitting names you don't recognize | [`00-orientation/01-nomenclature-and-renames.md`](00-orientation/01-nomenclature-and-renames.md) |
| Want to make your first call to a model | [`10-learning-paths/00-first-steps-with-gemini.md`](10-learning-paths/00-first-steps-with-gemini.md) |
| Need to choose between the available APIs | [`03-model-access/06-choosing-the-right-path.md`](03-model-access/06-choosing-the-right-path.md) |
| Are deciding whether you even need an agent | [`05-agent-development/01-when-not-to-use-an-agent.md`](05-agent-development/01-when-not-to-use-an-agent.md) |
| Are taking something to production | [`08-production/08-production-checklist.md`](08-production/08-production-checklist.md) |

## The map

Modules are numbered in reading order. You do not have to read them in that
order, but the numbering tells you what each one assumes you already know.

| # | Module | What it covers |
|---|---|---|
| 00 | [orientation](00-orientation/) | The ecosystem map, how the layers divide responsibilities, current vs. historical naming, prerequisites, and how to choose between options |
| 01 | [foundations](01-foundations/) | Product-agnostic concepts: LLMs, context and tokens, multimodality, prompting, structured output, function calling, embeddings and grounding |
| 02 | [models](02-models/) | The model families, what each is for, and how to choose one |
| 03 | [model-access](03-model-access/) | The available paths to reach a model, how authentication differs between them, regions and quotas, and which path fits your case |
| 04 | [development-with-models](04-development-with-models/) | Building against the SDK: which call surface to write, calling without the SDK, reliable design, configuration, errors, retries, timeouts, testing. Includes Python and JavaScript examples |
| 05 | [agent-development](05-agent-development/) | What an agent is, when *not* to build one, ADK, tools and MCP, multi-agent workflows, sessions and memory, debugging, design patterns |
| 06 | [data-and-grounding](06-data-and-grounding/) | RAG end to end: ingestion, chunking, embeddings, retrieval, reranking, citations, access control, vector search |
| 07 | [agent-platform-google-cloud](07-agent-platform-google-cloud/) | The managed platform, organized by lifecycle: build, scale, govern, optimize |
| 08 | [production](08-production/) | Your own stack: reference architecture, threat model, secrets, evaluations, observability, CI/CD, resilience, costs, and a final checklist |
| 09 | [projects](09-projects/) | Five progressive hands-on projects, from a CLI chat to a capstone |
| 10 | [learning-paths](10-learning-paths/) | Curated sequences through the modules above, by goal |
| 11 | [related-products](11-related-products/) | Adjacent products that are easy to confuse with the core ones |
| 12 | [glossary](12-glossary/) | Terms, and a table of what things used to be called |
| — | [resources](resources/) | Official documentation, reference repositories, an ecosystem changelog, and sources per module |

### Where a topic lives

Several topics appear in more than one module on purpose. The axis is:

- **`01-foundations`** — the concept, independent of any product.
- **`05-agent-development`** — how you implement it yourself, in your code.
- **`07-agent-platform-google-cloud`** — how the managed platform solves it.
- **`08-production`** — how you operate it in your own stack.

Each concept is explained once, in one canonical place. The others link to it
and only add what is specific to their context.

## Learning paths

If you prefer a goal-driven route over the module tree:

- [First steps with Gemini](10-learning-paths/00-first-steps-with-gemini.md)
- [A generative app with Python](10-learning-paths/01-generative-app-with-python.md)
- [Your first agent with ADK](10-learning-paths/02-first-agent-with-adk.md)
- [RAG over private data](10-learning-paths/03-rag-and-private-data.md)
- [An agent in production](10-learning-paths/04-agent-in-production.md)

## Running the code

Examples target Python 3.12+ and are managed with [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

Every code sample is meant to run as-is with nothing but an API key in your
environment. If one doesn't, that's a bug — please open an issue.

## Conventions

- Files are numbered `NN-kebab-case.md`; the number encodes reading order.
- Pages with factual content end with a `Last verified: YYYY-MM-DD` line and the
  source they were checked against.
- Volatile data — prices, quotas, rate limits, region lists, per-model
  availability — is **linked, never transcribed**. It goes stale within weeks,
  and a guide that is confidently wrong is worse than no guide at all.

## Roadmap

Written so far: [orientation](00-orientation/) — the ecosystem map, the
nomenclature decoder, and prerequisites; the [glossary](12-glossary/); and the
[resources](resources/) module — the source catalog, the reference repositories,
and the ecosystem changelog.

Current focus is [model access](03-model-access/), the module that untangles the
two paths to a Gemini model, followed by
[foundations](01-foundations/).

## Contributing

Corrections are especially welcome. Google renames and reorganizes things
faster than any single person can track — if you find something outdated, an
issue with a link to the current source is genuinely useful.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
