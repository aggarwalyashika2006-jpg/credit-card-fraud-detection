import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Load model
model = joblib.load("models/fraud_model.pkl")

st.set_page_config(page_title="Fraud Detection", layout="wide")

st.title("💳 Credit Card Fraud Detection Dashboard")

st.markdown("### 🚨 Real-Time Transaction Monitoring System")

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("Enter Transaction Details")

amount = st.sidebar.slider("Amount", 0.0, 5000.0, 100.0)
time = st.sidebar.slider("Time", 0, 100000, 1000)

# Generate fake features
features = np.random.normal(0, 1, 28)

input_data = np.array([[time] + list(features) + [amount]])

# -----------------------------
# Prediction Button
# -----------------------------
if st.sidebar.button("🔍 Check Transaction"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Legitimate Transaction")

# -----------------------------
# Dashboard Section
# -----------------------------
st.markdown("## 📊 Transaction Insights")

# Load dataset
df = pd.read_csv("data/creditcard_fake.csv")

col1, col2 = st.columns(2)

# Fraud distribution
with col1:
    st.subheader("Fraud vs Normal")
    fig, ax = plt.subplots()
    df["Class"].value_counts().plot(kind="bar", ax=ax)
    st.pyplot(fig)

# Amount distribution
with col2:
    st.subheader("Transaction Amount Distribution")
    fig, ax = plt.subplots()
    ax.hist(df["Amount"], bins=30)
    st.pyplot(fig)

# -----------------------------
# Data Preview
# -----------------------------
st.markdown("## 📂 Dataset Preview")
st.dataframe(df.head(20))