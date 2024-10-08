from ._gemini import GeminiNode
from ._groq import GroqNode
from ._ollama import OllamaNode
from ._sambanova import SambaNovaNode
from ._cohere import CohereNode

class AgentFactory:

    @staticmethod
    def call_model(provider, llm_config): 
        try: 
            match provider: 
                case 'gemini': 
                    return GeminiNode(**llm_config)
                case 'groq': 
                    return GroqNode(**llm_config)
                case 'ollama': 
                    return OllamaNode(**llm_config)
                case 'sambanova': 
                    return SambaNovaNode(**llm_config)
                case 'cohere': 
                    return CohereNode(**llm_config)
        except:
            raise ValueError(
                "There are faults in your input. It could be `provider`, `model_name`, ..."
            )
