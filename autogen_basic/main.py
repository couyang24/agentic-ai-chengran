import autogen

# 1. Configuration
# Purpose: Setup the LLM connection.
# Improvement: Use 'filter_func' to switch models dynamically based on cost or complexity.
config_list = [{"model": "gpt-4", "api_key": "YOUR_API_KEY"}]

# 2. Define Agents
# AssistantAgent: The LLM brain.
# UserProxyAgent: Acts on behalf of the human, can execute code, and asks for help if stuck.
# Improvement: Set 'human_input_mode' to "NEVER" for fully autonomous agents (use with caution).
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
# user_proxy.initiate_chat(assistant, message="Write a python script to plot the stock price of NVDA.")
