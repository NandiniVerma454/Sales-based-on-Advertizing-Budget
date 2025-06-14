import streamlit as st
import numpy as np
import joblib

# Load your model
model = joblib.load("Python_Code/sales_model.pkl")

st.title("📊 Predict Sales via Advertising Budget")

tv = st.number_input("TV Budget")
radio = st.number_input("Radio Budget")
newspaper = st.number_input("Newspaper Budget")

if st.button("Predict Sales"):
    input_data = np.array([[tv, radio, newspaper]])
    prediction = model.predict(input_data)
    st.success(f"📈 Predicted Sales: {prediction[0]:.2f} units")
