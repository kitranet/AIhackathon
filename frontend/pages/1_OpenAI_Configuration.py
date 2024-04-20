import os
from util.config import OpenAIConfig
import streamlit as st
try:
    import pandas as pd
    import time
    from util.config import OpenAIConfig
except Exception as e:
    st.error(f"Import error:{e}")
st.session_state.update(st.session_state)

try:
# st page structure
    st.set_page_config(page_title="Open AI", layout="centered", initial_sidebar_state="collapsed", menu_items=None)
    api_key = st.text_input("OpenAI API Key",type='password')
    temperature = None#st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.4, step=0.05, key='oai_temp')
    max_tokens = None#st.slider("Max Tokens", min_value=100, max_value=1000, value=300, step=1, key='oai_max_tok')
    top_p = None#st.slider("Top p", min_value=0.0, max_value=1.0, value=0.5, step=0.05, key='oai_top_p')
    frequency_penalty = None#st.slider("Frequency Penalty", min_value=0.0, max_value=1.0, value=0.0, step=0.05, key='oai_frequency_penalty')
    presence_penalty = None#st.slider("Presence Penalty", min_value=0.0, max_value=1.0, value=0.0, step=0.05, key='oai_presence_penalty')
    best_of = None#st.slider("Best Of", min_value=1, max_value=10, value=1, step=1, key='oai_best_of')
    # database = st.text_input("Database")
    submitted = st.button("Submit")
    if submitted:
        st.session_state['openai_config'] = OpenAIConfig(api_key, temperature, max_tokens, top_p, frequency_penalty, presence_penalty, best_of)
        st.write(f"OpenAI config created!!")
except Exception as e:
    st.error(f"OpenAI config : {e}")

def handle_button_click():
    st.write("For code understanding and logic explanation, please reach out to vijaykrishnanmr@gmail.com")

st.button("About App", on_click=handle_button_click)
