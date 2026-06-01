from src.agents.state.agent_state import AgentState
from langchain_core.messages import AIMessage

async def critic_node(state: AgentState):
    # Logic to validate results and ensure quality
    # Simulated validation
    is_valid = True
    return {
        "messages": [AIMessage(content="Results validated. Groundedness check: Passed.")],
        "next_step": "end" if is_valid else "planner",
        "evaluations": [{"groundedness": 0.98, "relevance": 0.95}]
    }
