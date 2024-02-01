import time

import numpy as np

import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

from langchain import LLMChain, HuggingFacePipeline, PromptTemplate

config={
    "model_id": ["TheBloke/Llama-2-7b-Chat-GPTQ",
                 "TheBloke/Llama-2-7B-AWQ",
                 "TheBloke/Llama-2-7B-GGUF",
                 "TheBloke/Llama-2-7B-GGML",
                 "TheBloke/Llama-2-7B-fp16",
                 "TheBloke/Llama-2-7B-GPTQ",
                 "TheBloke/llama-2-7B-Guanaco-QLoRA-AWQ",
                 "TheBloke/Llama-2-7B-AWQ"],
    "hf_token": "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",
    "model": {
        "temperature": 0.7, # [0, 0.7, .0.9, 1.1, 1.3]  Testing iteratively.
        "max_length": 3000,
        "top_k": 10,
        "num_return": 1
    },
    "dataset": [
        "billsum",
        "cnn_dailymail",
        "big_patent"
    ],
    "eval": ['rouge', "bertscore", 'meteor']
}
  
def generate_model(model_id, config):
  print(f"Setting up model {model_id}")
  model = AutoModelForCausalLM.from_pretrained(model_id, token=config['hf_token'], use_safetensors=True,
                            device_map='auto', trust_remote_code=True)
  tokenizer = AutoTokenizer.from_pretrained(model_id, token=config['hf_token'],
                                            device_map='auto', trust_remote_code=True)
  return model, tokenizer

class Agent:
  def __init__(self, model, tokenizer):
    self.model = model
    self.tokenizer = tokenizer

  def __repr__(self):
    return f'Model {self.model.__class__.__name__}'
  
class Generator:
  def __init__(self, config, agent: Agent, template):
    self.agent = agent
    pipeline = transformers.pipeline(
        "text-generation",
        model=self.agent.model,
        tokenizer=self.agent.tokenizer,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto",
        max_length=config['model']['max_length'],
        do_sample=True,
        top_k=config['model']['top_k'],
        num_return_sequences=config['model']['num_return'],
        pad_token_id=self.agenttokenizer.eos_token_id
    )
    llm = HuggingFacePipeline(pipeline=pipeline, model_kwargs={'temperature': config['model']['temperature']})
    prompt = PromptTemplate(template=template, input_variables=["text"])
    self.llm_chain = LLMChain(prompt=prompt, llm=llm)

  def generate(self, text):
    result = self.llm_chain.invoke(text)
    return result