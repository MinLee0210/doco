# Testing simple case: whether the function is runnable or not.


from langchain_core.messages import HumanMessage
from doco.agents.summarizer.basic import Summarizer
from doco.agents.content_creator.basic import ContentCreator


def test_summarizer_agent(llm_summarizer): 
    summarizer_agent = Summarizer().build()
    result = summarizer_agent.invoke([HumanMessage(content=llm_summarizer)])
    assert result is not None and isinstance(result.content, str)



def test_content_creator_agent(llm_content_creator): 
    contentcreator_agent = ContentCreator().build()
    result = contentcreator_agent.invoke([HumanMessage(content=llm_content_creator)])
    assert result is not None and isinstance(result.content, str)