# PERFORMANCE EVALUATION METRICS

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report,
    roc_auc_score, roc_curve
)
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data.csv")   # replace with your dataset

# -------------------------------
# 🔹 PREPROCESSING (Basic)
# -------------------------------

# Convert categorical to numeric
data = pd.get_dummies(data, drop_first=True)

# Assume last column is target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# 🔹 TRAIN MODEL
# -------------------------------

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# -------------------------------
# 🔹 EVALUATION METRICS
# -------------------------------

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Precision
print("Precision:", precision_score(y_test, y_pred, average='binary'))

# Recall
print("Recall:", recall_score(y_test, y_pred, average='binary'))

# F1 Score
print("F1 Score:", f1_score(y_test, y_pred, average='binary'))

# Confusion Matrix
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Classification Report
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# ROC-AUC Score
print("ROC-AUC Score:", roc_auc_score(y_test, y_prob))

# -------------------------------
# 🔹 ROC CURVE
# -------------------------------

fpr, tpr, thresholds = roc_curve(y_test, y_prob)

plt.plot(fpr, tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.show()