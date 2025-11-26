import sys
from pathlib import Path

# Add the project root to sys.path to allow importing from models.py
sys.path.append(str(Path(__file__).parent.parent))

from agno.agent import Agent
from agno.tools.hackernews import HackerNewsTools

from models import openrouter_grok4_1_fast_model

agent = Agent(
    model=openrouter_grok4_1_fast_model,
    tools=[HackerNewsTools()],
    instructions="Write a report on the topic. Output only the report.",
    markdown=True,
)
agent.print_response("Trending startups and products.", stream=True)
