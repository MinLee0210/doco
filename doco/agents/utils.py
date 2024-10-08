
from langchain_core.messages import HumanMessage, trim_messages

def agent_node(state, agent, name):
    result = agent.invoke(state)
    return {
        "messages": [HumanMessage(content=result["messages"][-1].content, name=name)]
    }

def create_trimmer(llm, max_tokens:int=100000, include_system:bool=True, strategy="last") -> trim_messages: 
    return trim_messages(
    max_tokens=max_tokens,
    strategy=strategy,
    token_counter=llm,
    include_system=include_system,
    )
