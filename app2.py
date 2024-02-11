import streamlit as st
import pandas as pd
import numpy as np
from openai import OpenAI
 

def welcome_page():
    st.title("Welcome to Machine learning world")
    st.subheader("image")
    st.image("machine.jpg")
     

def prototype():
    st.title("PROTOTYPE")
    st.image("prototype.jpg")

def model_start():
    st.text_input("Enter temp")
    st.text_input("enter volume")
    st.text_input("enter pressure")
    st.text_input("enter humidity")
    df=st.file_uploader('Upload a dataset here')
    data=pd.read_csv('power_test.csv')
    st.line_chart(data) 
    st.markdown('Dataset :')
    st.write(data.head())
    st.text_input("Here are outputs:")

def chatgpt():
    st.title("ChatGPT-like clone")
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
         with st.chat_message(message["role"]):
             st.markdown(message["content"])
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
               model=st.session_state["openai_model"],
               messages=[
                  {"role": m["role"], "content": m["content"]}
                  for m in st.session_state.messages
              ],
              stream=True,
        )
        response = st.write_stream(stream)
       st.session_state.messages.append({"role": "assistant", "content": response})
            

        
             
def main():
    page = st.sidebar.radio("Navigation", ["Welcome", "prototype","chatbot","model"])

    if page == "Welcome":
        welcome_page()
    elif page == "prototype":
        login_page()
    elif page == "model":
        model_start()
    elif page == "chatbot":
        chatgpt()

if __name__ == "__main__":
    main()
