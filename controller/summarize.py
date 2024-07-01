from doco.agents.gemini import GeminiAgent
from doco.agents.groq import GroqAgent
from doco.prompts import base_summarize


def gemini_summarize(api_key, payload, **kwargs): 
    agent = GeminiAgent(api_key=api_key)
    prompt = base_summarize + '\n' + payload
    result = agent.invoke(prompt=prompt)
    return result

def groq_summarize(api_key, payload, **kwargs): 
    agent = GroqAgent(api_key=api_key)
    prompt = base_summarize + '\n' + payload
    result = agent.invoke(prompt=prompt)
    return result