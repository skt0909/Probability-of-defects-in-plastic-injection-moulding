import streamlit as st
import pickle
import pandas as pd
from Input_data.input_data import input_data
from Visualization.visualization import visualization

# Load the models from .pkl files
def load_model(model_path):
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

# Load models
rf_model = load_model('Model file/rf_model_3_features.pkl')
dt_model = load_model('Model file/dt_model_3_features.pkl')

# Mapping prediction values to labels
prediction_labels = {
    1.0: "Waste",
    2.0: "Acceptable",
    3.0: "Target",
    4.0: "Inefficient"
}

# Main app
def main():
    st.title("Model Prediction Dashboard")

    # Model Selection
    model_choice = st.radio(
        "Choose a Model:",
        ("Random Forest", "Decision Tree")
    )

    # Number input fields for feature input
    st.subheader("Enter Feature Values")
    melt_temperature = st.number_input('Melt Temperature', min_value=00.0, max_value=100000.0, value=00.0)
    mold_temperature = st.number_input('Mold Temperature', min_value=00.0, max_value=100000.0, value=00.0)
    time_to_fill = st.number_input('Time to Fill', min_value=00, max_value=90, value=00)

    # Create DataFrame from input_data function
    input_df = input_data(melt_temperature, mold_temperature, time_to_fill)

    # Select model based on user choice
    selected_model = rf_model if model_choice == "Random Forest" else dt_model

    # Make predictions
    if st.button("Predict"):
        raw_prediction = selected_model.predict(input_df)[0]  # Get the numeric prediction
        prediction_text = prediction_labels.get(raw_prediction, "Unknown")  # Map to label

        st.subheader("Prediction Result")
        st.write(f"**{model_choice} Model Prediction:** {prediction_text} ({raw_prediction})")

    # Show feature importance bar chart
    st.subheader("Feature Importance")
    visualization(selected_model)

if __name__ == "__main__":
    main()
