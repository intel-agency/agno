import os

from agno.agent import Agent
from agno.models.openrouter import OpenRouter

# Create your Agent
agent = Agent(
    model=OpenRouter(
        id="x-ai/grok-4.1-fast:free",
        api_key=os.getenv("OPENROUTER_AGNO_API_KEY"),
    ),
    instructions="You are a helpful AI assistant.",
    markdown=True,
)

# Run
agent.print_response("What is artificial intelligence?", stream=True)
