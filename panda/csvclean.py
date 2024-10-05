import pandas as pd

# Assuming your CSV file is named 'data.csv'
df = pd.read_csv('iris.csv')

# Inspect the DataFrame
print(df.head())  # Display the first few rows
print(df.info())  # Get information about data types and missing values

# Check for missing values
print(df.isnull().sum())



df.dropna(inplace=True)

# Explore data types
print(df)

# import pandas as pd
# import numpy as np

# Assuming you have a DataFrame 'df'

# # Handle missing values:
# df.fillna(value={'column_name': 'missing'}, inplace=True)  # Fill missing values with a specific value

# # Convert data types:
# df['column_name'] = df['column_name'].astype(float)  # Convert to numeric

# # Map values:
# mapping = {'old_value1': 'new_value1', 'old_value2': 'new_value2'}
# df['column_name'] = df['column_name'].map(mapping)

# # Create derived columns:
# df['new_column'] = df['column1'] + df['column2']

# # Remove outliers (e.g., using IQR method):
# Q1 = df['column_name'].quantile(0.25)
# Q3 = df['column_name'].quantile(0.75)
# IQR = Q3 - Q1
# df = df[(df['column_name'] >= Q1 - 1.5 * IQR) & (df['column_name'] <= Q3 + 1.5 * IQR)]