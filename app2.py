import streamlit as st
import pandas as pd
import numpy as np

def welcome_page():
    st.balloons()
    st.title("Welcome to Machine learning world")
    st.subheader("image")
    st.image("machine.jpg")
     

def login_page():
    st.balloons()
    st.title("PROTOTYPE")
    st.image("prototype.jpg")

def model_start():
    st.balloons()
    st.text_input("Enter input1")
    st.text_input("enter input2")
    df=st.file_uploader('Upload a dataset here')
    data=pd.read_csv('power_test.csv')
    st.line_chart(data) 
    st.markdown('Dataset :')
    st.write(data.head())
    st.text_input("Here are outputs:")
    
     

     
def main():
    page = st.sidebar.radio("Navigation", ["Welcome", "Login","model"])

    if page == "Welcome":
        welcome_page()
    elif page == "Login":
        login_page()
    elif page == "model":
        model_start()     

if __name__ == "__main__":
    main()
