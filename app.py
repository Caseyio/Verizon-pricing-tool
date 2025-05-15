import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("telco_pricing_ready.csv")
df['base_plan'] = df['base_plan'].astype(str)
df['segment_type'] = df['segment_type'].astype(str)

st.set_page_config(layout="wide")
st.title("📊 Smart Pricing & Revenue Planner")

tab1, tab2, tab3 = st.tabs([
    "💡 Pricing Efficiency", 
    "🔄 Mix Optimizer", 
    "📅 Annual Plan Simulator"
])

with tab1:
    st.header("💡 Pricing Efficiency View")
    st.markdown("Explore ARPU performance by customer segment and plan type.")

    st.subheader("Segment + Plan Level Table")
    st.dataframe(df[['segment_type', 'base_plan', 'monthly_charge', 'promo_discount', 'arpu']])

    st.subheader("ARPU Distribution by Plan")
    fig = px.box(df, x='base_plan', y='arpu', color='segment_type', title='ARPU by Plan and Segment')
    st.plotly_chart(fig, use_container_width=True)
