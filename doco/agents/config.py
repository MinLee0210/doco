class AgentConfig: 
    summarizer:dict = {'provider': 'ollama', 
                       'llm_config': {
                           'model': 'qwen2.5:1.5b'
                       }}
    content_creator:dict = {'provider': 'gemini', 
                       'llm_config': {
                           'model': 'models/gemini-1.5-flash'
                       }}
    supervisor:dict = {'provider': 'ollama', 
                       'llm_config': {
                           'model': 'qwen2.5:1.5b'
                       }}