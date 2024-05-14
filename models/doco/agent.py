from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

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
    def __init__(self): 
        pass

    @classmethod
    def call(self, api_key: str, 
                    model: str, 
                    max_tokens: int=512, 
                    temperature: float=1, 
                    top_p: float=1,
                    top_k: float=3,
                    frequency_penalty: float=1, 
                    presence_penalty: float=1,
                    config: Union[AgentConfig, None]=None, 
                    provider: str='Google'): 

        if config is not None: 
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

            # Small change due to the difference in naming parameters
            google_config = self.config.__dict__
            google_config['google_api_key'] = google_config['api_key']
            del google_config['api_key']
            
            llm = ChatGoogleGenerativeAI(**google_config)
        elif provider == 'OpenAI': 
            openai_config = self.config.__dict__
            llm = ChatOpenAI(**openai_config)
        else: 
            raise f"Your model is beyond what we currently have."
        return llm