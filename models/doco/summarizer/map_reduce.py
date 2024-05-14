from langchain.chains import MapReduceDocumentsChain, ReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain_text_splitters import CharacterTextSplitter

from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

from base import SummarizerBase

map_template = """
The following is a set of documents
{docs}
Based on this list of docs, please identify the main themes 
Helpful Answer:
"""

reduce_template = """
The following is set of summaries:
{docs}
Take these and distill it into a final, consolidated summary of the main themes. 
Helpful Answer:
"""

class MapReduceSummarizer(SummarizerBase): 
    def __init__(self, llm): 
        super().__init__(llm)

    def get_map_chain(self): 
        map_prompt = PromptTemplate.from_template(map_template)
        map_chain = LLMChain(llm=self.llm, prompt=map_prompt)
        return map_chain
    
    def get_reduce_chain(self): 
        reduce_prompt = PromptTemplate.from_template(reduce_template)
        reduce_chain = LLMChain(llm=self.llm, prompt=reduce_prompt)
        return reduce_chain

    def summarize(self, text, n_chunks:int=5, stride:int=0):
        map_chain = self.get_map_chain()
        reduce_chain = self.get_reduce_chain()


        # Takes a list of documents, combines them into a single string, and passes this to an LLMChain
        combine_documents_chain = StuffDocumentsChain(
            llm_chain=reduce_chain, document_variable_name="docs"
        )

        # Combines and iteratively reduces the mapped documents
        reduce_documents_chain = ReduceDocumentsChain(
            # This is final chain that is called.
            combine_documents_chain=combine_documents_chain,
            # If documents exceed context for `StuffDocumentsChain`
            collapse_documents_chain=combine_documents_chain,
            # The maximum number of tokens to group documents into.
            token_max=4000,
        )

        # Combining documents by mapping a chain over them, then combining results
        map_reduce_chain = MapReduceDocumentsChain(
            # Map chain
            llm_chain=map_chain,
            # Reduce chain
            reduce_documents_chain=reduce_documents_chain,
            # The variable name in the llm_chain to put the documents in
            document_variable_name="docs",
            # Return the results of the map steps in the output
            return_intermediate_steps=False,
        )

        # Splitting text
        n_tokens = len(text.split())
        chunk_size = n_tokens // n_chunks
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
                chunk_size=chunk_size, chunk_overlap=stride
            )
        split_docs = text_splitter.split_documents(text)

        result = map_reduce_chain.run({'docs': split_docs})
        return result