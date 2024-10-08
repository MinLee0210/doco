import operator
from typing import Annotated, List, Tuple, Sequence
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage


# The agent state is the input to each node in the graph
class AgentState(TypedDict):
    # The annotation tells the graph that new messages will always
    # be added to the current states
    messages: Annotated[Sequence[BaseMessage], operator.add]
    # The 'next' field indicates where to route to next
    next: str

# ===== SUPERVISOR ===== 
members = ['Summarizer', "ContentCreator"]
# Our team supervisor is an LLM node. It just picks the next agent to process
# and decides when the work is completed
options = ["FINISH"] + members