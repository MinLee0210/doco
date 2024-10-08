import pytest
from langchain_core.messages import HumanMessage

@pytest.mark.usefixtures("init_llm")
class Test_pLLM(): 
    def test_query(self): 
        query = "Tell me a joke"
        result = self.llm.invoke([HumanMessage(content=query)])
        assert result is not None and isinstance(result.content, str)