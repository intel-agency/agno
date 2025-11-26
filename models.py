import os

from agno.models.google import Gemini
from agno.models.openrouter import OpenRouter

gemini_3_model = Gemini(
    id="gemini-3-pro-preview",
)

openrouter_grok4_1_fast_model = OpenRouter(
    id="x-ai/grok-4.1-fast:free",
    api_key=os.getenv("OPENROUTER_AGNO_API_KEY"),
)

models = {
    "gemini_3_model": gemini_3_model,
    "openrouter_grok4_1_fast_model": openrouter_grok4_1_fast_model,
}
