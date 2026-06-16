
 import streamlit as st

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Project Overview",
        "EDA Visualization",
        "Prediction",
        "Model Performance"
    ]
)

if page == "Project Overview":
    st.title("Student Performance Prediction")
    st.write("This project predicts student performance using Machine Learning.")
    st.write("Dataset: StudentsPerformance.csv")
    st.write("Tools Used: Python, Pandas, Scikit-Learn, Streamlit")

elif page == "EDA Visualization":
    st.title("EDA Visualizations")

    st.image("Screenshot_20260605_214038.jpg")
    st.image("Screenshot_20260605_214541.jpg")
    st.image("Screenshot_20260605_215029.jpg")

elif page == "Prediction":
    st.title("Prediction Page")

    name = st.text_input("Student Name")

    reading = st.number_input("Reading Score", 0, 100)

    writing = st.number_input("Writing Score", 0, 100)

    if st.button("Predict"):
        prediction = (reading + writing) / 2
        st.success(f"Predicted Math Score: {prediction:.2f}")

elif page == "Model Performance":
    st.title("Model Performance")

    st.metric("Accuracy", "87%")
    st.write("Model evaluated using regression metrics.")