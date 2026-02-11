# =============================================
# STREAMLIT APP
# FRAUD PREDICTION IN MOBILE TRANSACTIONS
# UPDATED - AUTO FEATURE MATCHING
# =============================================

import streamlit as st
import pandas as pd
import pickle

# Load model and feature list
model = pickle.load(open("model.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

st.title("📱 Fraud Prediction in Mobile Transactions - Tanzania")
st.write("Enter transaction details to predict fraud.")

# ======================
# Dynamic Input Fields
# ======================
input_data = {}

for feature in features:
    input_data[feature] = st.number_input(f"Enter {feature}", value=0.0)

# ======================
# Prediction
# ======================
if st.button("Predict Fraud"):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)

    if round(prediction[0]) == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is NOT Fraudulent.")
