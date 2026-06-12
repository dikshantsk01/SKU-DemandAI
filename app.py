import streamlit as st
import pandas as pd
import joblib

# 1. Load the AI Model (Cached so it only loads once)
@st.cache_resource
def load_model():
    # Make sure this matches the exact filename in your GitHub repo
    return joblib.load('SKU_Demand_Estimator_v1.pkl')

model = load_model()

# 2. The Header
st.set_page_config(page_title="Retail Demand AI", layout="centered")
st.title("📊 SKU Demand Estimator AI")
st.write("Enter the product details below to predict future sales volume.")
st.markdown("---")

# 3. User Inputs
col1, col2 = st.columns(2)

with col1:
    item_mrp = st.number_input("Product Price (MRP)", min_value=30.0, max_value=300.0, value=150.0)
    item_weight = st.number_input("Product Weight", min_value=5.0, max_value=25.0, value=12.0)

with col2:
    outlet_year = st.slider("Store Opening Year", 1985, 2010, 1999)
    item_visibility = st.slider("Shelf Visibility %", 0.0, 0.2, 0.05)

st.markdown("---")

# 4. The Prediction Button & Logic
if st.button("🚀 Predict Sales Demand"):
    
    # Package the UI inputs into a DataFrame
    # CRITICAL: These column names must exactly match the ones used during XGBoost training!
    input_data = pd.DataFrame({
        'Item_MRP': [item_mrp],
        'Item_Weight': [item_weight],
        'Outlet_Establishment_Year': [outlet_year], 
        'Item_Visibility': [item_visibility]
    })
    
    try:
        # Feed the data to the model
        prediction = model.predict(input_data)
        
        # Display the result beautifully
        st.success(f"Estimated Sales Volume: {prediction[0]:.2f} units")
        st.balloons()
        
    except Exception as e:
        # If there is a column name mismatch, this will catch the error
        st.error(f"Error making prediction: {e}")
        st.warning("Hint: Verify that the column names in your DataFrame match your Jupyter notebook training data exactly.")
