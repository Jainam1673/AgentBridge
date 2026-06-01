from typing import List, TypedDict, Annotated, Union
from langchain_core.messages import BaseMessage
import operator

class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]
    next_step: str
    plan: List[str]
    context: dict
    evaluations: List[dict]
