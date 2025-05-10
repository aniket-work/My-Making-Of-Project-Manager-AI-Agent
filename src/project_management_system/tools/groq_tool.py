from langchain.tools import tool
from .groq_client import HealthcareGroqClient

groq_client = HealthcareGroqClient()

@tool("groq_generate", return_direct=True, description="Generate text via the GROQ LLM for Healthcare Research Analysis Project")
def groq_generate(prompt: str) -> str:
    return groq_client.generate(prompt)

