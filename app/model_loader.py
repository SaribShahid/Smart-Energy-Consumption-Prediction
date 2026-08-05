import joblib

MODEL_PATH = "models/energy_model.joblib"

def load_model():
    """
    Load the trained model.
    """
    return joblib.load(MODEL_PATH)