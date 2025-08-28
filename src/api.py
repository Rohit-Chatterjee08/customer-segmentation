# in src/api.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path # <<< ADD THIS IMPORT

# --- 1. Initialize FastAPI App ---
app = FastAPI(
    title="Customer Segmentation API",
    description="An API to predict customer segments based on their data."
)

# --- 2. Load Saved Model and Scaler (Robustly) ---
# <<< THIS SECTION IS CHANGED
# Get the directory of the current script
BASE_DIR = Path(__file__).resolve(strict=True).parent

# Define the paths to the model and scaler relative to this script
SCALER_PATH = BASE_DIR.parent / "models" / "scaler.joblib"
MODEL_PATH = BASE_DIR.parent / "models" / "kmeans_model.joblib"

# Load the artifacts using the absolute paths
scaler = joblib.load(SCALER_PATH)
model = joblib.load(MODEL_PATH)

# --- 3. Define Human-Readable Segment Names ---
segment_names = {
    0: 'Standard',
    1: 'Careful',
    2: 'Target (High-Spending)',
    3: 'Careless',
    4: 'Sensible'
}

# --- 4. Define the Input Data Model using Pydantic ---
class CustomerData(BaseModel):
    annual_income: float
    spending_score: float

# --- 5. Create the Prediction Endpoint ---
@app.post("/segment")
def predict_segment(customer_data: CustomerData):
    """
    Predicts the customer segment for a given set of data.
    """
    input_df = pd.DataFrame([customer_data.dict()])
    
    input_df.rename(columns={
        'annual_income': 'Annual Income (k$)',
        'spending_score': 'Spending Score (1-100)'
    }, inplace=True)
    
    scaled_features = scaler.transform(input_df)
    
    predicted_cluster = model.predict(scaled_features)[0]
    
    segment_name = segment_names.get(predicted_cluster, "Unknown Segment")
    
    return {
        "segment_id": int(predicted_cluster),
        "segment_name": segment_name
    }