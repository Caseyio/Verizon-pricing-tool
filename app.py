# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
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

# --------------------------------------------
# 💡 TAB 1: Pricing Efficiency
# --------------------------------------------
with tab1:
    st.header("💡 Pricing Efficiency View")
    st.markdown("Explore ARPU performance by customer segment and plan type.")

    st.subheader("Segment + Plan Level Table")
    st.dataframe(df[['segment_type', 'base_plan', 'monthly_charge', 'promo_discount', 'arpu']])

    st.subheader("ARPU Distribution by Plan")
    fig = px.box(df, x='base_plan', y='arpu', color='segment_type', title='ARPU by Plan and Segment')
    st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------
# 🔄 TAB 2: Mix Optimizer
# --------------------------------------------
with tab2:
    st.header("🔄 Mix Optimization Scenario")
    st.markdown("Adjust customer plan mix to simulate the impact on ARPU.")

    current_mix = df['base_plan'].value_counts(normalize=True).sort_index()

    col1, col2, col3 = st.columns(3)
    basic_pct = col1.slider("Basic %", 0, 100, int(current_mix.get("0", 0) * 100))
    plus_pct = col2.slider("Plus %", 0, 100, int(current_mix.get("1", 0) * 100))
    premium_pct = col3.slider("Premium %", 0, 100, int(current_mix.get("2", 0) * 100))

    total_pct = basic_pct + plus_pct + premium_pct

    if total_pct != 100:
        st.warning("⚠️ Total must equal 100%. Adjust sliders.")
    else:
        avg_arpu = df.groupby("base_plan")["arpu"].mean().to_dict()
        simulated_arpu = (
            basic_pct / 100 * avg_arpu.get("0", 0) +
            plus_pct / 100 * avg_arpu.get("1", 0) +
            premium_pct / 100 * avg_arpu.get("2", 0)
        )
        st.metric(label="📈 Simulated Average ARPU", value=f"${simulated_arpu:.2f}")

# --------------------------------------------
# 📅 TAB 3: Annual Price Plan Simulator
# --------------------------------------------
with tab3:
    st.header("📅 Annual Price Plan Simulator")
    st.markdown("Simulate ARPU growth over 12 months with adjustable inputs.")

    col1, col2, col3 = st.columns(3)
    base_price = col1.slider("Monthly Base Price ($)", 20, 100, 50)
    promo_discount = col2.slider("Promo Discount (%)", 0, 50, 10)
    growth_rate = col3.slider("Customer Growth Rate (%)", 0, 10, 3)

    # Calculate monthly ARPU
    net_price = base_price * (1 - promo_discount / 100)
    arpu_projection = [net_price * (1 + growth_rate / 100) ** month for month in range(12)]

    arpu_df = pd.DataFrame({
        "Month": list(range(1, 13)),
        "Projected_ARPU": arpu_projection
    })

    st.line_chart(arpu_df.set_index("Month"))

    total_revenue = sum(arpu_projection)
    st.metric(label="📊 Projected 12-Month Revenue per Customer", value=f"${total_revenue:.2f}")
