import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the saved model
model = joblib.load('student_performance_model.pkl')

# App title
st.title("🎓 Student Performance Prediction App")
st.write("Predict a student's Performance Index based on study habits and activities.")

st.sidebar.header("📋 Enter Student Details")

hours_studied = st.sidebar.number_input("Hours Studied per day", min_value=0, max_value=24, value=5)
previous_scores = st.sidebar.number_input("Previous Exam Score", min_value=0, max_value=100, value=75)
sleep_hours = st.sidebar.number_input("Average Sleep Hours", min_value=0, max_value=12, value=7)
sample_papers = st.sidebar.number_input("Sample Question Papers Practiced", min_value=0, max_value=50, value=5)
extracurricular = st.sidebar.selectbox("Participates in Extracurricular Activities?", ['Yes', 'No'])


if st.button("Predict Performance Index"):
    # Create input DataFrame
    input_data = pd.DataFrame({
        'Hours Studied': [hours_studied],
        'Previous Scores': [previous_scores],
        'Sleep Hours': [sleep_hours],
        'Sample Question Papers Practiced': [sample_papers],
        'Extracurricular Activities': [extracurricular]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display result
    st.success(f"🎯 Predicted Performance Index: {prediction:.2f}")
    
    
rmse = 2.01
mae = 1.60
r2 = 0.989

st.write("### 📈 Model Evaluation Metrics")
st.write(f"**RMSE:** {rmse:.2f}")
st.write(f"**MAE:** {mae:.2f}")
st.write(f"**R² Score:** {r2:.2f}")

    
