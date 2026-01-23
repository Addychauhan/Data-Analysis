import streamlit as st
import pandas as pd
import joblib


# Load model & scaler
model = joblib.load("churn_model.pkl")
sch_scaler = joblib.load("scaler.pkl")
feature_order = joblib.load("feature_order.pkl")

st.write(model.feature_names_in_)


num_cols = [
    'CreditScore',
    'Age',
    'Tenure',
    'Balance',
    'NumOfProducts',
    'EstimatedSalary'
]

st.title("Customer Churn Prediction App")

credit_score = st.number_input("Credit Score", 300, 850, 600)
age = st.number_input("Age", 18, 100, 35)
tenure = st.slider("Tenure (years)", 0, 10, 3)
balance = st.number_input("Balance", 0.0, 300000.0, 50000.0)
salary = st.number_input("Estimated Salary", 0.0, 200000.0, 50000.0)

num_products = st.number_input("Number of Products", min_value=1, max_value=4, value=1, step=1)


# num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
has_card = st.selectbox("Has Credit Card", [0, 1])
active = st.selectbox("Is Active Member", [0, 1])
gender = st.selectbox("Gender", ["Female", "Male"])
geo = st.selectbox("Geography", ["France", "Germany", "Spain"])

if st.button("Predict Churn"):

    new_customer = pd.DataFrame([{
        'CreditScore': credit_score,
        'Age': age,
        'Tenure': tenure,
        'Balance': balance,
        
        'NumOfProducts': num_products,
        'HasCrCard': has_card,
        'IsActiveMember': active,
        'EstimatedSalary': salary,
        'Geography_Germany': 1 if geo == "Germany" else 0,
        'Geography_Spain': 1 if geo == "Spain" else 0,
        'Gender_Male': 1 if gender == "Male" else 0
    }])

    new_customer[num_cols] = sch_scaler.transform(new_customer[num_cols])

    prediction = model.predict(new_customer)[0]
    probability = model.predict_proba(new_customer)[0][1]

    if prediction == 1:
        st.error(f"⚠ Customer is likely to churn (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Customer will NOT churn (Probability: {probability:.2f})")