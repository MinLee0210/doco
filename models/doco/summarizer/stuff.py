from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain

from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate

from base import SummarizerBase

# Define prompt
prompt_template = """You will generate concise, entity-dense summaries of the above document. Do not discuss the guidelines for summarization in your response.

Guidelines for summarization:

- The first should be concise (4-5 sentences, ~80 words).

- Make every word count. Do not fill with additional words which are not critical to summarize the original document.

- Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".

- The summaries should become highly dense and concise yet self-contained, i.e., easily understood without the article.

Summary:
"""

class StuffSummarizer(SummarizerBase): 
    def __init__(self, llm): 
        super().__init__(llm)
        
    def summarize(self, text):
        try: 
            prompt = PromptTemplate.from_template(prompt_template)

            # Define LLM chain
            llm_chain = LLMChain(llm=self.llm, prompt=prompt)

            # Define StuffDocumentsChain
            stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")

            text = Document(page_content=text)
            result = stuff_chain.run([text])
            return result
        
        except Exception as e: 
            return e