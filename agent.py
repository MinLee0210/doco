from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import OpenAI

from typing import Union

class AgentConfig: 
    def __init__(self,  api_key: str, 
                        model: str, 
                        max_tokens: int, 
                        temperature: float, 
                        top_p: float,
                        top_k: float,
                        frequency_penalty: float, 
                        presence_penalty: float): 
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.top_k = top_k
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

class Agent: 
    def __init__(self, api_key: str, 
                        model: str, 
                        max_tokens: int, 
                        temperature: float, 
                        top_p: float,
                        top_k: float,
                        frequency_penalty: float, 
                        presence_penalty: float,
                        config: Union[AgentConfig, None], 
                        provider: str): 

        if not config: 
            self.config = config
        else: 
            self.config = AgentConfig(api_key=api_key, 
                                      model=model, 
                                      max_tokens=max_tokens,
                                      temperature=temperature,
                                      top_p=top_p,
                                      top_k=top_k, 
                                      frequency_penalty=frequency_penalty,
                                      presence_penalty=presence_penalty)
            
    
        if provider == 'Google' or provider == None: 
            self.llm = ChatGoogleGenerativeAI(**self.config.__dict__)
        elif provider == 'OpenAI': 
            self.llm = OpenAI(**self.config.__dict__)
        else: 
            raise f"Your model is beyond what we currently have."