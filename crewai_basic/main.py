from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

# 0. Initialize LLM & Tools
# Using Groq for free/fast inference
llm = ChatGroq(
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-70b-8192"
)

search_tool = SerperDevTool()

# 1. Define Agents
researcher = Agent(
  role='Senior Research Analyst',
  goal='Uncover cutting-edge developments in AI agents',
  backstory="""You are an expert at a technology think tank.
  Your expertise lies in identifying emerging trends.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool],
  llm=llm
)

writer = Agent(
  role='Tech Content Strategist',
  goal='Craft compelling content on AI advancements',
  backstory="""You are a renowned content strategist known for 
  making complex topics simple.""",
  verbose=True,
  allow_delegation=True,
  llm=llm
)

# 2. Define Tasks
# Purpose: Specific assignments for agents.
# Improvement: Use 'context' to pass the output of one task directly as the requirement for another.
task1 = Task(description="Analyze the 2024 trends in Agentic AI.", agent=researcher, expected_output="A list of 5 key trends.")
task2 = Task(description="Write a blog post based on the analysis.", agent=writer, expected_output="A 500-word blog post.")

# 3. Assemble the Crew
# Purpose: Management layer that dictates how agents interact (Sequential vs Hierarchical).
# Improvement: Switch process=Process.hierarchical to add a "Manager" agent who oversees the work.
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  process=Process.sequential
)

# result = crew.kickoff()
# print(result)
