import os
import yaml
from dotenv import load_dotenv
from constants.constants import TOOL_INVOCATION_MESSAGE
from src.project_management_system.supervisor import buildProjectSupervisor

def runProjectSupervisor():
    load_dotenv()

    supervisor_graph = buildProjectSupervisor()
    supervisor = supervisor_graph.compile(name="project_supervisor") if hasattr(supervisor_graph, "compile") else supervisor_graph

    with open("settings.yaml", "r") as f:
        settings = yaml.safe_load(f)
    project_description = settings["project"]["description"]

    result = supervisor.invoke({
        "messages": [
            {"role": "user", "content": project_description},
            {"role": "system", "content": TOOL_INVOCATION_MESSAGE}
        ]
    })

    for msg in result["messages"]:
        msg_dict = msg.model_dump() if hasattr(msg, "model_dump") else msg
        role = msg_dict.get("role", "PM")
        content = msg_dict.get("content", "No content available")
        print(f"{role}: {content}")

if __name__ == "__main__":
    runProjectSupervisor()
