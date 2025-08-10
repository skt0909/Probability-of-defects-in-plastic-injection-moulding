import pandas as pd

def input_data(melt_temperature, mold_temperature, time_to_fill):
    """
    Converts user input into a DataFrame for model prediction.
    """
    return pd.DataFrame({
        'Melt temperature': [melt_temperature],
        'Mold temperature': [mold_temperature],
        'time_to_fill': [time_to_fill]
    })
