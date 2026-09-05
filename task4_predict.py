import pandas as pd
from task2_clean_data import clean_data

from sklearn.linear_model import LogisticRegression


df = clean_data()

contract_numeric = {
    'Month-to-month': 0,
    'One year': 1,
    'Two year': 2
}

df['Contract'] = df['Contract'].map(contract_numeric)


df['InternetService'] = df['InternetService'].str.strip().str.lower()

internet_mapping = {
    'dsl': 'DSL',
    'fiber optic': 'Fiber optic',
    'no': 'No'
}

df['InternetService'] = df['InternetService'].replace(internet_mapping)


df['TotalCharges'] = pd.to_numeric(
    df['TotalCharges'],
    errors='coerce'
)

df = df[df['tenure'] > 0]

df = df[
    (df['MonthlyCharges'] >= 10) &
    (df['MonthlyCharges'] <= 200)
]

df['MonthlyCharges'] = df['MonthlyCharges'].fillna(
    df['MonthlyCharges'].mean()
)

df['TotalCharges'] = df['TotalCharges'].fillna(
    df['TotalCharges'].mean()
)

df['tenure'] = df['tenure'].fillna(
    df['tenure'].median()
).round().astype(int)


df['Churn'] = df['Churn'].map({
    'Yes': 1,
    'No': 0
})


features = [
    'tenure',
    'MonthlyCharges',
    'TotalCharges',
    'SeniorCitizen',
    'Contract'
]

X = df[features]
y = df['Churn']

model = LogisticRegression(max_iter=5000)

model.fit(X, y)


tenure = int(input("Enter tenure (months): "))

MonthlyCharges = float(input("Enter Monthly Charges: "))

TotalCharges = float(input("Enter Total Charges: "))

SeniorCitizen = int(
    input("Senior Citizen? (1 = Yes, 0 = No): ")
)

Contract = int(
    input(
        "Contract type (0 = Month-to-month, "
        "1 = One year, 2 = Two year): "
    )
)

new_customer = pd.DataFrame([{
    'tenure': tenure,
    'MonthlyCharges': MonthlyCharges,
    'TotalCharges': TotalCharges,
    'SeniorCitizen': SeniorCitizen,
    'Contract': Contract
}])

prediction = model.predict(new_customer)[0]

if prediction == 1:
    print("Prediction: This customer is likely to CHURN.")
else:
    print("Prediction: This customer is likely to STAY.")