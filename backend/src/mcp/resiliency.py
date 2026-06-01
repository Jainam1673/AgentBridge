from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import logging

logger = logging.getLogger(__name__)

class MCPResiliency:
    """
    Implements production-grade resiliency patterns for MCP tool execution.
    Handles transient network failures and service rate limits.
    """
    
    @staticmethod
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type((ConnectionError, TimeoutError)),
        before_sleep=lambda retry_state: logger.warning(f"Retrying MCP tool call: attempt {retry_state.attempt_number}")
    )
    async def execute_with_retry(func, *args, **kwargs):
        return await func(*args, **kwargs)

class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failures = 0
        self.last_failure_time = 0
        self.state = "CLOSED" # CLOSED, OPEN, HALF_OPEN

    def record_success(self):
        self.failures = 0
        self.state = "CLOSED"

    def record_failure(self):
        self.failures += 1
        import time
        self.last_failure_time = time.time()
        if self.failures >= self.failure_threshold:
            self.state = "OPEN"
            logger.error("Circuit Breaker OPEN: MCP Server is failing.")

    def can_execute(self) -> bool:
        if self.state == "CLOSED":
            return True
        import time
        if self.state == "OPEN" and (time.time() - self.last_failure_time) > self.recovery_timeout:
            self.state = "HALF_OPEN"
            return True
        return False
