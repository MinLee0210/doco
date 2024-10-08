from abc import ABC
from doco.components.llms import AgentFactory

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class BaseAgent(ABC): 
    
    def __init__(self, 
                 provider:str, 
                 llm_config:dict,
                 tools:list,
                 system_prompt:str, 
                 instruction:str): 
        
        # For llm's calling
        self.provider = provider
        self.llm_config = llm_config

        # For llm's persona
        self.tools = tools
        self.system_prompt = system_prompt
        self.instruction = instruction


    # TODO: Separate tool vs non-tool agent
    def _build_agent(self, llm, tools:list, system_prompt:str, instruction:str): 
        raise NotImplementedError


    def build_agent(self, provider, llm_config, tools:list, system_prompt:str, instruction:str):
        """Create an agent: it's core and llm's provider adaptability."""
        llm = AgentFactory.build(provider=provider,
                                      llm_config=llm_config)
        agent = self._build_agent(llm=llm, 
                                  tools=tools,
                                  system_prompt=system_prompt, 
                                  instruction=instruction)
        return agent


    def build(self): 
        agent = self.build_agent(provider=self.provider, 
                                 llm_config=self.llm_config, 
                                 tools=self.tools, 
                                 system_prompt=self.system_prompt, 
                                 instruction=self.instruction)
        return agent
    