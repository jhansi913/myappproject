import streamlit as st
import pickle

def load_model(model_path):
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def predict_power(model, temp, hum, press, volume):
    input_features = [[temp, hum, press, volume]]
    power = model.predict(input_features)[0]
    return power

def main():
    st.title("Power Prediction App")

    # Load machine learning model
    model_path = "model.pkl"
    model = load_model(model_path)

    # User inputs
    temp = st.number_input("Enter temperature:", min_value=0.0, step=0.1)
    hum = st.number_input("Enter humidity:", min_value=0.0, step=0.1)
    press = st.number_input("Enter pressure:", min_value=0.0, step=0.1)
    volume = st.number_input("Enter volume:", min_value=0.0, step=0.1)

    # Button to predict power
    if st.button("Predict Power"):
        # Predict power
        power = predict_power(model, temp, hum, press, volume)
        st.success(f"Predicted power: {power}")

if __name__ == "__main__":
    main()
