import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('models/machinery_failure_model.pkl')

# Title of the app
st.title("Mechanical Failure Prediction")

# Input fields for user to enter data
st.header("Enter Machine Parameters")

vibration_x = st.number_input("Vibration X", value=0.0)
vibration_y = st.number_input("Vibration Y", value=0.0)
vibration_z = st.number_input("Vibration Z", value=0.0)
temperature = st.number_input("Temperature (°C)", value=60.0)
rpm = st.number_input("RPM", value=1500)
operating_time = st.number_input("Operating Time (hours)", value=100)

# Create a DataFrame from user input
input_data = pd.DataFrame({
    'Vibration_X': [vibration_x],
    'Vibration_Y': [vibration_y],
    'Vibration_Z': [vibration_z],
    'Temperature': [temperature],
    'RPM': [rpm],
    'Operating_Time': [operating_time]
})

# Button to make a prediction
if st.button("Predict Failure"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Prediction: Failure Detected!")
    else:
        st.success("Prediction: No Failure Detected.")
