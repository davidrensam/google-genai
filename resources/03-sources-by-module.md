# Sources by module

Which sources feed which chapter. Use this when writing or revising a module, or
when you want to go past what a page here tells you.

Tier numbers refer to the
[five tiers](00-official-documentation.md#the-five-tiers). Tiers 1 and 2 are
citable; tier 3 is worth reading and must be marked as unofficial wherever it is
linked.

| Module | Primary sources | Tier |
|---|---|---|
| [00 orientation](../00-orientation/00-ecosystem-map.md) | Agent Platform documentation root · `ai.google.dev` · [ecosystem changelog](02-ecosystem-changelog.md) | 1 |
| [01 foundations](../01-foundations/00-generative-ai-and-llms.md) | `ai.google.dev/gemini-api/docs` · Gemini API release notes | 1 |
| [02 models](../02-models/00-overview.md) | Agent Platform documentation → Models · Gemini API release notes · `deepmind.google/models/gemma` and `ai.google.dev/gemma/docs` | 1 |
| [03 model-access](../03-model-access/00-overview.md) | `ai.google.dev` and the Agent Platform root, read side by side · `aistudio.google.com` · Application Default Credentials documentation | 1 |
| [04 development-with-models](../04-development-with-models/00-overview.md) | `googleapis/python-genai` and `googleapis/js-genai` source · Client Libraries · API Reference | 1, 2 |
| [05 agent-development](../05-agent-development/00-what-is-an-agent.md) | `adk.dev` · `google/adk-python` source · `google/adk-samples` | 1, 2, **3** |
| [06 data-and-grounding](../06-data-and-grounding/00-rag-design.md) | RAG and grounding sections of Agent Platform documentation · RAG folders in `GoogleCloudPlatform/generative-ai` | 1, **3** |
| [07 agent-platform](../07-agent-platform-google-cloud/00-overview.md) | Agent Platform documentation root, section by section: Studio, Agents, Models, Notebooks | 1 |
| [08 production](../08-production/00-reference-architecture.md) | Pricing · deprecations table · observability documentation · `adk.dev/deploy/` | 1 |
| [09 projects](../09-projects/) | `google/adk-samples` · `GoogleCloudPlatform/generative-ai` | **3** |
| [10 learning-paths](../10-learning-paths/00-first-steps-with-gemini.md) | Cross-cutting; no sources of its own | — |
| [11 related-products](../11-related-products/00-gemini-enterprise-app.md) | Gemini Enterprise documentation (`/gemini/enterprise/docs`) · Gemini Enterprise for CX · Dialogflow CX · `antigravity.google` · CodeMender documentation · Google Developers Blog for the CLI transition | 1, 4 |
| [12 glossary](../12-glossary/00-glossary.md) | Every rename below · deprecations table · both release-notes feeds | 1 |

## Notes on specific modules

**03 model-access** is the module most likely to go stale, because it describes
the boundary between two products that are being consolidated. Read both
documentation roots in the same sitting; reading one and then the other a week
later is how contradictions get missed.

**05 agent-development** leans hardest on tier 3. `adk-samples` is the fastest
way to see working agent code, and its own README states the recipes are not
intended for production. Take patterns from it, not guarantees.

**09 projects** is built almost entirely on tier 3 material. That is acceptable
for a project you are building to learn, and unacceptable as the basis for a
claim about how something works. When a project needs a normative statement,
source it from tier 1.

**11 related-products** is the only module that leans on tier 4. The Gemini CLI
to Antigravity transition was announced on the Google Developers Blog, and the
announcement is the clearest statement of what changed and for whom. Use it to
establish the date and the scope of the change, and the product documentation
for everything else.

**12 glossary** has no sources of its own by design. It is a derived artifact:
every entry should be traceable to a change recorded in the
[ecosystem changelog](02-ecosystem-changelog.md).

## Related

- [Official documentation](00-official-documentation.md)
- [Reference repositories](01-reference-repositories.md)
- [Ecosystem changelog](02-ecosystem-changelog.md)

---
_Last verified: 2026-07-28. Source inventory current as of that date; see the
individual pages above for per-source verification._
