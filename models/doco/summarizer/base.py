"""
Reference: 
1. https://github.com/gkamradt/langchain-tutorials/blob/main/data_generation/5%20Levels%20Of%20Summarization%20-%20Novice%20To%20Expert.ipynb
"""

class SummarizerBase:
    def __init__(self, llm): 
        self.llm = llm

    def summarize(self, text): 
        raise ValueError("Step needs to be implemented by the agent")
