import streamlit as st
import joblib
import pandas as pd

model = joblib.load("churn_model.pkl")

st.header("ChurnGuard")
st.subheader("AI-powered customer churn prediction system.")




st.text("Customer Details")

gender = st.radio(
    "Select your Gender:",
    ["Male", "Female"],
    index=None
)

senior_citizen = st.radio(
    "Are you Senior Citizen?",
    ["Yes", "No"],
    index=None
)

tenure = st.number_input(
    "Tenure (months)",
    min_value=0,
    max_value=72,
    value=12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    max_value=200.0,
    value=50.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=500.0,
    step=10.0
)

contract = st.selectbox(
    "Select your Contract:",
    ["Month-to-month", "One year", "Two year"]
)

button = st.button('Predict Churn')

gender_value = 1 if gender == "Male" else 0
senior_value = 1 if senior_citizen == 'Yes' else 0

contract_mapping = {
    "Month-to-month" : 0,
    "One year" : 1,
    "Two year" : 2
}
contract_value = contract_mapping[contract]

if button:

    input_data = pd.DataFrame({
        "gender": [gender_value],
        "SeniorCitizen": [senior_value],
        "tenure": [tenure],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges],
        "Contract": [contract_value]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error('⚠️ Prediction: This customer is likely to CHURN.')
    else:
        st.success('✅ Prediction: This customer is likely to STAY.')