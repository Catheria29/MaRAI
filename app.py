import streamlit as st
import pickle
import numpy as np

# 1. SETUP: Professional Page Title
st.set_page_config(page_title="MaRAI: Maternal Risk AI", layout="centered")

# 2. THE BRAIN: Loading your saved .pkl file
# We use st.cache_resource so it only loads once, keeping it fast!
@st.cache_resource
def load_model():
    with open('marai_model.pkl', 'rb') as file:
        return pickle.load(file)

model = load_model()

# 3. HEADER: The branding for your MaRAI project
st.title(" MaRAI: Smart Pregnancy Planning Tool")
st.write("Predict maternal health risk levels using AI-driven analysis.")
st.markdown("---")

# 4. INPUTS: Grouping data for a better User Experience
st.subheader("Patient Vitals")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 15, 55, 25)
    systolic = st.number_input("Systolic BP (High)", 90, 160, 120)
    diastolic = st.number_input("Diastolic BP (Low)", 60, 100, 80)

with col2:
    bs = st.number_input("Blood Sugar (BS)", 6.0, 19.0, 7.0)
    temp = st.number_input("Body Temperature (F)", 98.0, 103.0, 98.6)
    heart_rate = st.number_input("Heart Rate", 60, 100, 70)

# 5. PREDICTION: The magic moment
if st.button("Analyze Risk", use_container_width=True):
    # Format inputs exactly like the 1,500-row dataset the AI learned from
    input_data = np.array([[age, systolic, diastolic, bs, temp, heart_rate]])
    
    # Get numeric prediction (0, 1, or 2)
    prediction = model.predict(input_data)[0]
    
    # Map back to human-readable text
    risk_labels = {0: "Low Risk", 1: "Mid Risk", 2: "High Risk"}
    result = risk_labels[prediction]
    
    # 6. RESULTS: Visual feedback using Streamlit's colored alerts
    st.markdown("---")
    if prediction == 2:
        st.error(f"Prediction: {result}")
        st.write("⚠️ Urgent: Clinical consultation is highly recommended.")
    elif prediction == 1:
        st.warning(f"Prediction: {result}")
        st.write("🟡 Caution: Routine monitoring and follow-up advised.")
    else:
        st.success(f"Prediction: {result}")
        st.write("✅ Healthy: Vitals appear to be within normal range.")
