class AgentConfig: 
    summarizer:dict = {'provider': 'ollama', 
                       'llm_config': {
                           'model': 'qwen2.5:1.5b'
                       }}
    content_creator:dict = {'provider': 'ollama', 
                       'llm_config': {
                           'model': 'qwen2.5:1.5b'
                       }}
    supervisor:dict = {'provider': 'gemini', 
                       'llm_config': {
                           'model': 'models/gemini-1.5-flash'
                       }}

    # summarizer:dict = {'provider': 'ollama', 
    #                    'llm_config': {
    #                        'model': 'qwen2.5:1.5b'
    #                    }}
    # content_creator:dict = {'provider': 'gemini', 
    #                    'llm_config': {
    #                        'model': 'models/gemini-1.5-flash'
    #                    }}
    # supervisor:dict = {'provider': 'groq', 
    #                    'llm_config': {
    #                        'model': 'llama3-8b-8192'
    #                    }}
    
"""
                    (
                    "system",
                    "Given the conversation above, who should act next?"
                    "Or should we FINISH? Select one of: {options}",
                    ),
"""