import streamlit as st
import pandas as pd
import numpy as np
from openai import OpenAI
 

def welcome_page():
    st.title("Welcome to Machine learning world")
    st.subheader("image")
    st.image("machine.jpg")
def model2():
    uploaded_file = st.file_uploader("model.pkl")
    if uploaded_file is not None:
        clf2 = pickle.loads(uploaded_file.read())
        st.write("Model loaded")
        st.write(clf2)
        st.write("Predicting...")
        st.write(clf2.predict(X[0:1]))
        st.write(y[0])
        st.write("Done!")

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
        
             
def main():
    page = st.sidebar.radio("Navigation", ["Welcome", "prototype","model"])

    if page == "Welcome":
        welcome_page()
    elif page == "prototype":
        login_page()
    elif page == "model":
        model_start()

if __name__ == "__main__":
    main()
