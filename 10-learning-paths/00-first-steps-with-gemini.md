# First steps with Gemini

The shortest honest route from nothing to a working call, and then to
understanding what you just did.

**Entry cost:** an API key. No Google Cloud account, no project, no billing
setup. If a tutorial asks you for those on your first call, it is teaching the
other path — see [choosing the right path](../03-model-access/06-choosing-the-right-path.md).

**Where this leaves you:** able to call a model from your own code, and able to
tell whether any Gemini tutorial you find online is still current. The second
one matters more than it sounds.

## 1. Know what you are reaching for

Read [the ecosystem map](../00-orientation/00-ecosystem-map.md), specifically
the layers table and the two paths through it.

The point to carry forward: the model, the access path, the SDK, the agent
framework, and the runtime are **independent choices**. Right now you are
picking exactly two of them — Gemini, and the Developer API — and leaving the
rest alone. Nothing you do here commits you to a framework or a platform.

## 2. Get set up

[Prerequisites](../00-orientation/02-prerequisites.md), the direct-path section
only. Skip the cloud path entirely.

You need Python 3.12+, `uv`, and a Gemini API key in your environment:

```bash
export GEMINI_API_KEY="your-key"
```

Then, from the repository root:

```bash
uv sync
```

## 3. Make the call

```python
from google import genai

client = genai.Client()  # reads GEMINI_API_KEY from the environment

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="In one sentence: what is the difference between a model and an API?",
)
print(interaction.outputs[-1].text)
```

That is the whole thing. Two points in it are worth pausing on:

**The client takes no arguments.** `genai.Client()` finds your key in the
environment. Nothing in the code names a project, a region, or a credential
file, because on this path none of those exist.

**The call is `client.interactions.create()`.** Most tutorials you find will use
`client.models.generate_content()` instead. That one still works — it is not
deprecated — but it is no longer what the documentation recommends for new code.
This is the first place you will feel the ecosystem moving underneath you, and
settling it is the whole job of
[interactions and generate_content](../04-development-with-models/02-interactions-and-generate-content.md).

The runnable version of this, with error handling and the variations worth
trying, lands in
[04-development-with-models](../04-development-with-models/00-overview.md)
alongside that module's prose.

## 4. Learn to date what you read

This is the step people skip, and it is the one that saves the most time.

Read [nomenclature and renames](../00-orientation/01-nomenclature-and-renames.md),
especially the four name states and the table at the end.

Then do this: find any Gemini quickstart on the open web and score it. Check the
import line, then the client constructor, then the call. You will find plenty
that fail on the first line — `import google.generativeai` and `import vertexai`
are both switched off, and no amount of following along will make them work.

Being able to reject a dead tutorial in five seconds is a real skill, and this
ecosystem demands it more than most.

## 5. Understand what a model call actually is

[Foundations](../01-foundations/00-generative-ai-and-llms.md), in order:
generative models, then context and tokens, then prompting.

Do this *after* the working call, not before. The concepts land differently when
you have already seen a response come back and can experiment against something
real.

## Where to go next

| If you want to… | Go to |
|---|---|
| Build an actual application | [A generative app with Python](01-generative-app-with-python.md) |
| Get structured data back instead of prose | [structured output and function calling](../01-foundations/04-structured-output-and-function-calling.md) |
| Use your own documents as the source | [RAG over private data](03-rag-and-private-data.md) |
| Find out whether you need an agent | [when not to use an agent](../05-agent-development/01-when-not-to-use-an-agent.md) |
| Move onto Google Cloud | [choosing the right path](../03-model-access/06-choosing-the-right-path.md) |

## What this path deliberately skips

Not oversights — decisions, so you do not go looking for them:

- **Agents and ADK.** A single model call is not an agent, and treating it as
  one adds machinery you cannot yet evaluate.
- **Google Cloud, projects, and ADC.** Real, and unnecessary until you need
  identity, governance, or scale.
- **Model comparison.** Pick the default, get something working, then read
  [choosing a model](../02-models/05-choosing-a-model.md) with a concrete
  workload in hand.
- **Prices and quotas.** Read them on Google's pages when they matter. They
  change too fast to be worth memorising, and this repository links rather than
  transcribes them.

---
_Last verified: 2026-07-28 against `ai.google.dev/gemini-api/docs/get-started`
and the `googleapis/python-genai` client source._
