import streamlit as st

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Project Overview", "EDA Visualization", "Prediction", "Model Performance"]
)

if page == "Project Overview":
    st.title("Student Performance Prediction")
    st.write("This project predicts student performance using Machine Learning.")
    st.write("Dataset: StudentsPerformance.csv")

elif page == "EDA Visualization":
    st.title("EDA Visualization")
    st.write("Graphs and charts will be displayed here.")
    st.bar_chart([50, 70, 80, 90])

elif page == "Prediction":
    st.title("Prediction Page")

    reading = st.number_input("Reading Score", 0, 100)
    writing = st.number_input("Writing Score", 0, 100)

    if st.button("Predict"):
        prediction = (reading + writing) / 2
        st.success(f"Predicted Math Score: {prediction:.2f}")

elif page == "Model Performance":
    st.title("Model Performance")
    st.write("Model Accuracy: 92%")
    
 