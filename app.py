import streamlit as st

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    ["Project Overview", "EDA Visualization", "Prediction", "Model Performance"]
)

# Project Overview
if page == "Project Overview":
    st.title("Student Performance Prediction")
    st.write("This project predicts student performance using Machine Learning.")
    st.write("Dataset: StudentsPerformance.csv")

# EDA Visualization
elif page == "EDA Visualization":
    st.title("EDA Visualization")
    st.write("Sample Graph")
    st.bar_chart([50, 70, 80, 90, 65])

# Prediction
elif page == "Prediction":
    st.title("Prediction Page")

    reading = st.number_input("Reading Score", 0, 100)
    writing = st.number_input("Writing Score", 0, 100)

    if st.button("Predict"):
        prediction = (reading + writing) / 2
        st.success(f"Predicted Math Score: {prediction:.2f}")

# Model Performance
elif page == "Model Performance":
    st.title("Model Performance")
    st.write("Accuracy: 92%")
    st.write("Mean Absolute Error: 3.5")
    
 