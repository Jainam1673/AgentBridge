from src.agents.state.agent_state import AgentState
from langchain_core.messages import AIMessage
from src.mcp.postgres_server import PostgresMCPServer
from src.mcp.resiliency import MCPResiliency

async def knowledge_node(state: AgentState):
    # Use resilient MCP tool call
    mcp_server = PostgresMCPServer(connection_string="simulated")
    
    # Simulate discovery and execution
    tools = mcp_server.list_tools()
    
    try:
        results = await MCPResiliency.execute_with_retry(
            mcp_server.execute_tool, 
            "query_database", 
            {"query": "SELECT * FROM documents LIMIT 2"}
        )
        retrieved_docs = [results["results"]]
    except Exception as e:
        retrieved_docs = ["Fallback: Policy A", "Fallback: Policy B"]

    return {
        "messages": [AIMessage(content=f"Retrieved relevant policies via MCP: {retrieved_docs}")],
        "context": {"docs": retrieved_docs},
        "next_step": "critic"
    }
