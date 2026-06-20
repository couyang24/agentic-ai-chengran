from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool
import crewai.llms.cache
import os
from dotenv import load_dotenv

# Monkey-patch to fix Groq compatibility issue
crewai.llms.cache.mark_cache_breakpoint = lambda x: x

load_dotenv()

# Initialize LLM (using Groq)
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.7
)

# Initialize Tool
search_tool = SerperDevTool()

# 2. Define Agents
# Set verbose=False and add allow_delegation=False to stabilize tool calling
researcher = Agent(
    role='Research Analyst',
    goal='Uncover the latest facts on {topic}',
    backstory='You are an expert researcher at a top tech firm.',
    tools=[search_tool],
    llm=llm,
    verbose=False,
    allow_delegation=False
)

writer = Agent(
    role='Content Writer',
    goal='Write a compelling report based on research',
    backstory='You are a famous journalist known for engaging stories.',
    llm=llm,
    verbose=True
)

# 3. Define Tasks
research_task = Task(
    description='Analyze the current state of {topic}.',
    expected_output='A bulleted list of 3 key insights.',
    agent=researcher
)

writing_task = Task(
    description='Write a 200-word report on {topic} based on the research.',
    expected_output='A polished blog post.',
    agent=writer,
    context=[research_task] # This passes research_task output to the writer
)

# 4. Assemble the Crew
my_crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential # Agents work one after another
)

# 5. Execution (Interactive)
if __name__ == "__main__":
    topic = input("What topic would you like to research? ")

    print(f"\n--- Starting crew to research: {topic} ---\n")
    result = my_crew.kickoff(inputs={'topic': topic})

    print("\n\n########################")
    print("## RESULT ##")
    print("########################\n")
    print(result)
