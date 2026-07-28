# Prerequisites

The [ecosystem map](00-ecosystem-map.md) describes two paths through the stack.
They have very different entry costs, and most "getting started" friction comes
from paying the second path's bill when the first would do.

## For either path

- **One language.** This repository's examples use Python 3.12+ managed with
  [uv](https://docs.astral.sh/uv/); JavaScript equivalents live alongside them
  in [04-development-with-models](../04-development-with-models/00-overview.md).
- **A terminal and git.** Nothing advanced.
- **No machine learning background.** The concepts you need are covered in
  [01-foundations](../01-foundations/00-generative-ai-and-llms.md), and none of
  them require the math.

## Direct path: an API key and nothing else

You need a **Gemini API key**, issued through Google AI Studio — the current
steps are in the [Gemini API documentation](https://ai.google.dev). That is the
entire entry cost: no Google Cloud account, no project, no billing setup, no
`gcloud`.

The SDK reads the key from either `GEMINI_API_KEY` or `GOOGLE_API_KEY`:

```bash
export GEMINI_API_KEY="your-key-here"
```

Two rules from day one:

- **The key lives in the environment, never in code.** If it ends up in a file,
  that file is in `.gitignore`. Production-grade handling is covered in
  [secrets management](../08-production/02-secrets-management.md).
- **Usage tiers and rate limits are read on the official pages, not here.**
  They change without notice; this repository links them instead of
  transcribing them.

## Cloud path: a Google Cloud project

Everything above, plus:

- **A Google Cloud account and a project** with billing enabled.
- **The `gcloud` CLI**, authenticated for Application Default Credentials —
  the SDK's own documentation points to
  [Google's ADC setup guide](https://cloud.google.com/docs/authentication/provide-credentials-adc)
  for the current steps. ADC replaces the API key entirely on this path.
- **A region choice.** Which models are available where is exactly the kind of
  volatile data this repository links rather than copies — see
  [regions, versions, and quotas](../03-model-access/05-regions-versions-and-quotas.md).

The SDK picks the path up from the environment:

```bash
export GOOGLE_GENAI_USE_ENTERPRISE=true
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="us-central1"
```

## What you do not need

The most expensive prerequisite mistakes here are the ones you did not have to
pay:

- **No Google Cloud project** to call Gemini on the direct path. The API key is
  the whole story.
- **No agent framework** to call a model. ADK enters when you need multi-step
  structure, not before — see
  [when not to use an agent](../05-agent-development/01-when-not-to-use-an-agent.md).
- **No containers, no Kubernetes** until you are operating something. The
  runtime layer is the last one you adopt, not the first.
- **None of the retired SDKs.** If a tutorial starts with
  `pip install google-generativeai` or reaches Gemini through
  `import vertexai`, it predates the consolidation and will not run — see
  [nomenclature and renames](01-nomenclature-and-renames.md).

## Check your setup

```bash
uv --version
test -n "$GEMINI_API_KEY" && echo "key is set"
```

Then, from this repository's root:

```bash
uv sync
```

Every code sample here is meant to run as-is after that, with nothing but the
key in your environment. If one does not, that is a bug — open an issue.

---
_Last verified: 2026-07-28. Environment variables and client flags checked
against the `googleapis/python-genai` source; key issuance and ADC pointers
against `ai.google.dev` and the SDK's own documentation. See
[resources](../resources/00-official-documentation.md)._
