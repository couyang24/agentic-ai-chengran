from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

# 0. Initialize LLM
llm = ChatGroq(
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

# 1. Define State
class State(TypedDict):
    input: str
    output: str

# 2. Define Nodes (Functions)
def research_node(state: State):
    print("---Researching using Groq---")
    response = llm.invoke(f"Give me a 1-sentence fun fact about {state['input']}")
    return {"output": response.content}

def formatting_node(state: State):
    print("---Formatting Output---")
    return {"output": f"FUN FACT: {state['output']}"}

# 3. Build the Graph
workflow = StateGraph(State)

workflow.add_node("research", research_node)
workflow.add_node("format", formatting_node)

workflow.set_entry_point("research")
workflow.add_edge("research", "format")
workflow.add_edge("format", END)

app = workflow.compile()
result = app.invoke({"input": "AI Agents"})
print(result["output"])
