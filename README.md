# 📊 ARPU Modeling & Segment Analysis for Verizon Wireless Pricing Strategy

## 🚀 Project Goal

Build an explainable machine learning model to predict **Average Revenue Per User (ARPU)** using plan, pricing, and customer attributes. The project aligns with Verizon's focus on **pricing analytics, revenue growth, and strategic customer segmentation**.

---

## 🧱 Data Sources

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

## 🤓 Model Leaderboard (Top Versions)

| Version | Model         | RMSE  | Notes                                |
| ------- | ------------- | ----- | ------------------------------------ |
| v1.3    | Random Forest | 47.04 | Raw + engineered features (no churn) |
| v1.4    | Random Forest | 47.40 | Added real churn feature (0/1)       |
| v1.0    | XGBoost       | 51.94 | Baseline with raw features           |

📉 **Best performer**: `v1.3 Random Forest` for accuracy + explainability.

---

## 🔍 Feature Importance (v1.4 Random Forest)

| Rank | Feature                                      | Importance       |
| ---- | -------------------------------------------- | ---------------- |
| 1    | `monthlycharges`                             | Strongest driver |
| 2    | `tenure`                                     | Loyalty signal   |
| 3    | `promo_discount`                             | Promotional lift |
| 4    | `service_type`                               | Technology type  |
| 5    | `churn`                                      | Low signal       |
| 6+   | `contract`, `loyalty_tier`, `discount_level` | Supporting roles |

> 📈 Insight: Churn was *not* a strong predictor of ARPU. Revenue is driven more by pricing and plan structure.

---

## 🛠️ Segment-Level Analysis

### Top ARPU Segments (Contract × Loyalty Tier)

* **One-year, low-discount** customers are top performers
* **Month-to-month, low-discount** surprisingly competitive
* Loyalty alone doesn't guarantee ARPU — **price discipline matters**

### Discount Erosion

* Across all contracts, **high discounts reduce ARPU**
* Most efficient ARPU achieved in **low to medium discount tiers**

### Churn vs ARPU

* No strong correlation between high-ARPU segments and churn
* **ARPU-focused modeling** is appropriate for revenue planning

---

## 💼 Deliverables

* [x] Cleaned and enriched dataset
* [x] Version-controlled models + leaderboard
* [x] Segment visualizations (ARPU + churn)
* [x] Streamlit-ready pipeline (v1.3 model)
* [x] Markdown report for GitHub

---

## 🚩 Final Recommendation: Move Forward

* **Modeling has plateaued**: Performance has stabilized across techniques
* **Random Forest v1.3** is optimal for deployment
* **Insights are robust** for pricing, promotion, and portfolio planning

### 🏆 Next Steps

* Deploy v1.3 in a Streamlit app
* Share findings on GitHub + LinkedIn
* Consider building a separate **churn classifier** if targeting retention

---

> Built by Casey Ortiz | Data Analyst & SaaS Sales Leader
> [GitHub Repo](https://github.com/) | [LinkedIn](https://linkedin.com/in/...)
