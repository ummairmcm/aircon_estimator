import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Aircon Cost Estimator", page_icon="❄️")

# Load your newly trained Random Forest model
model = joblib.load("aircon_model.pkl")

st.title("Air Conditioner Electricity Cost Estimator")
st.write("Using a Machine Learning Regression Model to predict real-world monthly consumption.")

# 1. User Inputs
power = st.number_input(
    "Power Rating (Watts)",
    min_value=0.0,
    value=1030.0,
    help="Check your AC's technical specification sticker or yellow label for input power."
)

# Because your model expects CSPF during .predict(), we collect it here.
# (If you still want it hidden, you can hardcode this to a standard default like 5.0)
cspf = st.number_input(
    "Energy Efficiency Rating (CSPF)",
    min_value=0.0,
    value=5.70,
    help="Cooling Seasonal Performance Factor found on the yellow energy guide label."
)

# Your critical added feature!
hours = st.slider(
    "Average Daily Usage (Hours)",
    min_value=1.0,
    max_value=24.0,
    value=8.0,
    step=0.5
)

rate = st.number_input(
    "Electricity Rate (₱/kWh)",
    min_value=0.0,
    value=12.50,
    help="Look at your latest electrical utility bill for the total rate per kWh."
)

# 2. Execution and Prediction
if st.button("Estimate with ML", type="primary"):

    # CRITICAL: Feature names must precisely match the X training columns
    input_data = pd.DataFrame({
        "POWER_RATING": [power],
        "CSPF": [cspf], 
        "HOURS_USED": [hours]
    })

    # The ML model evaluates the row and predicts your scaled monthly consumption
    predicted_monthly_kwh = model.predict(input_data)[0]
    
    # Financial projections
    monthly_cost = predicted_monthly_kwh * rate
    yearly_cost = monthly_cost * 12

    st.success("ML Prediction Complete!")
    st.write("---")

    # Display Metrics
    st.metric(
        "Estimated Monthly Energy Consumption",
        f"{predicted_monthly_kwh:.2f} kWh"
    )

    st.metric(
        "Estimated Monthly Electricity Cost",
        f"₱{monthly_cost:,.2f}"
    )

    st.metric(
        "Estimated Yearly Electricity Cost",
        f"₱{yearly_cost:,.2f}"
    )