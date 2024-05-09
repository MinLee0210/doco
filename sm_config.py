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