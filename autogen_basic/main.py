import autogen
import os
from dotenv import load_dotenv

load_dotenv()

# 1. Configuration for Groq
# Purpose: Setup the connection to Groq's high-speed inference.
config_list = [
    {
        "model": "llama-3.3-70b-versatile",
        "api_key": os.getenv("GROQ_API_KEY"),
        "base_url": "https://api.groq.com/openai/v1",
    }
]

# 2. Define Agents
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list},
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "coding", "use_docker": False},
)

# 3. Start Conversation
# Purpose: Solve a problem through dialogue.
# Improvement: Use 'GroupChat' to involve 3+ agents in a round-robin or AI-selected sequence.
user_proxy.initiate_chat(assistant, message="Write a python script to plot the stock price of NVDA.")
