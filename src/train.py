# in src/train.py

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib
import os

# --- 1. Load and Prepare Data ---
print("Loading data...")
# The path is relative to the script's location in src/
df = pd.read_csv('../data/Mall_Customers.csv')

# Select the features for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# --- 2. Scale the Data ---
print("Scaling data...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- 3. Train the K-Means Model ---
k = 5
print(f"Training K-Means model with {k} clusters...")
kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init='auto')
kmeans.fit(X_scaled)

print("Model training complete.")

# --- 4. Save the Model and Scaler ---
# The path is relative to the script's location in src/
models_dir = '../models'
os.makedirs(models_dir, exist_ok=True)

joblib.dump(kmeans, os.path.join(models_dir, 'kmeans_model.joblib'))
joblib.dump(scaler, os.path.join(models_dir, 'scaler.joblib'))

print(f"Model and scaler have been saved to the '{models_dir}/' directory.")