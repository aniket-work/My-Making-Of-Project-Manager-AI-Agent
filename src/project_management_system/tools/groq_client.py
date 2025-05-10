import os
import json
from langchain_groq import ChatGroq
from dotenv import load_dotenv

class HealthcareGroqClient:
    def __init__(self):
        load_dotenv()
        with open("config.json", "r") as f:
            config = json.load(f)
        api_key = os.getenv(config["groq"]["api_key_env"])
        if not api_key:
            raise ValueError("Missing GROQ_API_KEY in environment")
        self.client = ChatGroq(groq_api_key=api_key, model=config["groq"]["model"])

    def generate(self, prompt: str, **kwargs) -> str:
        response = self.client.invoke(
            {"messages": [
                {"role": "system", "content": "Invoking GROQ tool for Healthcare Research Analysis Project."},
                {"role": "user", "content": prompt}
            ]},
            **kwargs
        )
        return response["messages"][-1]["content"]
