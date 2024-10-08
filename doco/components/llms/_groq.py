"GROQ Module"
import os
from langchain_groq import ChatGroq

class GroqNode(ChatGroq):
    """
    A wrapper for the ChatGroq class that
    provides default configuration and could be extended with additional methods
    if needed.

    Args:
        llm_config (dict): Configuration parameters for the language model.
    """

    def __init__(self, **llm_config):
        if 'api_key' in llm_config:
            llm_config['groq_api_key'] = llm_config.pop('api_key')
        else: 
            llm_config['groq_api_key'] = os.environ.get("GROQ_API_KEY")
        super().__init__(**llm_config)