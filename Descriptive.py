# DESCRIPTIVE STATISTICS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("data.csv")   # replace with your dataset

# Preview
print("Dataset:\n", data.head())

# -------------------------------
# 🔹 BASIC STATISTICS
# -------------------------------

print("\nSummary Statistics:")
print(data.describe())

# Mean
print("\nMean:\n", data.mean(numeric_only=True))

# Median
print("\nMedian:\n", data.median(numeric_only=True))

# Mode
print("\nMode:\n", data.mode().iloc[0])

# Standard Deviation
print("\nStandard Deviation:\n", data.std(numeric_only=True))

# Variance
print("\nVariance:\n", data.var(numeric_only=True))

# -------------------------------
# 🔹 CORRELATION
# -------------------------------

print("\nCorrelation Matrix:\n", data.corr(numeric_only=True))

# -------------------------------
# 🔹 VISUALIZATION
# -------------------------------

# Histogram
data.hist(figsize=(10, 8))
plt.suptitle("Histograms")
plt.show()

# Boxplot
sns.boxplot(data=data.select_dtypes(include=np.number))
plt.title("Boxplot")
plt.show()

# Heatmap
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()