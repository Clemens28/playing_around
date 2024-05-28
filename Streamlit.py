import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv('likelihoods_CWR.csv')  # Replace 'your_data.csv' with the actual file path

# Create a list of unique customer IDs
customer_ids = data['Customer ID'].unique()

# Streamlit app
st.title('Customer Product Selection')

# Customer selection
selected_customer = st.selectbox('Select Customer ID', customer_ids)

# Filter data for the selected customer
filtered_data = data[data['Customer ID'] == selected_customer]

if not filtered_data.empty:
    # Display the likelihood to buy and product name
    likelihood = filtered_data['Likelihood'].iloc[0]
    product_name = filtered_data['Product ID'].iloc[0]

    st.write(f"Customer ID: {selected_customer}")
    st.write(f"Likelihood: {likelihood}")
    st.write(f"Product ID: {product_name}")
else:
    st.write("No data available for the selected customer ID.")
