import requests
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_tags import st_tags  # to add labels on the fly!
from st_pages import add_page_title

from config import Config
from controller.apiv1 import query
from models.model import Model
# add_page_title()

# ----- From Navigation bar ----- 
st.sidebar.write("")

API_KEY = st.sidebar.text_input(
    "Enter your HuggingFace API key",
    help="Once you created you HuggingFace account, you can get your free API token in your settings page: https://huggingface.co/settings/tokens",
    type="password",
)

# Adding the HuggingFace API inference URL.
API_OPTION = Model.MODEL['fb_bart']
API_URL =  Model.API_INFERENCE + API_OPTION

# Now, let's create a Python dictionary to store the API headers.
headers = {"Authorization": f"Bearer {API_KEY}"}

st.sidebar.write(
    """
    App created by [Minh Le Duc](https://www.linkedin.com/in/minh-le-duc-a62863172/) using [Streamlit](https://streamlit.io/) and [HuggingFace](https://huggingface.co/inference-api).
    """
)


# ----- From Main side -----
# We create a set of columns to display the logo and the heading next to each other.
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(
        "static/doco_logo.jpg",
        width=100,
    )
st.caption("")
st.title("DoCo - Document Compressor")

# We need to set up session state via st.session_state so that app interactions don't reset the app.
if not "valid_inputs_received" in st.session_state:
    st.session_state["valid_inputs_received"] = False
# Then, we create a intro text for the app, which we wrap in a st.markdown() widget.

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
        height=100)

    submit_button = st.form_submit_button(label="Submit")


if not submit_button and not st.session_state.valid_inputs_received:
    st.stop()

elif submit_button and not text:
    st.warning("There is no input text")
    st.session_state.valid_inputs_received = False
    st.stop()

elif submit_button or st.session_state.valid_inputs_received:

    if submit_button:

        # The block of code below if for our session state.
        # This is used to store the user's inputs so that they can be used later in the app.

        st.session_state.valid_inputs_received = True

    api_json_output = query(
        {
            "inputs": text,
            "parameters": {"do_sample": False, 
                           "temperature": 20,
                           "top_k": 10, 
                           "top_p": 10},
            "options": {"wait_for_model": True},
        }, 
        url=API_URL, 
        headers=headers
    )

    api_error = api_json_output['error']
    if api_error: 
        st.warning(api_error)
    else: 
        st.success("✅ Done!")
        st.caption("")
        st.markdown("### Check the results!")
        st.caption("")
        st.write(api_json_output)

