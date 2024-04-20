import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from io import StringIO
import time
import base64
from dotenv import load_dotenv

st.session_state.update(st.session_state)
st.set_page_config(page_title="Code reviewer", layout="centered", initial_sidebar_state="collapsed", menu_items=None)

if 'openai_config' not in st.session_state:
    st.error('OpenAI Key not entered. Please key in your OpenAI key in OpenAI configuration page.')
else:
    os.environ["OPENAI_API_KEY"] = st.session_state.openai_config.api_key

st.title("Welcome to CodeWizard: Reviewing your code with Artistry and Magic.")
load_dotenv()
st.header("Please upload your code file here:")

def text_downloader(raw_text):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    b64 = base64.b64encode(raw_text.encode()).decode()
    new_filename = "code_review_analysis_file_{}_.txt".format(timestr)
    st.markdown("#### Download File ✅###")
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'
    st.markdown(href, unsafe_allow_html=True)

data = st.file_uploader("Upload python file", type=[".py", ".cs", ".js"])

if data:
    stringio = StringIO(data.getvalue().decode('utf-8'))
    fetched_data = stringio.read()
    st.write(fetched_data)

    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)
    systemMessage = SystemMessage(content="You are a code review assistant. Provide detailed suggestions to improve the given Python code along by mentioning the existing code line by line with proper indentYou are a code review assistant. Mention the the language the code is written and Provide detailed suggestions to improve the given  code in python or in java script or c sharp or in scala along by mentioning the existing code line by line with proper indent")
    humanMessage = HumanMessage(content=fetched_data)
    finalResponse = chat.invoke([systemMessage, humanMessage])

    st.markdown(finalResponse.content)
    text_downloader(finalResponse.content)

# Display the button after displaying the review comments
if data:
    if st.button("About App"):
        st.write("For code understanding and logic explanation, please reach out to vijaykrishnanmr@gmail.com")
