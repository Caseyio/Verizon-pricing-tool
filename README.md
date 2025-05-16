# 🚀 ARPU Modeling & Segment Analysis for Verizon Wireless Pricing Strategy

## 🧠 Project Goal

Build an explainable machine learning model to predict **Average Revenue Per User (ARPU)** using plan, pricing, and customer attributes. The project aligns with Verizon's focus on **pricing analytics, revenue growth, and strategic customer segmentation**.

---

## 💾 Data Sources

| Dataset       | Description                        |
| ------------- | ---------------------------------- |
| `telco_churn` | Customer-level plan + churn data   |
| `fcc_2024`    | Broadband plan-level pricing (FCC) |
| `fcc_2025`    | Broadband plan-level pricing (FCC) |

Data was merged and enriched using normalized `service_type` to append external monthly and total charges.

---

## 🧪 Feature Engineering

* **ARPU** calculated using enriched FCC pricing
* Derived Features:

  * `loyalty_tier` from `tenure`
  * `discount_level` from `promo_discount`
  * Encoded `contract`, `churn`, and `service_type`
* Merged and validated for modeling

---

## 📈 Final Model Leaderboard

| Version | Model         | RMSE   | Notes                                       |
|---------|---------------|--------|---------------------------------------------|
| v1.0c   | XGBoost       | **9.25**  | ✅ Final model — clean, full, non-leaky       |
| v1.3c   | Random Forest | 9.59   | Final clean RF, all service types included  |
| v1.3    | Random Forest | 10.64  | Clean model, missing service_type_none      |
| v1.4    | Random Forest | 47.40  | Churn feature tested                        |
| v1.0    | XGBoost       | 51.94  | Baseline with raw features                  |
| v1.2    | XGBoost       | 52.01  | With churn added                            |
| v1.1    | XGBoost       | 53.23  | Minor feature expansion                     |

> 🏆 **v1.0c XGBoost** is the most accurate and production-ready model.

---

## 📱 Streamlit App Design

The app is designed around 3 intuitive tabs to support real-time pricing analysis and strategic scenario planning.

### 1️⃣ Efficiency View
- Explore ARPU by service type, contract, and discount tier
- Identify inefficient segments with high discount + low return
- Visualize ARPU vs. promo erosion and plan mix

### 2️⃣ Mix Simulator
- Adjust sliders for:
  - Segment mix (contract types, loyalty tiers)
  - Discount levels
- Instantly view the projected ARPU impact
- Simulate margin lift from mix optimization

### 3️⃣ Annual Price Planner
- Project ARPU over time
- Customize churn assumptions, retention effort, or plan growth
- Monthly forecast visualization with annual performance indicators

---

## 📊 Feature Importance — v1.0c (XGBoost)

| Rank | Feature             | Insight                                 |
|------|---------------------|-----------------------------------------|
| 1    | `service_type_none` | Major negative predictor of ARPU       |
| 2    | `service_type_fiber`| High revenue customer cluster           |
| 3    | `tenure`            | Loyalty impact on recurring revenue     |
| 4    | `contract_One year` | Higher ARPU stability vs monthly plans  |
| 5    | `discount_level_Medium` | Balanced promotions = better retention |
| 6    | `loyalty_tier_Very Loyal` | Long-term plans retain higher ARPU     |
| ...  | Other features      | Provide marginal predictive lift        |

> 📌 Key Takeaway: Most revenue lift comes from **getting customers onto a plan**, not necessarily from retention or plan upsell alone.

---

## 🧬 Segment-Level Analysis

### Top ARPU Segments (Contract × Discount Level)

* **One-year, low-discount** customers continue to deliver the highest ARPU
* **Month-to-month, low-discount** customers are more profitable than expected
* Loyalty adds value, but **contract type + discount level are stronger predictors**

### Discount Impact

* **High-discount plans consistently reduce ARPU** across all contract types
* Optimal pricing performance is seen in **low to medium discount segments**
* Strategic discount targeting can drive meaningful revenue lift

### Service Type Dynamics

* Customers with **no internet service** (`service_type_none`) significantly reduce ARPU — the model flags this as the top negative driver
* **Fiber customers** are associated with the highest ARPU performance
* DSL remains mid-tier with stable, lower-range returns

### Churn vs ARPU

* After testing, **churn had little predictive value for ARPU**
* Including churn slightly degraded model accuracy
* **ARPU modeling is best used for proactive price and product planning**, not retention analysis

---

## 💼 Deliverables

* [x] Cleaned and enriched dataset (FCC + internal data)
* [x] Fully version-controlled model pipeline + leaderboard
* [x] Feature importance + segment-level analysis
* [x] Streamlit-ready app interface with 3-tab design
* [x] Final markdown summary + GitHub documentation

---

## 🚩 Final Recommendation: Move Forward

* ✅ **Model performance is excellent** — we’ve plateaued near optimal accuracy (RMSE = 9.25)
* ✅ **v1.0c XGBoost** is the final production model with full segment coverage
* ✅ **Insights are solid**: price discipline, contract strategy, and customer mix all impact ARPU
* ✅ Data is clean, non-leaky, and Streamlit-ready

### 🏆 Next Steps

* Deploy the **v1.0c model** to the Streamlit dashboard
* Publish the project on **GitHub + LinkedIn** to showcase business impact
* Optionally build a **separate churn classifier** for retention-specific insights

---

> Built by Casey Ortiz | Data Analyst & Ops Strategy Leader
> [GitHub Repo](https://github.com/caeyio) | [LinkedIn](https://linkedin.com/in/kco1)
