import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load the dataset
df = pd.read_csv('sales.csv')

# Select 10% of the rows randomly
df = df.sample(frac=0.1, random_state=42)

# Select customer features
customer_features = ['Customer_Age', 'Age_Group', 'Customer_Gender', 'Country', 'State']

# Combine customer features into a single string
df['customer_combined'] = df[customer_features].astype(str).apply(' '.join, axis=1)

# Create TF-IDF vectorizer for customer features
customer_tfidf = TfidfVectorizer()
customer_matrix = customer_tfidf.fit_transform(df['customer_combined'])

# Function to recommend products for a given customer
def recommend_products(customer_data):
    customer_vector = customer_tfidf.transform(customer_data)
    similarity_scores = linear_kernel(customer_vector, customer_matrix)
    likelihood_scores = np.where(similarity_scores > 0, 1, 0)  # Set likelihood to 1 if similarity score is greater than 0
    return likelihood_scores

# Test the recommender system on a sample customer
sample_customer_data = ['25', 'Young Adult', 'Male', 'United States', 'California']
predicted_likelihoods = recommend_products(sample_customer_data)

# Create a DataFrame to store customer likelihoods for each product
customer_likelihoods = pd.DataFrame(predicted_likelihoods, columns=df['Product'])

# Save the customer likelihoods to a CSV file
customer_likelihoods.to_csv('customer_likelihoods.csv', index=False)
