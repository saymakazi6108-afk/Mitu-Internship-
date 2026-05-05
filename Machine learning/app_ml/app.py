import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("My ML Model App")

st.write("Enter input values:")

# Example inputs (change according to your model)
f1 = st.number_input("CGPA")
f2 = st.number_input("IQ")

if st.button("Predict"):
    input_data = np.array([[f1, f2]])
    prediction = model.predict(input_data)

    st.success(f"Prediction: {prediction[0]}")
