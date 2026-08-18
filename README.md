# 🚗 Revving Up Insights: Used Car Price Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)
![XGBoost](https://img.shields.io/badge/Library-XGBoost-green.svg)

## 📌 The Project Vision
Navigating the used car market can feel like guessing in the dark. Is ₹5,00,000 a fair price for a 2018 Hyundai, or are you overpaying? 

This project takes the guesswork out of car shopping by building an end-to-end Machine Learning pipeline. Using a dataset of **8,128 real-world vehicle listings**, we clean the messy data, engineer smart features, and pit powerful algorithms against each other to deliver highly accurate, data-driven price estimates in Indian Rupees (₹). 

---

## 📊 Inside the Dataset
* **Dataset File:** `Used_Car_Prices.csv`
* **Total Records:** 8,128 vehicle listings 
* **Target Goal:** Predict the `selling_price` (₹), which wildly ranges from budget-friendly ₹30,000 beaters to luxury ₹10,000,000 (1 crore) dream cars.

### What Features Are We Learning From?
| Feature Name | Type | What it tells us |
| :--- | :--- | :--- |
| `brand` | Categorical | The car manufacturer. *Example: A "Mercedes" naturally holds a higher baseline price than a "Maruti".* |
| `km_driven` | Numerical | The total distance the car has traveled. *Example: A car driven 10,000 km will generally cost more than the exact same model driven 150,000 km due to wear and tear.* |
| `fuel` | Categorical | The engine's diet (Diesel, Petrol, LPG, CNG). |
| `owner` | Categorical | The vehicle's history. *Example: A "First Owner" car is usually valued higher than a "Third Owner" car.* |
| `selling_price` | Numerical | **Our Target:** The final price tag we are trying to predict. |

---

## 🔍 Data Detective Work (Exploratory Data Analysis)
Before feeding data to a model, we have to understand its quirks. Here is what we uncovered:

1. **The Good News (No Missing Data):** Every single row had complete information. No guesswork was needed to fill in blanks!
2. **The Clones (Duplicate Records):** We uncovered **1,678 exact duplicate listings** (about 20.6% of our data). 
   * *Why we fix this:* If we leave duplicates in, our model might memorize the price of a specific car instead of learning the general market trends, leading to poor predictions on new cars.
3. **The Impossible Journeys (Anomalies):** The `km_driven` column contained extreme outliers, including a car claiming to have driven **2,360,457 km**! 
   * *Why we fix this:* A model seeing extreme outliers will skew its mathematical weights, ruining the predictions for normal, everyday cars. We successfully capped and treated these anomalies.
4. **The Wealth Gap (Target Variance):** The `selling_price` is heavily right-skewed, meaning the vast majority of cars are affordable, with a long "tail" of rare, ultra-expensive luxury vehicles.

---

## 🛠️ Under the Hood: The Machine Learning Workflow

### 1. Feature Engineering & Preprocessing
Algorithms only understand numbers, not words. We transformed our raw data through:
* **Categorical Encoding:** We mathematically translated words into numbers. 
  * *Example:* The `fuel` column is converted so that "Petrol" might become `1` and "Diesel" becomes `2`.
* **Feature Scaling:** We applied a `StandardScaler` to put large numbers (like `km_driven`) on a level playing field. 
  * *Example:* Competing scales like ₹5,00,000 (price) and 100 (horsepower) confuse algorithms. Scaling squishes them into a standard range (like -1 to 1) so the model treats them equally.

### 2. The Model Showdown
We didn't settle for just one algorithm. We trained and cross-validated an entire arsenal of models to see which learned the market best:
* **Linear Models:** Linear Regression, Ridge, Lasso (Great for simple, straight-line trends).
* **Distance & Tree-Based Models:** $k$-Nearest Neighbors (KNN), Decision Tree, Random Forest, Gradient Boosting.
* **Heavyweights:** Support Vector Regressor (SVR), XGBoost Regressor (Excellent at finding hidden, complex patterns).

---

## 📈 How Do We Know It Works? (Evaluation Metrics)
We grade our models using strict mathematical scorecards:

* **$R^2$ Score:** Tells us how much of the price variation our model understands. An $R^2$ of 0.85 means our model can explain 85% of why car prices differ!
* **Mean Absolute Error (MAE):** The easiest to understand. 
  * *Example:* If our MAE is ₹25,000, it means our model's predictions are, on average, off by only ₹25,000 from the true selling price.
* **Root Mean Squared Error (RMSE):** Similar to MAE, but heavily penalizes the model when it makes a massive, terrible prediction. 
* **Mean Absolute Percentage Error (MAPE):** Tells us our error in percentages rather than strict rupees. 

---

## 📦 Tech Stack & Blueprint
* **Language:** Python
* **Data Manipulation:** `pandas`, `numpy`
* **Visual Storytelling:** `matplotlib`, `seaborn`
* **Machine Learning Brains:** `scikit-learn`, `xgboost`
* **Model Saving:** `joblib`

---

## 🚀 Get the Engine Running

### 1. Fuel Up (Prerequisites)
Install the required tools to run the project:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost joblib
