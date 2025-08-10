import plotly.graph_objects as go
import numpy as np
import streamlit as st

def visualization(model):
    """
    Plot feature importance bar chart using Plotly.
    """
    # Get feature importance from model (assuming model is a tree-based model)
    if hasattr(model, 'feature_importances_'):
        importance = model.feature_importances_
    else:
        st.error("Model does not have feature importances")
        return

    features = ['Melt temperature', 'Mold temperature', 'time_to_fill']

    # Sort feature importance
    sorted_idx = np.argsort(importance)[::-1]

    sorted_importance = importance[sorted_idx]
    sorted_features = [features[i] for i in sorted_idx]

    # Create the bar chart
    fig = go.Figure(
        data=[go.Bar(
            x=sorted_importance,
            y=sorted_features,
            orientation='h'
        )]
    )

    fig.update_layout(
        title="Feature Importance",
        xaxis_title="Importance",
        yaxis_title="Features",
        template="plotly_white"
    )

    # Show the chart in Streamlit
    st.plotly_chart(fig)
