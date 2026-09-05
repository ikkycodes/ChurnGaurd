import pandas as pd


def clean_data(path='churnguard_data.csv'):
    df = pd.read_csv(path)

    # Trim stray whitespace from every text column
    # (e.g. PaymentMethod values like " Credit card " -> "Credit card")
    string_columns = df.select_dtypes(include='object').columns
    for col in string_columns:
        df[col] = df[col].str.strip()

    # Normalize inconsistent Yes/No casing (e.g. "YES", "yes" -> "Yes")
    yes_no_columns = ['PhoneService', 'PaperlessBilling', 'Churn']
    for col in yes_no_columns:
        if col in df.columns:
            df[col] = df[col].str.capitalize()

    # Normalize inconsistent Contract labels to the 3 canonical values
    # (e.g. "month to month", "Monthly" -> "Month-to-month")
    if 'Contract' in df.columns:
        contract_variants = {
            'month-to-month': 'Month-to-month',
            'month to month': 'Month-to-month',
            'monthly': 'Month-to-month',
            'one year': 'One year',
            '1 year': 'One year',
            'two year': 'Two year',
            '2 year': 'Two year'
        }
        df['Contract'] = (
            df['Contract']
            .str.strip()
            .str.lower()
            .replace(contract_variants)
        )

    # TotalCharges contains invalid entries ("?", "--", "na") and blanks,
    # so it loads as text. Convert to numeric; invalid values become NaN.
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(
            df['TotalCharges'],
            errors='coerce'
        )

    # Drop duplicate rows
    df = df.drop_duplicates()

    # Fill remaining missing values in numeric columns with the column mean
    numeric_columns = ['tenure', 'MonthlyCharges', 'TotalCharges']
    for col in numeric_columns:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].mean())

    return df

