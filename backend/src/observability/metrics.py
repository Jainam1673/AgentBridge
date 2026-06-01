from pydantic import BaseModel
from typing import Optional
import time

class LLMMetrics(BaseModel):
    tokens_per_sec: float
    time_to_first_token_ms: float
    total_latency_ms: float
    input_tokens: int
    output_tokens: int
    estimated_cost_usd: float

class PerformanceTracker:
    @staticmethod
    def calculate_cost(input_tokens: int, output_tokens: int, model: str = "gemini-1.5-pro") -> float:
        # Simplified Google Cloud pricing logic
        rates = {
            "gemini-1.5-pro": {"input": 0.00125 / 1000, "output": 0.00375 / 1000},
            "gemini-1.5-flash": {"input": 0.000125 / 1000, "output": 0.000375 / 1000}
        }
        model_rates = rates.get(model, rates["gemini-1.5-pro"])
        return (input_tokens * model_rates["input"]) + (output_tokens * model_rates["output"])

    @staticmethod
    def generate_metrics(
        start_time: float, 
        ttft_time: float, 
        end_time: float, 
        input_tokens: int, 
        output_tokens: int
    ) -> LLMMetrics:
        total_latency = (end_time - start_time) * 1000
        ttft = (ttft_time - start_time) * 1000
        tokens_sec = output_tokens / (end_time - ttft_time) if (end_time - ttft_time) > 0 else 0
        
        return LLMMetrics(
            tokens_per_sec=round(tokens_sec, 2),
            time_to_first_token_ms=round(ttft, 2),
            total_latency_ms=round(total_latency, 2),
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            estimated_cost_usd=round(PerformanceTracker.calculate_cost(input_tokens, output_tokens), 6)
        )
