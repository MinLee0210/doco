"Gemini Module"

import os
from langchain_google_genai import ChatGoogleGenerativeAI

class GeminiNode(ChatGoogleGenerativeAI):
    """
    A wrapper for the ChatGoogleGenerativeAI class that
    provides default configuration and could be extended with additional methods
    if needed.

    Args:
        llm_config (dict): Configuration parameters for the language model.
    """

    def __init__(self, **llm_config):
        if 'api_key' in llm_config:
            llm_config['google_api_key'] = llm_config.pop('api_key')
        else: 
            llm_config['google_api_key'] = os.environ.get("GOOGLE_API_KEY")
        super().__init__(**llm_config)