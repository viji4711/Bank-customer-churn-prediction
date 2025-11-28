import streamlit as st
import pandas as pd
import joblib

# Load model & preprocessor
model = joblib.load("models/churn_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

st.title("Customer Churn Prediction App")

st.write("Enter customer details below:")

# UI inputs
CreditScore = st.number_input("Credit Score", min_value=0, max_value=1000, value=600)
Geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
Gender = st.selectbox("Gender", ["Female", "Male"])
Age = st.number_input("Age", min_value=18, max_value=100, value=30)
Tenure = st.number_input("Tenure (Years)", min_value=0, max_value=20, value=5)
Balance = st.number_input("Balance", min_value=0.0, step=100.0)
NumOfProducts = st.number_input("Number of Products", min_value=1, max_value=4, value=1)
HasCrCard = st.selectbox("Has Credit Card?", [0, 1])
IsActiveMember = st.selectbox("Is Active Member?", [0, 1])
EstimatedSalary = st.number_input("Estimated Salary", min_value=0.0, step=100.0)
Complain = st.selectbox("Complain (0 = No, 1 = Yes)", [0, 1])
SatisfactionScore = st.number_input("Satisfaction Score", min_value=1, max_value=5, value=3)
CardType = st.selectbox("Card Type", ["DIAMOND", "GOLD", "PLATINUM", "SILVER"])
PointEarned = st.number_input("Points Earned", min_value=0, value=100)

# Prepare dataframe exactly as preprocessor expects
input_data = pd.DataFrame({
    "CreditScore": [CreditScore],
    "Geography": [Geography],
    "Gender": [Gender],
    "Age": [Age],
    "Tenure": [Tenure],
    "Balance": [Balance],
    "NumOfProducts": [NumOfProducts],
    "HasCrCard": [HasCrCard],
    "IsActiveMember": [IsActiveMember],
    "EstimatedSalary": [EstimatedSalary],
    "Complain": [Complain],
    "SatisfactionScore": [SatisfactionScore],
    "CardType": [CardType],
    "PointEarned": [PointEarned]
})

if st.button("Predict Churn"):
    # Transform with preprocessor
    processed = preprocessor.transform(input_data)

    # Predict probability
    prediction = model.predict(processed)[0]
    prob = model.predict_proba(processed)[0][1]

    st.subheader("Prediction Result:")
    if prediction == 1:
        st.error(f"❌ Customer is likely to CHURN (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Customer will NOT churn (Probability: {prob:.2f})")
