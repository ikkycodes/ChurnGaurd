import pandas as pd

# 1. Load dataset
df = pd.read_csv('churnguard_data.csv')

# 2. Print shape
print("Shape of dataset:")
print(df.shape)

# 3. Print first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# 4. Print column names and data types
print("\nColumn names and data types:")
df.info()

# 5. Print missing values
print("\nMissing values:")
print(df.isnull().sum())

# 6. Print number of duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# 7. Print Churn value counts
print("\nChurn value counts:")
print(df['Churn'].value_counts())

# 8. Print unique Contract values
print("\nUnique Contract values:")
print(df['Contract'].unique())