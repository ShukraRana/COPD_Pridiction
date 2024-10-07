import os
import joblib

# Check the current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# Update the model path if needed
model_path = os.path.join(current_dir, 'Best_Random_Forest_Model.pkl')

# Load the model
with open(model_path, 'rb') as f:
    model = joblib.load(f)
