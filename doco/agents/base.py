from abc import ABC

"""Set of constants."""
DEFAULT_CANDIDATE_COUNT = 1
DEFAULT_TEMPERATURE = 1.
DEFAULT_TOP_K = 20
DEFAULT_TOP_P = 0.8
DEFAULT_NUM_OUTPUTS = 5096  # tokens


class BaseAgent(): 

    def set_model(self, api_key, **kwargs): 
        pass

    def get_models(self): 
        pass

    def invoke(self, prompt, **kwargs): 
        pass