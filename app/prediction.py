import pandas as pd
from app.model_loader import load_model

# Load the trained model
model = load_model()

def predict(input_data):
    """
    Predict appliance energy consumption.
    """

    if isinstance(input_data, dict):
        input_data = pd.DataFrame([input_data])

    prediction = model.predict(input_data)

    return prediction