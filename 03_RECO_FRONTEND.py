import pandas as pd
import streamlit as st

# Load the matrix DataFrame
df= pd.read_csv('transposed_pred_ma_02.csv', index_col=0)

print(df.head)

# Streamlit app
def main():
    st.title("Product Sales Recommender System")

    # Select customer_id
    customer_id = st.selectbox("Select a Customer ID", df.columns)

    # Get product_id and likelihoods for the selected customer_id
    customer_data = df[customer_id].reset_index()
    customer_data.columns = ['product_id', 'likelihood']
    sorted_data = customer_data.sort_values('likelihood', ascending=False)

    # Display the sorted table
    st.write(sorted_data)

if __name__ == '__main__':
    main()
