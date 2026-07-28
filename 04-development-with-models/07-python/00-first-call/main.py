"""The smallest useful call to a Gemini model.

Run it:
    export GEMINI_API_KEY="your-key"
    uv run 04-development-with-models/07-python/00-first-call/main.py

This uses the Interactions API, which is what Google's documentation recommends
for new development. `client.models.generate_content()` still works and is still
fully supported — see 04-development-with-models/02-interactions-and-generate-content.md
for which one to write and why.
"""

import os
import sys

from google import genai


def main() -> None:
    # The client reads GEMINI_API_KEY or GOOGLE_API_KEY from the environment.
    # Never put the key in the source — see 08-production/02-secrets-management.md.
    if not (os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")):
        sys.exit("Set GEMINI_API_KEY first. See 00-orientation/02-prerequisites.md")

    client = genai.Client()

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input="In one sentence: what is the difference between a model and an API?",
    )

    print(interaction.outputs[-1].text)


if __name__ == "__main__":
    main()
