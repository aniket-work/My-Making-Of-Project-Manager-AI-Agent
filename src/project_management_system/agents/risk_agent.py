import yaml
from langgraph.prebuilt import create_react_agent

def _load_agent_settings():
    with open("settings.yaml", "r") as f:
        settings = yaml.safe_load(f)
    return settings["agents"]["risk_agent"]

def instantiateRiskAnalysisAgent(llm, tools):
    settings = _load_agent_settings()
    prompt = settings["prompt"]
    return create_react_agent(
        llm,
        tools=tools,
        state_modifier=prompt,
        name="RiskAnalysisAgent"
    )
