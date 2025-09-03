import streamlit as st
import pickle
import numpy as np

# ---------------------------
# Load your trained model (pipeline)
# ---------------------------
model = pickle.load(open("stress_model.pkl", "rb"))

# ---------------------------
# App frontend
# ---------------------------
st.set_page_config(page_title="Stress Level Predictor", layout="centered")
st.title("🧠 Stress Level Prediction App")
st.write("Enter your details to predict your stress level.")

# ---------------------------
# Inputs for Top 10 Features
# ---------------------------
basic_needs = st.slider("Basic Needs Satisfaction (1=Very Poor, 10=Excellent)", 1, 10, 5)
headache = st.selectbox("Frequent Headache?", ["No", "Yes"])
academic_performance = st.slider("Academic Performance (1=Low, 10=High)", 1, 10, 5)
sleep_quality = st.slider("Sleep Quality (1=Poor, 10=Excellent)", 1, 10, 5)
depression = st.slider("Depression Level (1=Low, 10=High)", 1, 10, 5)
anxiety_level = st.slider("Anxiety Level (1=Low, 10=High)", 1, 10, 5)
bullying = st.selectbox("Exposed to Bullying?", ["No", "Yes"])
extracurricular_activities = st.slider("Extracurricular Activities (1=Low, 10=High)", 1, 10, 5)
peer_pressure = st.slider("Peer Pressure Level (1=Low, 10=High)", 1, 10, 5)
self_esteem = st.slider("Self Esteem (1=Low, 10=High)", 1, 10, 5)

# Convert Yes/No inputs to numeric
headache_val = 1 if headache == "Yes" else 0
bullying_val = 1 if bullying == "Yes" else 0

# Prepare input (must match training order)
features = np.array([[basic_needs, headache_val, academic_performance,
                      sleep_quality, depression, anxiety_level,
                      bullying_val, extracurricular_activities,
                      peer_pressure, self_esteem]])

# ---------------------------
# Prediction
# ---------------------------
if st.button("Predict Stress Level"):
    prediction = model.predict(features)[0]
    
    if prediction == 0:
        st.success("✅ Low Stress Level")
    elif prediction == 1:
        st.warning("⚠️ Moderate Stress Level")
    else:
        st.error("🚨 High Stress Level")
