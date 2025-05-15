# 📊 Smart Pricing & Revenue Planner

**A machine learning–powered tool for telecom pricing optimization, customer mix simulation, and ARPU forecasting.**

Built as a case study to showcase applied data science and business intelligence aligned with pricing analytics roles in telecom and enterprise SaaS.

---

## 🔍 Use Case

This tool simulates a pricing analytics engine similar to what a wireless carrier like Verizon might use. It empowers analysts to:

- Predict **Average Revenue Per User (ARPU)** using XGBoost
- Identify **pricing inefficiencies** and margin erosion
- Simulate changes to **customer mix across plan tiers**
- Forecast **annual revenue performance** based on pricing strategy

---

## 🧠 How It Works

### ✅ ARPU Modeling
A regression model (XGBoost) trained on a real telco churn dataset with simulated broadband pricing logic. It predicts ARPU based on:

- Plan type
- Promo discount
- Segment type (Consumer, SMB, Enterprise)
- Monthly charges
- Churn risk score

### ✅ Tabs & Features

#### 💡 **Pricing Efficiency View**
Explore current pricing by segment and plan. Identify underperforming plans and ARPU trends.

#### 🔄 **Mix Optimizer**
Adjust customer distribution across Basic, Plus, and Premium plans. See how mix shifts impact average ARPU.

#### 📅 **Annual Plan Simulator** *(Coming Soon)*
Project ARPU and revenue across 12 months using interactive sliders for pricing and customer mix.

---

## 📂 Project Structure


