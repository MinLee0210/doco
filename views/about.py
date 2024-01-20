import streamlit as st
from st_pages import add_page_title

add_page_title()

st.sidebar.write(
    """
    App created by [Minh Le Duc](https://www.linkedin.com/in/minh-le-duc-a62863172/) using [Streamlit](https://streamlit.io/) and [HuggingFace](https://huggingface.co/inference-api).
    """
)

# ----- Main content -----
st.subheader("About me")
st.markdown(
"""
    My name is Minh Le Duc, an AI enthusiast who is walking step by step on the path of becoming an expert in AI career. 
"""
)

st.subheader("About the project")
st.markdown(
"""
Clearly, we can see that thanks to the advancement of the technology, the traffic of information becomes more remarkably astonishing. 
However, the advantage does raise a disturb phenomenon in which a person who need to do research or whose job relate to searching documents becomes drowned. 
A tool which is able to extract most important features from documents are actually in need. 

Automatic text summarization comes and save the day. Summarize is an act of convey important information from the original text(s). 
Automatic text summarization is the task of producing a concise and fluent summary while preserving key information content and overall meaning. 
The task is usually put into question since the action requires human knowledge and language adaptability. 
However, there are many researches have been raised and prove that, although the quality is not remarkable, but the capability is implement-able and develop-able. 

I am inspired by the ability and desired to create an application that pursuit the AI-based summarizer. Thereore, I create this application to demonstrate the
automatic text summarization which is performed by deep learning. The project is actively developed. In other words, it would be updated and expaned continuously.
"""
)

st.subheader("More details")
st.markdown(
"""
    More details about project structure and results of experiments are disscussed in [the project's Github repo](https://github.com/MinLee0210/DoCo.git).
"""
)