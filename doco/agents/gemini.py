from typing import Union

try: 
    import google.generativeai as genai

except: 
    raise "google.generativeai is not installed. Try `pip install google.generativeai`"

from doco.agents.base import (BaseAgent, 
                         DEFAULT_CANDIDATE_COUNT, DEFAULT_NUM_OUTPUTS, DEFAULT_TEMPERATURE,DEFAULT_TOP_K, DEFAULT_TOP_P)
from google.generativeai.types import HarmCategory, HarmBlockThreshold


class GeminiAgent(BaseAgent): 
    def __init__(self, api_key, 
                    model_name:str="gemini-1.5-flash-latest",
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

        self.safety_settings = {
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
        }
        self.model = self.set_model(api_key=api_key, 
                                    model_name=model_name)
        
    def get_models(self):
        models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                models.append(m)
        return models
                
    def set_model(self, api_key, model_name):
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name=model_name)
        return model
    
    def invoke(self, prompt, text_only:bool=True):
        messages = []
        user_msg = {
            "role": "user",
            "parts": prompt
        }
        if hasattr(self, "system_prompt"):
            messages.append(self.system_prompt)
        else:
            messages.append(user_msg)
        response = self.model.generate_content(prompt, 
                                               generation_config=genai.GenerationConfig(**self.generation_config), 
                                                safety_settings=self.safety_settings)
        if text_only: 
            return response.text
        return response