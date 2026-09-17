import streamlit as st
import joblib

model = joblib.load("updated_model.pkl")

st.title("Student Pass/Fail Prediction")

hours = st.number_input(
    "Enter Study Hours",
    min_value=0.0,
    max_value=15.0,
    value=5.0
)

attendance = st.number_input(
    "Enter Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

if st.button("Predict"):
    prediction = model.predict([[hours, attendance]])

    if prediction[0] == 1:
        st.success("PASS 🎉")
    else:
        st.error("FAIL")
