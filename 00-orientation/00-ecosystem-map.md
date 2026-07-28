# The ecosystem map

Google's generative AI offering is not hard because any single piece is
complicated. It is hard because the pieces are presented as one product when
they are not. You can pick a model without picking an API. You can write code
without adopting a framework. You can build an agent and never touch the
managed platform.

This page is the map. Everything else in this repository hangs off it.

## Start here

Find your question, go to the layer that owns it.

| Your question | Layer | Read |
|---|---|---|
| "Which model can do what I need?" | The model | [02-models](../02-models/00-overview.md) |
| "Do I need a Google Cloud project for this?" | Access | [03-model-access](../03-model-access/00-overview.md) |
| "Why are there two APIs that look the same?" | Access | [03-model-access](../03-model-access/06-choosing-the-right-path.md) |
| "Is the `import` in this tutorial still valid?" | Code | [04-development](../04-development-with-models/01-google-gen-ai-sdk.md) |
| "Do I even need an agent?" | Agent framework | [05-agent-development](../05-agent-development/01-when-not-to-use-an-agent.md) |
| "How do I ground this in my own data?" | Cross-cutting | [06-data-and-grounding](../06-data-and-grounding/00-rag-design.md) |
| "Where does this run in production?" | Runtime and operations | [07](../07-agent-platform-google-cloud/00-overview.md) · [08](../08-production/00-reference-architecture.md) |
| "What is this thing called now?" | — | [12-glossary](../12-glossary/01-equivalences-and-historical-names.md) |

## The layers

A layer is not a topic. It is a **substitution boundary**: the point where you
can replace what sits on one side without rewriting what sits on the other.

| Layer | Question it answers | What lives here |
|---|---|---|
| **The model** | What does the actual work? | Gemini, Gemma, and the image, video, and audio families — see [02-models](../02-models/00-overview.md) |
| **Access** | How do you reach it? | Gemini Developer API · Gemini API on Agent Platform |
| **Code** | How do you call it? | Google Gen AI SDK (Python, JavaScript/TypeScript, Go, Java, .NET) · REST |
| **Agent framework** | How do you structure multi-step work? | ADK · LangGraph · LangChain · LlamaIndex · AG2 · your own |
| **Runtime and operations** | Where does it run, and who governs it? | Agent Runtime · Cloud Run · GKE · your own containers |
| **Your application** | What are you actually building? | Yours |

## The layers are independent

This is the part most introductions skip, and the reason the ecosystem feels
heavier than it is. Walk up the stack and ask what a change actually costs you:

- Swap **Gemini for Gemma** — your code does not change.
- Swap the **Developer API for Agent Platform** — authentication changes
  completely, the endpoint changes, your model calls do not.
- Swap **direct SDK calls for ADK** — the shape of your program changes, the
  model and the access path do not.
- Swap **Agent Runtime for Cloud Run** — your agent is the same code, only the
  deployment changes.

Every cut where one thing changes and the others hold is a layer.

The practical consequence: **choosing one layer does not commit you to the
next.** A large share of the confusion around this ecosystem comes from
assuming it does — that adopting ADK, say, means deploying to Agent Runtime.
It does not.

## One name, two layers

**Agent Platform appears twice in the layers table** — once under Access, once
under Runtime and operations.

That is not an error. Agent Platform genuinely is two things:

- **An access path.** The Gemini API on Agent Platform is one of the two ways to
  reach a Gemini model. Choosing it means Application Default Credentials, a
  Google Cloud project, and a region, instead of an API key.
- **A managed runtime and governance layer.** Agent Runtime, Sessions, Memory
  Bank, Skill Registry, and Agent Gateway are where agents run and are governed.

You can use the first without the second: reach Gemini through Agent Platform
and deploy your application wherever you like. You can also use the second while
your agent calls models elsewhere.

The SDK makes the split visible. Its client takes an `enterprise` flag that
selects the access path — and the flag says nothing about where your code runs.
See
[03-model-access](../03-model-access/03-gemini-api-in-agent-platform.md).

## Two paths through the same layers

Neither path is more correct. They differ in what they ask of you up front.

```
  Layer                   Direct path            Cloud path
  ─────────────────────────────────────────────────────────────────
  The model               Gemini                 Gemini
  Access                  Developer API          Gemini API on
                                                 Agent Platform
  Code                    Gen AI SDK             Gen AI SDK
  Agent framework         —                      ADK
  Runtime and operations  —                      Agent Runtime
  Your application        your app               your app
```

The dashes are the point. **The direct path skips two entire layers** — you get
an API key, install the SDK, and ship. No project, no framework, no managed
runtime.

The cloud path adds identity, governance, scaling, and persistence, and asks for
a Google Cloud project in return.

Most real work starts in the left column and adopts the right column one layer
at a time; nothing obliges you to make the whole journey. See
[10-learning-paths](../10-learning-paths/00-first-steps-with-gemini.md) for both
routes as step-by-step sequences.

## What is not a layer

**Data and grounding.** It is tempting to slot RAG between the agent and the
runtime. It does not fit, because it attaches at three different heights:
grounding at the model layer, tools and retrieval at the agent layer, RAG Engine
and Vector Search at the platform layer. It is a cross-cutting concern, not a
step — one more sign of how independent the layers are. See
[06-data-and-grounding](../06-data-and-grounding/00-rag-design.md).

**Named services inside a layer.** Memory Bank, Skill Registry, and Agent
Gateway have their own names, their own documentation pages, and their own
pricing. None of them is a layer. They are services within Runtime and
operations. Having a name does not confer rank.

**Finished products built on the stack.** Gemini Enterprise, the application
knowledge workers use, and CodeMender, a security agent, run on this ecosystem
but are not part of the stack you assemble. They are destinations, not layers,
and they live in
[11-related-products](../11-related-products/00-gemini-enterprise-app.md).

**Lifecycle stages.** [Module 07](../07-agent-platform-google-cloud/00-overview.md)
is organized as build, scale, govern, and optimize, mirroring the platform's own
documentation. Those are *stages* — temporal, sequential, describing the life of
an agent. Layers are structural and coexist: when your agent runs, all six are
active at once. Two useful taxonomies, two different axes; do not read one as
the other.

## Where the repository goes from here

The module numbering follows the layers:

```
01 Foundations → 02 Models → 03 Access → 04 Code → 05 Agents
   → 06 Data → 07 Platform → 08 Production → 09 Projects
```

In one sentence: **model → access → code → agents → operations**, with data
cutting across all of them.

If you would rather follow a goal than a stack, start at
[10-learning-paths](../10-learning-paths/00-first-steps-with-gemini.md).

And if a product name here does not match what you saw somewhere else, that is
expected, and it has its own page:
[nomenclature and renames](03-nomenclature-and-renames.md).

---
_Last verified: 2026-07-28 against `docs.cloud.google.com/gemini-enterprise-agent-platform`
(overview, build, scale, govern), `ai.google.dev`, `adk.dev/deploy/`, and the
`googleapis/python-genai` client source. See
[resources](../resources/00-official-documentation.md)._
