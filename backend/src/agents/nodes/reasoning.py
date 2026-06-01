from src.agents.state.agent_state import AgentState
from langchain_core.messages import AIMessage

async def reasoning_node(state: AgentState):
    """
    Implements the 'Reason' part of the ReAct pattern.
    Analyzes the current state and decides whether to retrieve information,
    execute an action, or move to final criticism.
    """
    # Simulate internal reasoning
    last_message = state["messages"][-1].content if state["messages"] else ""
    
    if "Retrieved" in last_message:
        next_step = "critic" # Have info, let's validate
    elif "Planning" in last_message:
        next_step = "knowledge" # Just started, need info
    else:
        next_step = "action" # Need to do something
        
    return {
        "messages": [AIMessage(content=f"Reasoning: Decided to proceed to {next_step}")],
        "next_step": next_step
    }
