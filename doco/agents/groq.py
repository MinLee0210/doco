from typing import Optional, Union

try:
    from groq import Groq
except ImportError:
    raise ValueError(
        "Groq is not installed. Please install it with "
        "`pip install 'groq'`."
    )

from doco.agents.base import (BaseAgent, 
                         DEFAULT_CANDIDATE_COUNT, DEFAULT_NUM_OUTPUTS, DEFAULT_TEMPERATURE,DEFAULT_TOP_K, DEFAULT_TOP_P)

class GroqAgent(BaseAgent):

    def __init__(self,
                api_key: Optional[str] = None,
                model_name: str='llama3-8b',
                temperature:float=DEFAULT_TEMPERATURE, 
                max_tokens:int=DEFAULT_NUM_OUTPUTS, 
                top_k:float=DEFAULT_TOP_K, 
                top_p:float=DEFAULT_TOP_P,
                candidate_count:int=DEFAULT_CANDIDATE_COUNT,
                system_instructions:Union[str, None]=None):
        super().__init__()

        self.generation_config = {
            "candidate_count": candidate_count,
            "max_output_tokens": max_tokens,
            "temperature": temperature,
            "top_k": top_k,
            "top_p": top_p,
        }
        if system_instructions:
            self.system_prompt = {"role": "system",
                                  "parts": [system_instructions]}
            
        self.supported_models = {
        "llama3-8b": "llama3-8b-8192",
        "llama3-70b": "llama3-70b-8192",
        "mixtral-8x7b": "mixtral-8x7b-32768",
        "gemma-7b": "gemma-7b-it",
        }
        if model_name not in self.supported_models: 
            return f"Your input {model_name} is not supported. We support {self.get_models()}"
        else: 
            self.model_name = model_name
        self.model = self.set_model(api_key)


    def set_model(self, api_key, max_retries:int=5):
        model = Groq(api_key=api_key, max_retries=max_retries)
        return model

    def get_models(self):
        return self.supported_models
    

    def invoke(self, prompt, text_only:bool=True):
        messages = []
        usr_msg = {"role": "user",
                   "content": prompt}

        if hasattr(self, "system_prompt"):
            messages.append(self.system_prompt)
        else:
            messages.append(usr_msg)

        chat_completion = self.model.chat.completions.create(messages=messages,
                                                            model=self.model_name, 
                                                            **self.generation_config)
        if text_only: 
            return chat_completion.choices[0].message.content
        return chat_completion