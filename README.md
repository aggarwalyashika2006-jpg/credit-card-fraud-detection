# 💳 Credit Card Fraud Detection System

## 🌐 Live Demo

👉 https://credit-card-fraud-detection-hdh33s87kq7yjtadvnkx5a.streamlit.app/

---

## 📌 Overview

This project is an end-to-end **Machine Learning-based Credit Card Fraud Detection System** that simulates how banks identify fraudulent transactions in real time.

It includes:

* Data generation (synthetic dataset)
* Model training
* Fraud prediction
* Interactive web dashboard using Streamlit

---

## 🚨 Problem Statement

Credit card fraud is a major issue in banking and fintech. Detecting fraud is difficult because:

* Fraud cases are very rare (imbalanced data)
* Patterns are complex and constantly changing

---

## 💡 Solution

This project builds a system that:

* Learns patterns from transaction data
* Identifies suspicious transactions
* Provides real-time fraud prediction through a dashboard

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn (Random Forest)
* Streamlit (Web App)
* Joblib (Model Saving)

---

## 📊 Features

* Synthetic transaction data generation
* Data preprocessing & analysis
* Machine Learning model training
* Fraud prediction system
* Interactive UI for testing transactions
* Model saving and reuse

---

## 📁 Project Structure

```
Credit-Card-Fraud-Detection/
│
├── data/
│   └── creditcard_fake.csv
│
├── models/
│   └── fraud_model.pkl
│
├── outputs/
│
├── main.py          # Model training script
├── app.py           # Streamlit web app
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/credit-card-fraud-detection.git
cd credit-card-fraud-detection
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Run model training

```
python main.py
```

---

### 5. Run Streamlit app

```
streamlit run app.py
```

---

## 📊 Model Details

* Algorithm: Random Forest Classifier
* Problem Type: Binary Classification
* Target:

  * 0 → Normal Transaction
  * 1 → Fraudulent Transaction

---

## 🚀 Future Improvements

* Real-time API integration
* Advanced models (XGBoost, Deep Learning)
* Better feature engineering
* Live transaction streaming

---

## 🙏 Acknowledgment

* Mentor guidance and support
* Learning support from Indian Institute of Placement

---

## 👨‍💻 Author

Yashika Aggarwal

---

⭐ If you like this project, consider giving it a star!
