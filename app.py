import streamlit as st

st.title("Student Performance Prediction")

name = st.text_input("Student Name")

reading = st.number_input("Reading Score", 0, 100)

writing = st.number_input("Writing Score", 0, 100)

if st.button("Predict"):
    prediction = (reading + writing) / 2
    st.success(f"Predicted Math Score: {prediction:.2f}")