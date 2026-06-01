from src.agents.state.agent_state import AgentState
from langchain_core.messages import AIMessage
from src.observability.metrics import PerformanceTracker
import time

async def planner_node(state: AgentState):
    start_time = time.time()
    
    # Logic to decompose task
    # Simulate thinking time
    time.sleep(0.1)
    
    ttft_time = time.time()
    
    # End simulation
    end_time = time.time()
    
    metrics = PerformanceTracker.generate_metrics(
        start_time=start_time,
        ttft_time=ttft_time,
        end_time=end_time,
        input_tokens=150,
        output_tokens=50
    )
    
    return {
        "messages": [AIMessage(content=f"Plan generated. Metrics: {metrics.json()}")],
        "next_step": "knowledge",
        "plan": ["Retrieve relevant documents", "Summarize findings"],
        "context": {"metrics": metrics.dict()}
    }
