import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Verizon Pricing Intelligence Tool", layout="wide")

# ---- Custom Styling ----
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Helvetica', sans-serif;
    }
    .main {
        background-color: #ffffff;
        color: #222222;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #f3f3f3;
        padding: 10px;
        border-radius: 6px 6px 0 0;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        background-color: #DA291C;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Load Data ----
@st.cache_data

def load_data():
    df = pd.read_csv("telco_pricing_ready.csv")
    return df

df = load_data()

# ---- Tabs ----
tabs = st.tabs(["Efficiency View", "Mix Simulator", "Annual Plan"])

# ---- Tab 1: Efficiency View ----
with tabs[0]:
    st.header("📊 Efficiency View")
    st.markdown("Identify pricing inefficiencies by segment.")

    group_cols = ["contract_label", "loyalty_label", "discount_label"]
    summary = df.groupby(group_cols).agg(
        arpu_mean=("arpu", "mean"),
        churn_rate=("churn", "mean"),
        count=("arpu", "count")
    ).reset_index().sort_values("arpu_mean", ascending=False)

    st.dataframe(summary.head(10), use_container_width=True)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(
        data=summary.head(10),
        x="arpu_mean", y="contract_label", hue="discount_label",
        palette="Reds_r"
    )
    ax.set_title("Top Segments by ARPU")
    ax.set_xlabel("Average ARPU")
    ax.set_ylabel("Contract Type")
    st.pyplot(fig)

# ---- Tab 2 and 3 placeholders ----
with tabs[1]:
    st.header("🧮 Mix Simulator")
    st.markdown("Coming soon: Adjust product/customer mix and simulate ARPU impact.")

with tabs[2]:
    st.header("📅 Annual Price Plan")
    st.markdown("Coming soon: Forecast ARPU by quarter based on price, mix, and churn inputs.")
