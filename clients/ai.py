import os
from typing import Optional

from openai import OpenAI

def get_openai_client() -> Optional[OpenAI]:
    """Return an OpenAI client if API key is set,
     otherwise return None (fallback)."""

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)

def summarize_project_text(description: str, notes: str | None = None) -> str:
    """Generate a short (1–2 sentence) summary of a project.

    If OPENAI_API_KEY is missing or the API call fails,
    fall back to a simple
    truncated version of the original text (~280 characters).
    """

    base_text = (description or "").strip()
    if notes:
        base_text += "\n\nNotes:\n" + notes.strip()

    if not base_text:
        return ""


    # simple fallback
    client = get_openai_client()
    if client is None:
        # fallback make shorter text
        return base_text[:280]

    prompt = (
        "You are helping a freelance developer keep a concise CRM.\n"
        "Summarize the following project in 1–2 short sentences, in plain English.\n"
        "Focus on what the project does and tech stack (if mentioned).\n\n"
        f"Project text:\n{base_text}"
    )


    try:
        # New OpenAI „responses“ API, like in official examples  [oai_citation:1‡OpenAI Platform](https://platform.openai.com/docs/overview?lang=python&utm_source=chatgpt.com)
        response = client.responses.create(
            model="gpt-5.2-mini",
            input=prompt,
            max_output_tokens=80,
        )
        # Library returns convenient .output_text
        return (response.output_text or "").strip()
    except Exception:
        # if something  happens (net, quota, wrong key and so on) – silent fallback
        return base_text[:280]




