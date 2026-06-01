from src.agents.state.agent_state import AgentState
from langchain_core.messages import AIMessage

async def action_node(state: AgentState):
    # Logic to execute workflows (create tickets, update docs)
    # Simulated action
    ticket_id = "JIRA-90210"
    return {
        "messages": [AIMessage(content=f"Successfully created Jira ticket: {ticket_id}")],
        "next_step": "critic"
    }
