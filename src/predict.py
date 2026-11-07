import joblib
import pandas as pd
from pathlib import Path

# Get project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load model
model = joblib.load(BASE_DIR / "models" / "random_forest_model.pkl")

# Load scaler
scaler = joblib.load(BASE_DIR / "models" / "scaler.pkl")

# Load sample data
data = pd.read_csv(BASE_DIR / "models" / "sample_input.csv")

# Scale data
scaled_data = scaler.transform(data)

# Predict activity
prediction = model.predict(scaled_data)

print("Predicted Human Activity:", prediction[0])