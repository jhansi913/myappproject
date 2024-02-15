import streamlit as st
import pandas as pd
import numpy as np
import pickle
 

def welcome_page():
    st.title("Welcome to Machine learning world")
    st.subheader("image")
    st.image("machine.jpg")
 
     
        
        
         
def make_prediction(model, Temperature,Volume,Pressure,Humidity):
    input_data = [[Temperature,Volume,Pressure,Humidity]]
    prediction = model.predict(input_data)
    return prediction


def prototype():
    st.title("PROTOTYPE")
    st.image("prototype.jpg")

def model_start():
    uploaded_file = st.file_uploader("model.pkl")
    if uploaded_file is not None:
        clf2 = pickle.loads(uploaded_file.read())
    Temperature=st.text_input("Enter temp")
    Volume=st.text_input("enter volume")
    Pressure=st.text_input("enter pressure")
    Humidity=st.text_input("enter humidity")
    power=make_prediction(clf2,Temperature,Volume,Pressure,Humidity)
    st.write(power)
    df=st.file_uploader('Upload a dataset here')
    data=pd.read_csv('power_test.csv')
    st.line_chart(data) 
    st.markdown('Dataset :')
    st.write(data.head())
    st.text_input("Here are outputs:")
        
             
def main():
    page = st.sidebar.radio("Navigation", ["Welcome", "prototype","model","model2"])

    if page == "Welcome":
        welcome_page()
    elif page == "prototype":
        login_page()
    elif page == "model":
        
        model_start()
    elif page == "model2":
        model2()
     
      

if __name__ == "__main__":
    main()
