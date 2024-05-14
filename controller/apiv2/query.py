"""
    An example can be found in /notebooks dir. Otherwise, I suggest reading this writint 
    to have a clearer vision about the implementation: 
        https://medium.com/@octoopt_8888/text-summarization-with-llm-f69b4f2ccb3e
"""

from agent import generate_model, config, Agent, Generator

model, tokenizer = generate_model(config['model_id'][0], config)

template = """
              Write a summary of the following text delimited by triple backticks.
              Return your response which covers the key points of the text.
              ```{text}```
              SUMMARY:
           """


agent = Agent(model, tokenizer)
llm_agent = Generator(config, agent, template)

# generated_sample = llm_agent.generate(doc)

