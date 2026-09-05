import pandas as pd
from task2_clean_data import clean_data
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

df = clean_data()

le = LabelEncoder()
df['Churn'] = le.fit_transform(df['Churn'])

categorical_columns = ['gender', 'PhoneService', 'InternetService', 'Contract', 'PaperlessBilling', 'PaymentMethod']

df = df.drop(columns=['customerID'])

df = pd.get_dummies(
    df,
    columns=categorical_columns,
    drop_first=True
)

X = df.drop('Churn', axis=1)
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

lg = LogisticRegression(max_iter=5000)

lg.fit(X_train, y_train)

y_pred = lg.predict(X_test)

print(accuracy_score(y_test, y_pred))

print(classification_report(
    y_test,
    y_pred,
    target_names=['Stay', 'Churn']
))