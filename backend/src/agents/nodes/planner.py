from src.agents.state.agent_state import AgentState
from langchain_core.messages import AIMessage

async def planner_node(state: AgentState):
    # Logic to decompose task and decide next step
    # For now, just a dummy transition
    return {
        "messages": [AIMessage(content="Planning next steps...")],
        "next_step": "knowledge",
        "plan": ["Retrieve relevant documents", "Summarize findings"]
    }
