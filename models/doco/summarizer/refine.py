from langchain_text_splitters import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate

from base import SummarizerBase


prompt_template = """Write a concise summary of the following:
{text}
CONCISE SUMMARY:"""
prompt = PromptTemplate.from_template(prompt_template)

refine_template = (
    "Your job is to produce a final summary\n"
    "We have provided an existing summary up to a certain point: {existing_answer}\n"
    "We have the opportunity to refine the existing summary"
    "(only if needed) with some more context below.\n"
    "------------\n"
    "{text}\n"
    "------------\n"
    "Given the new context, refine the original summary in Italian"
    "If the context isn't useful, return the original summary."
)

class MapReduceSummarizer(SummarizerBase): 
    def __init__(self, llm): 
        super().__init__(llm)

    def summarize(self, text, n_chunks:int=5, stride:int=0):
        refine_prompt = PromptTemplate.from_template(refine_template)

        chain = load_summarize_chain(
            llm=self.llm,
            chain_type="refine",
            question_prompt=prompt,
            refine_prompt=refine_prompt,
            return_intermediate_steps=True,
            input_key="input_documents",
            output_key="output_text",
        )

        n_tokens = len(text.split())
        chunk_size = n_tokens // n_chunks
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
                chunk_size=chunk_size, chunk_overlap=stride
            )
        split_docs = text_splitter.split_documents(text)
        result = chain({"input_documents": split_docs}, return_only_outputs=True)
        return result
