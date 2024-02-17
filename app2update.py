import streamlit as st
import pandas as pd
import numpy as np
import pickle

def load_model(model_path):
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def welcome_page():
    st.title("Welcome to Machine learning world")
    st.subheader("image")
    st.image("machine.jpg")
 
     
        
        
         
def predict_power(model, temp, hum, press, volume):
    input_features = [[temp, hum, press, volume]]
    power = model.predict(input_features)[0]
    return power


def prototype():
    st.title("PROTOTYPE")
    st.image("prototype.jpg")

def model_start():
     temp = st.number_input("Enter temperature:", min_value=0.0, step=0.1)
     hum = st.number_input("Enter humidity:", min_value=0.0, step=0.1)
     press = st.number_input("Enter pressure:", min_value=0.0, step=0.1)
     volume = st.number_input("Enter volume:", min_value=0.0, step=0.1)
     if st.button("Predict Power"):
         power = predict_power(model, temp, hum, press, volume)
         st.success(f"Predicted power: {power}")
    df=st.file_uploader('Upload a dataset here')
    data=pd.read_csv('power_test.csv')
    st.line_chart(data) 
    st.markdown('Dataset :')
    st.write(data.head())
    st.text_input("Here are outputs:")
        
             
def main():
    page = st.sidebar.radio("Navigation", ["Welcome", "prototype","model","model22"])

    if page == "Welcome":
        welcome_page()
    elif page == "prototype":
        prototype()
    elif page == "model":
        model_start()
    elif page == "model22":
        model2()
     
      

if __name__ == "__main__":
    main()
