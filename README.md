# 🚗 Used Car Price Prediction

This project focuses on Exploratory Data Analysis (EDA) and predictive modeling to estimate the selling price of used cars using vehicle attributes and historical sales data.

---

## 📊 Dataset Overview

The dataset (`Used_Car_Prices.csv`) consists of **8,128 records** and **5 features**:

| Column Name | Type | Description |
| :--- | :--- | :--- |
| **`brand`** | Categorical | Brand or manufacturer of the car |
| **`km_driven`** | Numerical | Total distance driven in kilometers |
| **`fuel`** | Categorical | Fuel type (e.g., Petrol, Diesel, CNG, LPG) |
| **`owner`** | Categorical | Previous ownership history (e.g., First Owner, Second Owner) |
| **`selling_price`** | Numerical | Target variable representing the sale price in INR (₹) |

---

## 🔑 Key EDA Insights

* **Missing Data:** **0 missing values** across all features[cite: 2].
* **Duplicate Records:** **1,678 duplicate rows** (~20.6% of the dataset)[cite: 2].
  * *Action:* Remove duplicates prior to train-test splitting to avoid data leakage and overoptimistic performance metrics[cite: 2].
* **Target Variable Skewness:**
  * `selling_price` displays extreme right-skewness due to high-value luxury vehicles[cite: 2].
  * Applying a $\log_{10}$ transformation converts `selling_price` into a near-normal distribution, stabilizing variance and improving linear and distance-based regression algorithms[cite: 2].
* **Outlier Analysis:**
  * `km_driven` contains extreme values (up to **2,360,457 km**)[cite: 2], indicating entry errors or extreme outliers that require filtering/capping[cite: 2].

---

## ⚙️ Data Preprocessing Workflow

1. **Deduplication:** Remove duplicate records[cite: 2].
2. **Outlier Mitigation:** Filter extreme outliers in `km_driven`[cite: 2].
3. **Target Transformation:** Transform `selling_price` using $\log_{10}(\text{selling\_price})$[cite: 2].
4. **Encoding & Feature Scaling:**
   * One-Hot Encoding for categorical features (`brand`, `fuel`, `owner`).
   * Standard scaling for numerical variables (`km_driven`).

---

## 💻 Quick Start

### Installation

Install the required Python dependencies:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn