import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

st.set_page_config(page_title="Verizon ARPU Intelligence", layout="wide")

# Load model
@st.cache_resource
def load_model():
    return joblib.load("data/model_v1.0c_xgboost.pkl")

model = load_model()

# 💅 Styling - Verizon-themed + visible tabs + clean layout
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background-color: #ffffff;
    color: #000000;
    font-family: "Helvetica Neue", sans-serif;
}
[data-testid="stSidebar"] {
    background-color: #ffffff;
}
.stTabs [data-baseweb="tab"] {
    font-size: 16px;
    font-weight: 600;
    color: #000000 !important;
    padding: 10px 16px;
}
.stTabs [data-baseweb="tab"]:hover {
    background-color: #ffef00;
}
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    background-color: #fff0f0;
    border-bottom: 3px solid #ff0000;
    color: #000000 !important;
}
h1, h2, h3, .stSubheader {
    color: #ff0000;
}
.stButton>button {
    background-color: #ff0000;
    color: white;
    border-radius: 8px;
    padding: 0.5em 1.5em;
    border: none;
}
.stButton>button:hover {
    background-color: #cc0000;
}
.stDataFrame, .element-container {
    border-left: 6px solid #ffef00;
    padding-left: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

st.title("📶 Verizon Wireless ARPU Intelligence Tool")
st.markdown("Forecast, simulate, and optimize revenue performance by segment.")

# Define Tabs FIRST
tab1, tab2, tab3 = st.tabs(["Efficiency View", "Mix Simulator", "Annual Plan"])

# ---------------- Tab 1: Efficiency View ----------------
with tab1:
    st.subheader("Efficiency by Contract & Discount")
    summary = pd.read_csv("data/segment_summary.csv")

    fig = px.bar(summary, x="contract", y="arpu_mean", color="discount_level",
                 barmode="group", title="ARPU by Contract Type and Discount Level",
                 labels={"arpu_mean": "Average ARPU", "contract": "Contract Type"},
                 template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(summary, use_container_width=True)

# ---------------- Tab 2: Mix Simulator ----------------
with tab2:
    st.subheader("🎛️ Mix Optimization Simulator")
    st.markdown("Adjust segment mix to estimate revenue impact.")

    col1, col2, col3 = st.columns(3)
    mix_contract = col1.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    mix_loyalty = col2.selectbox("Loyalty Tier", ["New", "Established", "Loyal", "Very Loyal"])
    mix_discount = col3.selectbox("Discount Level", ["Low", "Medium", "High"])

    mix_tenure = st.slider("Customer Tenure (months)", 1, 72, 24)
    senior = st.checkbox("Senior Citizen", value=False)
    service_type = st.selectbox("Service Type", ["fiber", "dsl", "none"])

    input_df = pd.DataFrame({
        "tenure": [mix_tenure],
        "seniorcitizen": [int(senior)],
        "service_type_dsl": [1 if service_type == "dsl" else 0],
        "service_type_fiber": [1 if service_type == "fiber" else 0],
        "service_type_none": [1 if service_type == "none" else 0],
        f"contract_{mix_contract}": [1],
        f"loyalty_tier_{mix_loyalty}": [1],
        f"discount_level_{mix_discount}": [1]
    })

    for col in model.feature_names_in_:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[model.feature_names_in_]

    pred_arpu = model.predict(input_df)[0]
    st.metric("📈 Projected ARPU", f"${pred_arpu:.2f}")

# ---------------- Tab 3: Annual Price Planner ----------------
with tab3:
    st.subheader("📅 ARPU Forecast Planner")
    st.markdown("Model monthly ARPU growth and churn for planning.")

    base_arpu = st.slider("Base ARPU", 20.0, 120.0, 75.0, step=1.0)
    churn_rate = st.slider("Monthly Churn Rate (%)", 0.0, 10.0, 1.5, step=0.1) / 100
    growth_rate = st.slider("Monthly Growth Rate (%)", 0.0, 10.0, 2.0, step=0.1) / 100

    months = list(range(1, 13))
    forecast = []
    current_arpu = base_arpu
    for _ in months:
        current_arpu *= (1 - churn_rate + growth_rate)
        forecast.append(current_arpu)

    forecast_df = pd.DataFrame({"Month": months, "Projected ARPU": forecast})
    fig = px.line(forecast_df, x="Month", y="Projected ARPU", markers=True,
                  title="12-Month ARPU Projection", template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(forecast_df, use_container_width=True)
