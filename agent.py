import json
from google.adk.agents import LlmAgent

def get_menu() -> str:
    """Reads and returns the coffee menu items."""
    try:
        with open("menu.json", "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading menu: {str(e)}"

barista_agent = LlmAgent(
    name="coffee_barista",
    model="gemini-3.5-flash",
    instruction=(
        "You are a friendly coffee shop barista assistant. "
        "Always use the `get_menu` tool to answer questions about menu items, prices, and allergens. "
        "Strictly recommend ONLY items present in the menu. "
        "If a user asks for something not on the menu, politely inform them it is unavailable."
    ),
    tools=[get_menu]
)
