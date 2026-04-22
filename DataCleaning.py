# DATA CLEANING TECHNIQUES

import pandas as pd
import numpy as np

# Load dataset
data = pd.read_csv("data.csv")   # replace with your dataset

print("Original Dataset:\n", data.head())

# -------------------------------
# 🔹 1. HANDLE MISSING VALUES
# -------------------------------

# Check missing values
print("\nMissing Values:\n", data.isnull().sum())

# Fill missing numeric values with mean
for col in data.select_dtypes(include=np.number).columns:
    data[col].fillna(data[col].mean(), inplace=True)

# Fill categorical values with mode
for col in data.select_dtypes(include='object').columns:
    data[col].fillna(data[col].mode()[0], inplace=True)

# -------------------------------
# 🔹 2. REMOVE DUPLICATES
# -------------------------------

data.drop_duplicates(inplace=True)

# -------------------------------
# 🔹 3. HANDLE OUTLIERS (IQR METHOD)
# -------------------------------

for col in data.select_dtypes(include=np.number).columns:
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Remove outliers
    data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]

# -------------------------------
# 🔹 4. DATA TYPE CONVERSION
# -------------------------------

# Convert to appropriate types if needed
# Example:
# data['Age'] = data['Age'].astype(int)

# -------------------------------
# 🔹 5. HANDLE INCONSISTENT DATA
# -------------------------------

# Standardize text (lowercase, remove spaces)
for col in data.select_dtypes(include='object').columns:
    data[col] = data[col].str.lower().str.strip()

# -------------------------------
# 🔹 6. ENCODING CATEGORICAL DATA
# -------------------------------

# Convert categorical columns into numeric
data = pd.get_dummies(data, drop_first=True)

# -------------------------------
# 🔹 7. FEATURE SCALING
# -------------------------------

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
num_cols = data.select_dtypes(include=np.number).columns

data[num_cols] = scaler.fit_transform(data[num_cols])

# -------------------------------
# 🔹 FINAL CLEANED DATA
# -------------------------------

print("\nCleaned Dataset:\n", data.head())

# Save cleaned dataset
data.to_csv("cleaned_data.csv", index=False)

print("\nData cleaning completed and saved as 'cleaned_data.csv'")