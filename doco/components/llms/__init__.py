from ._gemini import GeminiNode
from ._groq import GroqNode
from ._ollama import OllamaNode


class AgentFactory:

    @staticmethod
    def build(provider, llm_config): 
        try: 
            match provider: 
                case 'gemini': 
                    return GeminiNode(**llm_config)
                case 'groq': 
                    return GroqNode(**llm_config)
                case 'ollama': 
                    return OllamaNode(**llm_config)
        except:
            raise ValueError(
                "There are faults in your input. It could be `provider`, `model_name`, ..."
            )
