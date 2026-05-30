from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, END

# 1. Define State
# Purpose: This object is passed between every node. It's the "memory" of the graph.
# Improvement: Add a 'history' list to track previous decisions for complex reasoning.
class State(TypedDict):
    input: str
    output: str

# 2. Define Nodes (Functions)
# Purpose: Individual steps in your process.
def logic_step_1(state: State):
    print("---Processing Step 1---")
    return {"output": state["input"] + " -> Processed by 1"}

def logic_step_2(state: State):
    print("---Processing Step 2---")
    return {"output": state["output"] + " -> Processed by 2"}

# 3. Build the Graph
# Purpose: Defining the "Map" of the AI's logic.
# Improvement: Add 'add_conditional_edges' to create loops (e.g., if answer is bad, go back to step 1).
workflow = StateGraph(State)

workflow.add_node("step_1", logic_step_1)
workflow.add_node("step_2", logic_step_2)

workflow.set_entry_point("step_1")
workflow.add_edge("step_1", "step_2")
workflow.add_edge("step_2", END)

# app = workflow.compile()
# result = app.invoke({"input": "Hello Agent"})
# print(result)
