import pandas as pd
import numpy as np

# Assuming df01 is your matrix-like DataFrame
df01=pd.read_csv('predictions_matrix.csv')

df02 = df01.copy()  # Create a copy of the original DataFrame

# Get the axis values (row and column names)
rows = df02.index
columns = df02.columns

# Generate random values for the non-axis cells
random_values = np.random.rand(len(rows), len(columns))

# Update the non-axis values in the copied DataFrame with the random values
df02.iloc[:, :] = random_values

# Assign the axis values back to the copied DataFrame
df02.index = rows
df02.columns = columns

df02.to_csv('predictions_matrix_02.csv')

import pandas as pd
import streamlit as st

# Load the matrix DataFrame
df_matrix = pd.read_csv('predictions_matrix_03.csv', index_col='user_id')

# Transponieren des DataFrame
df_matrix_transposed = df_matrix.transpose()

df_matrix_transposed.to_csv('transposed_pred_ma.csv')

# Ausgabe des transponierten DataFrames
print(df_matrix_transposed)