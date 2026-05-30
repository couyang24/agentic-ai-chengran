# Agentic AI Exploration - Chengran

Welcome to your agentic AI sandbox. This folder contains templates for different agent frameworks to help you understand their unique architectures and strengths.

## Current Templates

1. **CrewAI (`/crewai_basic`)**: Best for role-based collaboration. Think of it like a "company" where you hire different specialists.
2. **AutoGen (`/autogen_basic`)**: Best for conversational agents that can talk to each other and the user to solve tasks.
3. **LangGraph (`/langgraph_basic`)**: Best for complex, state-driven workflows where you need precise control over the logic flow (loops, conditions).

## Why "Agentic"?
Standard LLM apps are "one-shot" (Prompt -> Answer). Agentic apps use **cycles**:
1. **Plan**: Decide what to do.
2. **Act**: Use a tool (Search, Code, API).
3. **Observe**: See the result.
4. **Iterate**: Adjust the plan based on the result.

## How to use this folder
Each subfolder contains a `main.py` with a basic implementation. You will need an API key (like OpenAI or Anthropic) in a `.env` file at the root.
