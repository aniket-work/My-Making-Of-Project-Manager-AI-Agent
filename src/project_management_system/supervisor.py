import json
import yaml
from langgraph_supervisor import create_supervisor
from langchain_openai import ChatOpenAI
from .agents.task_agent import instantiateTaskGeneratorAgent
from .agents.scheduling_agent import instantiateScheduleCoordinatorAgent
from .agents.risk_agent import instantiateRiskAnalysisAgent
from .tools.groq_client import HealthcareGroqClient
from .tools.groq_tool import groq_generate

def _load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def buildProjectSupervisor():
    config = _load_config()
    openai_llm = ChatOpenAI(model=config["llm"]["model"], temperature=config["llm"]["temperature"])
    groq_client = HealthcareGroqClient()
    tools = [groq_generate]
    task_agent = instantiateTaskGeneratorAgent(openai_llm, tools)
    schedule_agent = instantiateScheduleCoordinatorAgent(openai_llm, tools)
    risk_agent = instantiateRiskAnalysisAgent(openai_llm, tools)

    with open("settings.yaml", "r") as f:
        settings = yaml.safe_load(f)
    supervisor_prompt = settings["supervisor"]["prompt"]

    return create_supervisor(
        agents=[task_agent, schedule_agent, risk_agent],
        model=openai_llm,
        prompt=supervisor_prompt
    )

