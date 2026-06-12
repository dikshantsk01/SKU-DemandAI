import streamlit as st
import pandas as pd

# 1. The Header
st.set_page_config(page_title="Retail Demand AI", layout="centered")
st.title("📊 SKU Demand Estimator AI")
st.write("Enter the product details below to predict future sales volume.")
st.markdown("---")

# 2. User Inputs
col1, col2 = st.columns(2)

with col1:
    item_mrp = st.number_input("Product Price (MRP)", min_value=30.0, max_value=300.0, value=150.0)
    item_weight = st.number_input("Product Weight", min_value=5.0, max_value=25.0, value=12.0)

with col2:
    outlet_year = st.slider("Store Opening Year", 1985, 2010, 1999)
    item_visibility = st.slider("Shelf Visibility %", 0.0, 0.2, 0.05)

st.markdown("---")

# 3. The Prediction Button
if st.button("🚀 Predict Sales Demand"):
    st.success(f"System is ready to predict for a product priced at ${item_mrp}!")
    st.info("Next step: We will wire up the AI brain to give us the real number.")
