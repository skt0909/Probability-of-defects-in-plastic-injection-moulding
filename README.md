# Probability of Defects in Plastic Injection Moulding

A Streamlit dashboard for predicting plastic injection moulding quality based on key process parameters. The app loads pre-trained Random Forest and Decision Tree models, accepts user input for melt temperature, mold temperature, and time to fill, then displays a prediction along with feature importance.

## Features

- Select between Random Forest and Decision Tree models
- Input melt temperature, mold temperature, and time to fill
- Display predicted defect category:
  - Waste
  - Acceptable
  - Target
  - Inefficient
- Show feature importance chart for the selected model

## Project Structure

- `main.py` - Streamlit app entrypoint
- `requirements.txt` - Python dependencies
- `Input_data/input_data.py` - Converts input values into a DataFrame for prediction
- `Visualization/visualization.py` - Generates feature importance plots in Streamlit
- `Model file/` - Contains pretrained model pickle files

## Requirements

- Python 3.8+ (recommended)
- Install dependencies from `requirements.txt`

## Installation

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app from the project root:

```bash
streamlit run main.py
```

Open the URL shown in the terminal to use the dashboard.

## Notes

- Ensure the model files `rf_model_3_features.pkl` and `dt_model_3_features.pkl` are present in the `Model file/` directory.
- The app expects the model input features to be named:
  - `Melt temperature`
  - `Mold temperature`
  - `time_to_fill`

## License

Add your preferred license here.
