import sys
from pathlib import Path

# Add the project root to sys.path to allow importing from models.py
sys.path.append(str(Path(__file__).parent.parent))
from typing import Iterator

from agno.agent import Agent, RunEvent, RunOutput, RunOutputEvent
from agno.tools.hackernews import HackerNewsTools
from agno.utils.pprint import pprint_run_response

from models import models

agent = Agent(
    model=models["gemini_2_5_flash"],
    tools=[HackerNewsTools()],
    instructions="Write a report on the topic. Output only the report.",
    markdown=True,
)

# Run the agent and print the response
agent.print_response("Trending startups and products.")

################ STREAM RESPONSE #################
stream: Iterator[RunOutputEvent] = agent.run("Trending products", stream=True)
for chunk in stream:
    if chunk.event == RunEvent.run_content:
        print(chunk.content)

################ STREAM AND PRETTY PRINT #################
stream: Iterator[RunOutputEvent] = agent.run("Trending products", stream=True)
pprint_run_response(stream, markdown=True)
