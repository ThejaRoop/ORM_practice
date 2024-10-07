import pandas as pd

# Assuming your CSV file is named 'data.csv'
df = pd.read_csv('iris.csv')

# Inspect the DataFrame
# print(df.head())  # Display the first few rows
# print(df.info())  # Get information about data types and missing values

df['petal.width'] = pd.to_numeric(df['petal.width'], errors='coerce').fillna(df['petal.width'].mean())
df['sepal.width'] = pd.to_numeric(df['sepal.width'], errors='coerce')
# print(df[df['petal.width'].isnull()])

# Optionally, fill NaN values with a specific value (like the mean or mode of the column)
df['petal.width'] = df['petal.width'].fillna(df['petal.width'].mean())
df['sepal.width'] = df['sepal.width'].fillna(df['sepal.width'].mean())


df['date'] = pd.to_datetime(df['date'], format='%m/%d/%y')

df['petal.width'] = df['petal.width'].round(0).astype(int)

# df['combined_sum'] = df['sepal.width'] + df['petal.length'] + df['petal.width']
df.dropna(inplace=True)


missingval = df.isnull().sum()
# print(missingval)

df['sepal.length'] = df['sepal.length'].round(2)
df['sepal.width'] = df['sepal.width'].round(2)
df['petal.width'] = df['petal.width'].round(2)

# Renaming the column
df.rename(columns={'sepal.length': 'sepal_length'}, inplace=True)
df.rename(columns={'sepal.width': 'sepal_width'}, inplace=True)
df.rename(columns={'petal.length': 'petal_length'}, inplace=True)
df.rename(columns={'petal.width': 'petal_width'}, inplace=True)
# print(df.dtypes)
print(df.isnull().sum())

# df.to_csv('output.csv', index=False)

cleaneddf = df

print(cleaneddf)

# sepal.length
# sepal.width 
# petal.length
# variety
# # Check for missing values
# print(df.isnull().sum())



# # Explore data types
# print(df)

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

