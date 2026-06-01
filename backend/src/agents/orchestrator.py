from langgraph.graph import StateGraph, END
from src.agents.state.agent_state import AgentState
from src.agents.nodes.planner import planner_node
from src.agents.nodes.reasoning import reasoning_node
from src.agents.nodes.knowledge import knowledge_node
from src.agents.nodes.action import action_node
from src.agents.nodes.critic import critic_node

def create_agent_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("planner", planner_node)
    workflow.add_node("reasoning", reasoning_node) # Explicit ReAct node
    workflow.add_node("knowledge", knowledge_node)
    workflow.add_node("action", action_node)
    workflow.add_node("critic", critic_node) # Self-reflection node

    workflow.set_entry_point("planner")

    workflow.add_edge("planner", "reasoning")
    
    workflow.add_conditional_edges(
        "reasoning",
        lambda x: x["next_step"],
        {
            "knowledge": "knowledge",
            "action": "action",
            "critic": "critic"
        }
    )

    workflow.add_edge("knowledge", "reasoning") # ReAct loop
    workflow.add_edge("action", "reasoning")    # ReAct loop
    
    workflow.add_conditional_edges(
        "critic",
        lambda x: x["next_step"],
        {
            "planner": "planner", # Hierarchical correction
            "end": END
        }
    )

    return workflow.compile()
