import pytest
import os
from dotenv import load_dotenv

from doco.components.llms import AgentFactory

def setup_api_key(): 
    load_dotenv()

    os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
    os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")


@pytest.fixture(params=['gemini', 'ollama', 'groq'], scope='class')
def init_llm(request):
    "Used to trigger connection to LLMs." 
    setup_api_key()
    llm_config = None
    if request.param == 'gemini':
        llm_config = {'model': 'models/gemini-1.5-flash'}
    elif request.param == 'groq':
        llm_config = {'model': 'llama3-8b-8192'}
    elif request.param == 'ollama':
        llm_config = {'model': 'tinyllama'}

    request.cls.llm = AgentFactory.build(provider=request.param, llm_config=llm_config)


@pytest.fixture
def llm_summarizer(): 
    "Used to test summarizer agent."
    setup_api_key()
    return """I want to understand this passage correctly: Extraction-based summarization
Here, content is extracted from the original data, but the extracted content is not modified in any way. Examples of extracted content include key-phrases that can be used to "tag" or index a text document, or key sentences (including headings) that collectively comprise an abstract, and representative images or video segments, as stated above. For text, extraction is analogous to the process of skimming, where the summary (if available), headings and subheadings, figures, the first and last paragraphs of a section, and optionally the first and last sentences in a paragraph are read before one chooses to read the entire document in detail.[10] Other examples of extraction that include key sequences of text in terms of clinical relevance (including patient/problem, intervention, and outcome).[11]

Abstractive-based summarization
Abstractive summarization methods generate new text that did not exist in the original text.[12] This has been applied mainly for text. Abstractive methods build an internal semantic representation of the original content (often called a language model), and then use this representation to create a summary that is closer to what a human might express. Abstraction may transform the extracted content by paraphrasing sections of the source document, to condense a text more strongly than extraction. Such transformation, however, is computationally much more challenging than extraction, involving both natural language processing and often a deep understanding of the domain of the original text in cases where the original document relates to a special field of knowledge. "Paraphrasing" is even more difficult to apply to images and videos, which is why most summarization systems are extractive.

Aided summarization
Approaches aimed at higher summarization quality rely on combined software and human effort. In Machine Aided Human Summarization, extractive techniques highlight candidate passages for inclusion (to which the human adds or removes text). In Human Aided Machine Summarization, a human post-processes software output, in the same way that one edits the output of automatic translation by Google Translate."""

@pytest.fixture
def llm_content_creator(): 
    "Used to test Content Creator agent."
    setup_api_key()
    return "I want to know more about content creator."