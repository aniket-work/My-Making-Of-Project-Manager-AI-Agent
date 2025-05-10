import yaml
from langgraph.prebuilt import create_react_agent
from typing_extensions import TypedDict

class Task(TypedDict):
    title: str
    description: str
    estimate_hours: float
    role: str

def _load_agent_settings():
    with open("settings.yaml", "r") as f:
        settings = yaml.safe_load(f)
    return settings["agents"]["task_agent"]

def instantiateTaskGeneratorAgent(llm, tools):
    settings = _load_agent_settings()
    prompt = settings["prompt"]
    return create_react_agent(
        llm,
        tools=tools,
        state_modifier=prompt,
        name="TaskGeneratorAgent"
    )
