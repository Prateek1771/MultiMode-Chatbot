# Basic Structure V1.0

import ollama
import streamlit as st

st.title('Chatbot')

# models = [model['name'] for model in ollama.list() ['models']]
# st.selectbox("Select a model", models)

query = st.chat_input("enter your question")
if query:
    with st.chat_message("user"):
        st.write(query)
    with st.chat_message("assistant"):
        response = ollama.generate(model="llama3.2",prompt = query)
        st.write(response["response"])


