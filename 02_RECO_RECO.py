import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD

# Load the initial matrix DataFrame
initial_matrix = pd.read_csv('initial_matrix.csv')
index = initial_matrix.index  # Save the index

# Apply Singular Value Decomposition (SVD) to the initial matrix
svd = TruncatedSVD(n_components=10)
matrix_factors = svd.fit_transform(initial_matrix)

# Reconstruct the matrix using the matrix factors
reconstructed_matrix = svd.inverse_transform(matrix_factors)

# Normalize the reconstructed matrix to ensure values are between 0 and 1
normalized_matrix = (reconstructed_matrix - reconstructed_matrix.min()) / (
    reconstructed_matrix.max() - reconstructed_matrix.min()
)

# Create the predictions matrix DataFrame
predictions_matrix = pd.DataFrame(normalized_matrix, index=index, columns=initial_matrix.columns)

# Save the predictions matrix to a CSV file
predictions_matrix.to_csv('predictions_matrix.csv', index=False)

