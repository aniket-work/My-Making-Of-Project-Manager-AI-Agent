# My Making Of Project Manager AI Agent

Hands on : How to leverage AI Agents for project management


## TL;DR
I built a project management system using three AI agents (task generator, scheduler, risk analyzer) that work together under a supervisor to create comprehensive healthcare project plans. The system uses Muliple Agents for healthcare expertise, with all configuration stored externally for flexibility. This approach shows how collaborative AI can transform business operations beyond simple automation.


## What’s This Article About?
This article walks through my implementation of an AI-powered project planning tool specifically designed for healthcare research projects. I built a system with three specialized agents — one generates tasks, another handles scheduling, and a third analyzes risks. These agents collaborate under a central “supervisor” that coordinates their work. 

The system leverages both general-purpose AI (OpenAI) and healthcare-specialized AI (Groq) to produce comprehensive project plans tailored to healthcare contexts. I designed everything to be configurable through external files rather than hardcoding, making it adaptable to different projects.

Full Article : [https://medium.com/@learn-simplified/my-making-of-project-manager-ai-agent-455d2f0bfdca


## Tech Stack  

| Component | Technology |
|-----------|------------|
| Programming Language | Python |
| Agent Framework | LangGraph (ReAct agents) |
| LLM Orchestration | LangChain |
| Primary AI Model | OpenAI ChatGPT |
| Domain-specific AI | Groq API |
| Configuration | YAML, JSON |
| Environment | dotenv |
| Type Handling | typing_extensions |



## Architecture

![Design Diagram](design_docs/design.png)


# Tutorial: My Making Of Project Manager AI Agent

## Prerequisites
- Python installed on your system.
- A basic understanding of virtual environments and command-line tools.

## Steps

1. **Virtual Environment Setup:**
   - Create a dedicated virtual environment for our project:
   
     ```bash
     python -m venv My-Making-Of-Project-Manager-AI-Agent
     ```
   - Activate the environment:
   
     - Windows:
       ```bash
          My-Making-Of-Project-Manager-AI-Agent\Scripts\activate        
       ```
     - Unix/macOS:
       ```bash
       source My-Making-Of-Project-Manager-AI-Agent/bin/activate
       ```
   

# Installation and Setup Guide

**Install Project Dependencies:**

Follow these steps to set up and run the  "My Making Of Project Manager AI Agent"

1. Navigate to your project directory:
   ```
   cd path/to/your/project
   ```
   This ensures you're in the correct location for the subsequent steps.

2. Install the required dependencies:
   ```
   pip install -r requirements.txt   
   ```
   This command installs all the necessary Python packages listed in the requirements.txt file.


# Run - Hands-On Guide: My Making Of Project Manager AI Agent
  
   ```
   python main.py   
   ```
   
## Closing Thoughts

The future of AI in business lies in these collaborative systems where multiple specialized agents work together, each bringing domain expertise to complex problems. We’re moving beyond single-purpose AI tools toward intelligent ecosystems that mirror human team structures. Soon, these systems will extend beyond planning into execution — monitoring progress, adapting to changes, and even participating in decision-making.

Healthcare is just the beginning; similar approaches will transform financial services, manufacturing, and other industries. As these technologies mature, the boundary between human and AI contributions will blur, creating truly augmented organizations where people and machines collaborate as partners.
