# =============================================
# STREAMLIT APP
# FRAUD PREDICTION IN MOBILE TRANSACTIONS
# =============================================

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load saved model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("📱 Fraud Prediction in Mobile Transactions - Tanzania")
st.write("Enter transaction details to predict whether it is fraud.")

# ======================
# User Inputs
# ======================
amount = st.number_input("Transaction Amount", min_value=0.0)
old_balance = st.number_input("Old Balance", min_value=0.0)
new_balance = st.number_input("New Balance", min_value=0.0)
transaction_type = st.number_input("Transaction Type (Encoded)", min_value=0)

# ======================
# Prediction
# ======================
if st.button("Predict Fraud"):

    input_data = np.array([[amount, old_balance, new_balance, transaction_type]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    if round(prediction[0]) == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is NOT Fraudulent.")