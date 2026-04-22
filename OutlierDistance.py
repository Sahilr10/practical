
# DISTANCE-BASED OUTLIER DETECTION (KNN)

import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv("data.csv")

# Select only numeric data
X = data.select_dtypes(include=np.number)

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply KNN
k = 5
knn = NearestNeighbors(n_neighbors=k)
knn.fit(X_scaled)

# Compute distances
distances, _ = knn.kneighbors(X_scaled)

# Take average distance
avg_distance = distances.mean(axis=1)

# Set threshold (top 5% as outliers)
threshold = np.percentile(avg_distance, 95)

# Identify outliers
outliers = avg_distance > threshold

# Add result to dataset
data['Outlier_KNN'] = outliers

print("Number of outliers (KNN):", sum(outliers))
print(data.head())