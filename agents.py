import os

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openrouter import OpenRouter
from agno.tools.mcp import MCPTools

agent = Agent(
    model=OpenRouter(
        id="x-ai/grok-4.1-fast:free",
        api_key=os.getenv("OPENROUTER_AGNO_API_KEY"),
    ),
    tools=[MCPTools(transport="streamable-http", url="https://docs.agno.com/mcp")],
    instructions="You are a helpful AI assistant.",
    db=SqliteDb(db_file="agent.db"),  # Store conversations
    add_history_to_context=True,  # Remember previous messages
    markdown=True,
)
