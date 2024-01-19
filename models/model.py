"""
    https://huggingface.co/docs/api-inference/detailed_parameters#summarization-task
"""

class Model: 
    API_INFERENCE="https://api-inference.huggingface.co/models/"
    MODEL = {
        "fb_bart": "facebook/bart-large-cnn",
        "falcon_ai": "Falconsai/text_summarization", # Quite slow
        "pegasus_xsum_gnad": "Einmalumdiewelt/PegasusXSUM_GNAD"
    }
    EXTRACTOR = {
        "h2_trans": "transformer3/H2-keywordextractor"
    }
