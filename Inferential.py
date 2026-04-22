# INFERENTIAL STATISTICS

import pandas as pd
import numpy as np
from scipy import stats

# Load dataset
data = pd.read_csv("data.csv")   # replace with your dataset

# Select numeric columns
num_cols = data.select_dtypes(include=np.number).columns

# -------------------------------
# 🔹 ONE-SAMPLE T-TEST
# -------------------------------

col = num_cols[0]   # first numeric column
t_stat, p_value = stats.ttest_1samp(data[col].dropna(), popmean=50)

print("\nOne Sample T-Test:")
print("Column:", col)
print("T-statistic:", t_stat)
print("P-value:", p_value)

# -------------------------------
# 🔹 INDEPENDENT T-TEST
# -------------------------------

if len(num_cols) >= 2:
    col1 = num_cols[0]
    col2 = num_cols[1]

    t_stat2, p_value2 = stats.ttest_ind(
        data[col1].dropna(),
        data[col2].dropna()
    )

    print("\nIndependent T-Test:")
    print("Columns:", col1, "vs", col2)
    print("T-statistic:", t_stat2)
    print("P-value:", p_value2)

# -------------------------------
# 🔹 CHI-SQUARE TEST
# -------------------------------

cat_cols = data.select_dtypes(include='object').columns

if len(cat_cols) >= 2:
    contingency = pd.crosstab(data[cat_cols[0]], data[cat_cols[1]])

    chi2, p, dof, expected = stats.chi2_contingency(contingency)

    print("\nChi-Square Test:")
    print("Chi2:", chi2)
    print("P-value:", p)

# -------------------------------
# 🔹 ANOVA TEST
# -------------------------------

if len(num_cols) >= 3:
    f_stat, p_val = stats.f_oneway(
        data[num_cols[0]].dropna(),
        data[num_cols[1]].dropna(),
        data[num_cols[2]].dropna()
    )

    print("\nANOVA Test:")
    print("F-statistic:", f_stat)
    print("P-value:", p_val)

# -------------------------------
# 🔹 INTERPRETATION
# -------------------------------

alpha = 0.05

print("\nInterpretation Rule:")
print("If p-value < 0.05 → Significant (Reject H0)")
print("If p-value >= 0.05 → Not Significant (Accept H0)")