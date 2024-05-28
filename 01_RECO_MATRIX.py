import pandas as pd

df01 = pd.read_csv('filtered_ecommerce_data.csv')

## Drop Products
# Assuming df01 is your original DataFrame
# Count the occurrences of each product_id
product_counts = df01['product_id'].value_counts()

# Get the product_ids that appear more than 50 times
product_ids = product_counts[product_counts > 50].index

# Filter the rows in df01 based on the selected product_ids
df02 = df01[df01['product_id'].isin(product_ids)].copy()

# Reset the index of df02
df02.reset_index(drop=True, inplace=True)


## Drop Customers
user_counts = df02['user_id'].value_counts()

# Get the product_ids that appear more than 50 times
user_ids = user_counts[user_counts > 5].index

# Filter the rows in df01 based on the selected product_ids
df03 = df02[df02['user_id'].isin(user_ids)].copy()

# Reset the index of df02
df03.reset_index(drop=True, inplace=True)

# Create a dictionary to store the matrix matrix = {}

matrix= {}

for index, row in df03.iterrows():
    product_id = row['product_id']
    user_id = row['user_id']
    if product_id not in matrix:
        matrix[product_id] = {}
    matrix[product_id][user_id] = 1

# Convert the dictionary to a DataFrame
matrix_df = pd.DataFrame.from_dict(matrix, orient='index', columns=df02['user_id'].unique()).fillna(0)

print(matrix_df)

# Saving Matrix
matrix_df.to_csv('initial_matrix.csv')
