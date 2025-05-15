# 📊 Smart Pricing & Revenue Planner

An interactive Streamlit dashboard that combines machine learning, customer segmentation, and pricing simulation to support strategic revenue planning.

> ⚙️ Built as a real-world case study aligned with enterprise pricing and analytics roles — like Verizon's Pricing Analytics team.

---

## 🚀 Try the App

👉 **Live Streamlit App:** [https://your-streamlit-url.streamlit.app](#)  
📦 **GitHub Repo:** [https://github.com/yourusername/Verizon-pricing-tool](#)

---

## 🎯 Use Cases

This app simulates the work of a telecom pricing analytics team by answering key questions:

- What pricing tiers and customer segments are underperforming?
- How does the customer mix affect overall ARPU?
- How will ARPU evolve over the year if we adjust price, discount, or growth?

---

## 🧱 App Features

### 💡 Tab 1: Pricing Efficiency View
Explore ARPU performance by segment and plan. Identify pricing inefficiencies and underperforming combinations.

- ARPU box plot by plan and segment
- Interactive data table with monthly charge and promo data

### 🔄 Tab 2: Mix Optimizer
Adjust the customer distribution across Basic, Plus, and Premium plans to simulate the impact on average ARPU.

- Sliders for customer mix (%)
- Real-time ARPU impact metric

### 📅 Tab 3: Annual Plan Simulator
Project ARPU growth over 12 months based on adjustable pricing strategy inputs.

- Sliders for base price, promo discount, customer growth rate
- ARPU forecast chart + total annual revenue metric

---

## 📊 Behind the Scenes

- **Dataset:** Based on real Telco customer churn data enriched with broadband pricing (FCC data)
- **Model:** XGBoost regressor trained to predict ARPU
- **Stack:** Streamlit, Pandas, Plotly, Scikit-learn, XGBoost

---

## 📁 File Structure

