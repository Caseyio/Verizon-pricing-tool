import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

st.set_page_config(page_title="Verizon ARPU Intelligence", layout="wide")

# Load model and segment summary
@st.cache_resource
def load_model():
    return joblib.load("data/model_v1.0c_xgboost.pkl")

@st.cache_data
def load_data():
    return pd.read_csv("data/segment_summary.csv")

model = load_model()
summary = load_data()

# ---------- 🎨 Styling ----------
st.markdown("""
<style>
body, .main {
    background-color: #ffffff;
    color: #111;
    font-family: "Helvetica Neue", sans-serif;
}
.stTabs [data-baseweb="tab"] {
    font-size: 18px;
    font-weight: 600;
    border-bottom: 3px solid transparent;
}
.stTabs [data-baseweb="tab"]:hover {
    color: #ff0000 !important;
}
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    border-color: #ffef00;
    color: #000;
}
h1, h2, h3 {
    color: #cc0000;
}
.stButton>button {
    background-color: #cc0000;
    color: white;
    border-radius: 8px;
    padding: 0.5em 1.5em;
}
.stButton>button:hover {
    background-color: #990000;
}
.stDataFrame, .element-container {
    border-left: 6px solid #ffef00;
    padding-left: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# ---------- 🎯 App Title ----------
st.title("📡 Verizon Wireless ARPU Intelligence Tool")
st.markdown("Forecast, simulate, and optimize revenue performance by segment.")

# ---------- 🗂 Tabs ----------
tab1, tab2, tab3 = st.tabs(["Efficiency View", "Mix Simulator", "Annual Plan"])

# ---------- 📊 Tab 1: Efficiency View ----------
with tab1:
    st.subheader("💡 Efficiency by Contract & Discount")

    col1, col2 = st.columns(2)
    selected_contract = col1.selectbox("Select Contract Type", sorted(summary["contract"].unique()))
    selected_discount = col2.selectbox("Select Discount Level", sorted(summary["discount_level"].unique()))

    filtered = summary[
        (summary["contract"] == selected_contract) &
        (summary["discount_level"] == selected_discount)
    ]

    st.markdown(f"#### ARPU Snapshot: `{selected_contract}` with `{selected_discount}` discount")
    st.dataframe(filtered, use_container_width=True)

    fig = px.bar(summary, x="contract", y="arpu_mean", color="discount_level",
                 barmode="group", title="ARPU by Contract Type and Discount Level",
                 labels={"arpu_mean": "Average ARPU", "contract": "Contract Type"})
    st.plotly_chart(fig, use_container_width=True)

# ---------- ⚙️ Tab 2: Mix Simulator ----------
with tab2:
    st.subheader("🎛️ Mix Optimization Simulator")
    st.markdown("Adjust segment traits to simulate ARPU outcome.")

    col1, col2, col3 = st.columns(3)
    mix_contract = col1.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    mix_loyalty = col2.selectbox("Loyalty Tier", ["New", "Established", "Loyal", "Very Loyal"])
    mix_discount = col3.selectbox("Discount Level", ["Low", "Medium", "High"])

    col4, col5 = st.columns([2, 1])
    mix_tenure = col4.slider("Customer Tenure (months)", 1, 72, 24)
    senior = col5.checkbox("Senior Citizen", value=False)
    service_type = st.radio("Service Type", ["fiber", "dsl", "none"], horizontal=True)

    # Prepare input
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

# ---------- 📅 Tab 3: Annual Plan ----------
with tab3:
    st.subheader("📅 ARPU Forecast Planner")
    st.markdown("Model monthly ARPU growth and churn for planning.")

    base_arpu = st.slider("Base ARPU", 20.0, 120.0, 75.0)
    churn_rate = st.slider("Monthly Churn Rate (%)", 0.0, 10.0, 1.5) / 100
    growth_rate = st.slider("Monthly Growth Rate (%)", 0.0, 10.0, 2.0) / 100

    forecast = []
    current = base_arpu
    for _ in range(12):
        current *= (1 - churn_rate + growth_rate)
        forecast.append(current)

    forecast_df = pd.DataFrame({"Month": range(1, 13), "Projected ARPU": forecast})
    fig = px.line(forecast_df, x="Month", y="Projected ARPU", markers=True,
                  title="12-Month ARPU Projection")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(forecast_df, use_container_width=True)
