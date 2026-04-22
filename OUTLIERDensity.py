# DENSITY-BASED OUTLIER DETECTION (DBSCAN)

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv("data.csv")

# Select numeric data
X = data.select_dtypes(include=np.number)

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X_scaled)

# Outliers are labeled as -1
data['Outlier_DBSCAN'] = labels == -1

print("Number of outliers (DBSCAN):", sum(data['Outlier_DBSCAN']))
print(data.head())