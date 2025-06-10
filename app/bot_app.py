import streamlit as st
import joblib
import numpy as np

# Load the trained XGBoost model
model = joblib.load("app/xgboost_model.pkl")

st.set_page_config(page_title="Personality Predictor", page_icon="🧠")
st.title("🧠 Personality Prediction...")
st.markdown("Enter the details below to predict whether You are an Introvert or Extrovert.")

# Input fields
col1, col2 = st.columns(2)
with col1:
    time_spent_alone = st.slider("Time spent alone (hours/day)", 0, 12, 5)
    stage_fear = st.radio("Stage Fear?", ["Yes", "No"])
    social_event_attendance = st.slider("Social event attendance (0-10)", 0, 10, 5)
    going_outside = st.slider("Interest in going outside (0-10)", 0, 10, 5)

with col2:
    drained_after_socializing = st.radio("Feel drained after socializing?", ["Yes", "No"])
    friend_circle_size = st.slider("Friend circle size (0-15)", 0, 15, 5)
    post_freq_on_social_media = st.slider("Post frequency on social media (0-10)", 0, 10, 5)

# Convert categorical inputs
stage_fear_val = 1 if stage_fear == "Yes" else 0
drained_val = 1 if drained_after_socializing == "Yes" else 0

# Prepare input vector
features = np.array([
    time_spent_alone,
    stage_fear_val,
    social_event_attendance,
    going_outside,
    drained_val,
    friend_circle_size,
    post_freq_on_social_media
]).reshape(1, -1)

# Predict button
if st.button("Predict Personality"):
    prediction = model.predict(features)[0]
    result = "🧍‍♂️ Introvert" if prediction == 0 else "🧑‍🤝‍🧑 Extrovert"
    st.success(f"Your Personality : {result}")
