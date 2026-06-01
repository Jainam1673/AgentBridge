from langgraph.graph import StateGraph, END
from src.agents.state.agent_state import AgentState
from src.agents.nodes.planner import planner_node
from src.agents.nodes.knowledge import knowledge_node
from src.agents.nodes.action import action_node
from src.agents.nodes.critic import critic_node

def create_agent_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("planner", planner_node)
    workflow.add_node("knowledge", knowledge_node)
    workflow.add_node("action", action_node)
    workflow.add_node("critic", critic_node)

    workflow.set_entry_point("planner")

    workflow.add_conditional_edges(
        "planner",
        lambda x: x["next_step"],
        {
            "knowledge": "knowledge",
            "action": "action",
            "end": END
        }
    )

    workflow.add_edge("knowledge", "critic")
    workflow.add_edge("action", "critic")
    
    workflow.add_conditional_edges(
        "critic",
        lambda x: x["next_step"],
        {
            "planner": "planner",
            "end": END
        }
    )

    return workflow.compile()
