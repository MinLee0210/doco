import streamlit as st

from controller.apiv1 import query
from models.model import Model

# ----- From Navigation bar ----- 
st.sidebar.write("")

API_KEY = st.sidebar.text_input(
    "Enter your HuggingFace API key",
    help="Once you created you HuggingFace account, you can get your free API token in your settings page: https://huggingface.co/settings/tokens",
    type="password",
)

# Adding the HuggingFace API inference URL.
MODEL_SUMMARISE = Model.MODEL['fb_bart']
MODEL_EXTRACTOR = Model.EXTRACTOR['h2_trans']
API_SUMMARISE =  Model.API_INFERENCE + MODEL_SUMMARISE
API_EXTRACTOR = Model.API_INFERENCE + MODEL_EXTRACTOR

# Now, let's create a Python dictionary to store the API headers.
headers = {"Authorization": f"Bearer {API_KEY}"}

st.sidebar.write(
    """
    App created by [Minh Le Duc](https://www.linkedin.com/in/minh-le-duc-a62863172/) using [Streamlit](https://streamlit.io/) and [HuggingFace](https://huggingface.co/inference-api).
    """
)


# ----- From Main side -----
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(
        "static/doco_logo.jpg",
        width=100,
    )
st.caption("")
st.title("DoCo - Document Compressor")

if not "valid_inputs_received" in st.session_state:
    st.session_state["valid_inputs_received"] = False

st.write("")
st.markdown(
    """
    ### Summarizing documents with this app with no training need. Hope you enjoy!
    """
)

st.write("")

with st.form(key="my_form"):
    
    text = st.text_area(        
        "Enter some text 👇",
        label_visibility='visible',
        placeholder='Input something ...',
        height=256)

    submit_button = st.form_submit_button(label="Submit")


if not submit_button and not st.session_state.valid_inputs_received:
    st.stop()

elif submit_button and not text:
    st.warning("There is no input text")
    st.session_state.valid_inputs_received = False
    st.stop()

elif submit_button or st.session_state.valid_inputs_received:

    if submit_button:

        st.session_state.valid_inputs_received = True

    api_summarise = query(
        {
            "inputs": text,
            "parameters": {"do_sample": False, 
                           "temperature": 20,
                           "top_k": 10, 
                           "top_p": 10},
            "options": {"wait_for_model": True},
        }, 
        url=API_SUMMARISE, 
        headers=headers
    )
    api_extractor = query(
        {
            "inputs": text,
            "parameters": {"do_sample": False, 
                           "temperature": 20,
                           "top_k": 10, 
                           "top_p": 10},
            "options": {"wait_for_model": True},
        }, 
        url=API_EXTRACTOR, 
        headers=headers
    )

    api_result = {
        "Summarizing": api_summarise, 
        "Extracting": api_extractor
    }

    for api, result in api_result.items(): 
        if 'error' in result[0].keys(): 
            st.warning(f'{api} failed')



    st.success("✅ Done!")
    st.caption("")
    st.markdown(f"### Generated text!")
    st.caption("")
    st.write(api_summarise[0]['summary_text'])
    st.markdown(f"### Most important words!")
    st.caption("")
    st.write(api_extractor[0]['summary_text'].split(',  ')) # Custtom `split` function based on results of the API.

