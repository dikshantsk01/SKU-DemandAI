# SKU Demand Estimator AI 📊
**End-to-End Retail Forecasting Pipeline**

## The Mission
Retail companies lose millions of dollars either overstocking products that don't sell, or running out of products that do. This project is an AI-driven machine learning pipeline built to predict exact SKU-level sales across multiple store locations, replacing human guesswork with hard data.

## 🛠️ Tech Stack & Architecture
* **Language:** Python 3.x
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn, XGBoost Regressor
* **Model Optimization:** RandomizedSearchCV

## 🧠 Core Pipeline Phases
1. **Data Ingestion:** Automated loading of multi-store historical sales data.
2. **Smart Imputation:** Dynamically handles missing numerical weights (mean) and categorical store sizes (mode mapping).
3. **Feature Engineering:** Converts text-based categorical data into machine-readable numerical formats using Label Encoding.
4. **Model Tuning:** Applies hyperparameter constraints (`max_depth`, `learning_rate`, `n_estimators`) to prevent overfitting, stabilizing the model for real-world unseen data.

## 📈 Model Performance & Results
By transitioning from a baseline XGBoost model to a hyperparameter-tuned architecture using RandomizedSearchCV, the pipeline successfully eliminated overfitting, resulting in a highly stable model ready for production deployment.

* **Final R-Squared (Testing Data):** 0.5852
* **Final R-Squared (Training Data):** 0.6353
* **Business Impact:** Reduced the train/test performance gap to ~5%, ensuring reliable, consistent predictions when exposed to completely new, unseen inventory data.

## 🚀 Deployment Status
* The optimized AI model is compiled and exported as `SKU_Demand_Estimator_v1.pkl`.
* Ready for integration into a web-based inference dashboard.
* How to Run Locally:

Clone this repository: git clone https://github.com/dikshantsk01/SKU-DemandAI.git
Install requirements: pip install -r requirements.txt
Launch the dashboard: streamlit run app.py

---
*Developed by Dikshant Khobragade*


