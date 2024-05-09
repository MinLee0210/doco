import prompt

from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_core.output_parsers import StrOutputParser

class SummarizerBase:
    def __init__(self, llm): 
        self.llm = llm

    def summarize(self): 
        ...

class LangChainSummarizer(SummarizerBase):
    def __init__(self): 
        super().__init__
        self.supported_types = ['stuff', 'map_duce', 'refine']

    def get_chain(self, chain_type):
        try: 
            # For those who want to implement the chain from scratch, here is the link: https://python.langchain.com/docs/use_cases/summarization/
            chain = load_summarize_chain(self.llm,
                                        chain_type=chain_type)
            return chain
        except Exception as e: 
            return e
        
    def summarize(self, text:str, chain_type:str):
        try: 
            sm_chain = self.get_chain(chain_type)
            result = sm_chain.invoke(input=text) 
            return result
        except Exception as e: 
            return e
        
class DoCoSM(SummarizerBase): 
    def __init__(self): 
        super().__init__
        
    def get_chain(self, llm, prompt, output_parser:bool=True):
        if output_parser: 
            output_parser = StrOutputParser()
            chain = prompt | llm | output_parser
        else: 
            chain = prompt | llm 
        return chain

    def get_cod(self): 
        template = """
        Article: {text}
        You will generate increasingly concise, entity-dense summaries of the
        above article.
        Repeat the following 2 steps 5 times.
        Step 1. Identify 1-3 informative entities (";" delimited) from the article
        which are missing from the previously generated summary.
        Step 2. Write a new, denser summary of identical length which covers every
        entity and detail from the previous summary plus the missing entities.

        A missing entity is:
        - relevant to the main story,
        - specific yet concise (5 words or fewer),
        - novel (not in the previous summary),
        - faithful (present in the article),
        - anywhere (can be located anywhere in the article).

        Guidelines:
        - The first summary should be long (4-5 sentences, ~80 words) yet highly
        non-specific, containing little information beyond the entities marked
        as missing. Use overly verbose language and fillers (e.g., "this article
        discusses") to reach ~80 words.
        - Make every word count: rewrite the previous summary to improve flow and
        make space for additional entities.
        - Make space with fusion, compression, and removal of uninformative
        phrases like "the article discusses".
        - The summaries should become highly dense and concise yet self-contained,
        i.e., easily understood without the article.
        - Missing entities can appear anywhere in the new summary.
        - Never drop entities from the previous summary. If space cannot be made,
        add fewer new entities.
        Remember, use the exact same number of words for each summary.
        Answer in JSON. The JSON should be a list (length 5) of dictionaries whose
        keys are "Missing_Entities" and "Denser_Summary".
        """

        prompt = PromptTemplate.from_template(template=template)
