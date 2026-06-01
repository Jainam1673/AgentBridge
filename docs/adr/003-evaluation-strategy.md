# ADR 003: LLM-as-a-Judge for Automated Evaluation (Evals)

## Status
Accepted

## Context
Traditional heuristic-based evaluations (e.g., string matching, BLEU) are insufficient for measuring the "Groundedness" and "Safety" of complex agentic responses in an enterprise context.

## Decision
We will implement an **LLM-as-a-Judge** framework using Gemini 1.5 Flash as the primary evaluator.

## Rationale
- **Semantic Understanding:** Gemini can assess if a response is "grounded" in a retrieved document even if the phrasing differs.
- **Cost Efficiency:** Using a "Flash" model for evaluations maintains high accuracy while minimizing the operational cost of the evaluation pipeline.
- **Consistency:** By standardizing on a structured evaluation prompt (Rubric), we ensure that measurements are comparable across different agent versions and tenants.

## Consequences
- Evaluation latency: Running an extra LLM call for every response increases the total time-to-response for the user.
- Bias: The judge model may have inherent biases or "hallucinate" its own evaluation scores. We mitigate this with a "Critic" agent loop.
