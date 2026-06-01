from src.agents.state.agent_state import AgentState
from langchain_core.messages import AIMessage

async def knowledge_node(state: AgentState):
    # Logic to retrieve data from BigQuery/Postgres/VectorStore
    # Simulated retrieval
    retrieved_docs = ["Policy A: Use AES-256", "Policy B: Rotate keys every 90 days"]
    return {
        "messages": [AIMessage(content=f"Retrieved relevant policies: {', '.join(retrieved_docs)}")],
        "context": {"docs": retrieved_docs},
        "next_step": "critic"
    }
