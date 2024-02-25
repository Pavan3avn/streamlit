import streamlit as st
from langchain_community.llms import OpenAI

st.title('Quick Start App')
openai_api_key = st.sidebar.text_input('OpenAI_API_Key',type = 'password')

def genarate_response(input_text):
    llm = OpenAI(temperature = 0,openai_api_key = openai_api_key)
    st.info(llm(input_text))
    
with st.form('my_form'):
    text = st.text_area('Enter text:','what are the concepts that are need to learn LLMs ')
    submitted = st.form_submit_button("submit")
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your api key correctly!',icon='⚠')
    else :
        genarate_response(text)
            
    