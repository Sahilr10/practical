# DATA VISUALIZATION TECHNIQUES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("Titanic-Dataset.csv")   # replace with your dataset

print("Dataset Preview:\n", data.head())

# -------------------------------
# 🔹 1. HISTOGRAM
# -------------------------------

data.hist(figsize=(10, 8))
plt.suptitle("Histogram of Features")
plt.show()

# -------------------------------
# 🔹 2. BOXPLOT
# -------------------------------

sns.boxplot(data=data.select_dtypes(include=np.number))
plt.title("Boxplot (Detect Outliers)")
plt.show()

# -------------------------------
# 🔹 3. SCATTER PLOT
# -------------------------------

num_cols = data.select_dtypes(include=np.number).columns

if len(num_cols) >= 2:
    plt.scatter(data[num_cols[0]], data[num_cols[1]])
    plt.xlabel(num_cols[0])
    plt.ylabel(num_cols[1])
    plt.title("Scatter Plot")
    plt.show()

# -------------------------------
# 🔹 4. LINE PLOT
# -------------------------------

if len(num_cols) >= 1:
    plt.plot(data[num_cols[0]])
    plt.title("Line Plot")
    plt.xlabel("Index")
    plt.ylabel(num_cols[0])
    plt.show()

# -------------------------------
# 🔹 5. BAR PLOT
# -------------------------------

cat_cols = data.select_dtypes(include='object').columns

if len(cat_cols) >= 1:
    data[cat_cols[0]].value_counts().plot(kind='bar')
    plt.title("Bar Plot (Category Count)")
    plt.xlabel(cat_cols[0])
    plt.ylabel("Count")
    plt.show()

# -------------------------------
# 🔹 6. PIE CHART
# -------------------------------

if len(cat_cols) >= 1:
    data[cat_cols[0]].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Pie Chart")
    plt.ylabel("")
    plt.show()

# -------------------------------
# 🔹 7. HEATMAP (CORRELATION)
# -------------------------------

corr = data.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# -------------------------------
# 🔹 8. PAIR PLOT
# -------------------------------

sns.pairplot(data.select_dtypes(include=np.number))
plt.show()