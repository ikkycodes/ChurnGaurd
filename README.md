# ChurnGaurd
An AI-powered customer churn prediction project that uses machine learning and a Streamlit interface to predict whether a customer is likely to stay or churn

# 🛡️ ChurnGuard — Customer Churn Prediction

ChurnGuard is an AI-powered customer churn prediction system that uses **Machine Learning and Streamlit** to predict whether a customer is likely to **churn or stay**.

The project covers the complete ML workflow, including data exploration, data cleaning, model training, model saving, and deployment through a user-friendly Streamlit interface.

## 🚀 Features

* Customer data exploration
* Data cleaning and preprocessing
* Missing-value handling
* Duplicate removal
* Categorical data normalization and encoding
* Logistic Regression model
* Churn prediction
* Churn probability
* Interactive Streamlit UI
* Saved trained model using Joblib

## 📁 Project Structure

```text
ChurnGuard/
│
├── churnguard_data.csv
├── clean_data.csv
│
├── task1_load_explore.py
├── task2_clean_data.py
├── task3_train_model.py
├── task4_predict.py
├── train_app_model.py
│
├── churn_model.pkl
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 📌 Project Workflow

```text
Raw Dataset
     ↓
Data Exploration
     ↓
Data Cleaning
     ↓
Feature Preparation
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Save Model
     ↓
Streamlit UI
     ↓
Customer Input
     ↓
Churn Prediction
```

## 📋 Tasks

### Task 1 — Data Exploration

Loads the ChurnGuard dataset and explores:

* Dataset shape
* First few records
* Column information
* Missing values
* Duplicate rows
* Churn distribution
* Unique contract values

### Task 2 — Data Cleaning

Cleans and prepares the dataset by:

* Removing `customerID`
* Removing duplicates
* Cleaning whitespace
* Standardizing categorical values
* Normalizing contract types
* Converting `TotalCharges` to numeric
* Handling invalid values
* Removing invalid tenure and charge values
* Handling missing values

The cleaned dataset is saved as:

```text
clean_data.csv
```

### Task 3 — Model Training

Trains a **Logistic Regression** classification model using the cleaned data.

The model is evaluated using classification metrics and saved for later use.

### Task 4 — Prediction

Allows customer information to be provided and generates a churn prediction.

### Streamlit Application

`app.py` provides an interactive UI where users can enter customer information and receive:

* Churn prediction
* Stay prediction
* Churn probability

## 🤖 Machine Learning Model

**Algorithm:** Logistic Regression

Logistic Regression is used because ChurnGuard is a **binary classification problem**:

```text
0 → Stay
1 → Churn
```

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/<username>/ChurnGuard.git
```

Move into the project directory:

```bash
cd ChurnGuard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 📊 Prediction

The application takes customer information and passes it to the trained Logistic Regression model.

```text
Customer Details
       ↓
Feature Processing
       ↓
Logistic Regression
       ↓
Prediction
       ↓
Churn / Stay
```

## 🔮 Future Improvements

* Add additional ML models for comparison
* Improve model accuracy
* Add feature importance
* Add customer risk levels
* Add model performance dashboard
* Add database integration
* Deploy the application to the cloud

## 👨‍💻 Author

**Your Name**

GitHub: https://github.com/ikkycodes

---

⭐ If you found ChurnGuard useful, consider giving the repository a star!
