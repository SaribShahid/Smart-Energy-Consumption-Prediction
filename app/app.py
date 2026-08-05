import streamlit as st
import pandas as pd
from model_loader import load_model

# Load the trained model
model = load_model()

st.set_page_config(page_title="Smart Energy Consumption Prediction")

st.title("🏠 Smart Energy Consumption Prediction")
st.write("Predict appliance energy consumption using the trained machine learning model.")

# List of input features (same order as used for training)
feature_names = [
    "lights", "T1", "RH_1", "T2", "RH_2", "T3", "RH_3", "T4", "RH_4",
    "T5", "RH_5", "T6", "RH_6", "T7", "RH_7", "T8", "RH_8", "T9",
    "RH_9", "T_out", "Press_mm_hg", "RH_out", "Windspeed",
    "Visibility", "Tdewpoint", "Year", "Month", "Day",
    "Hour", "Minute", "DayOfWeek", "IsWeekend"
]

user_input = {}

st.subheader("Enter Feature Values")

for feature in feature_names:
    user_input[feature] = st.number_input(feature, value=0.0)

if st.button("Predict"):

    input_df = pd.DataFrame([user_input])

    prediction = model.predict(input_df)

    st.success(f"Predicted Energy Consumption: {prediction[0]:.2f} Wh")