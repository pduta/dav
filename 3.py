import pandas as pd
import numpy as np

# Create a DataFrame with 3 columns and 50 rows of random numeric data
np.random.seed(42)
data = np.random.rand(50, 3)
columns = ['Column1', 'Column2', 'Column3']
df = pd.DataFrame(data, columns=columns)

# Replace 10% of the values with null values
null_indices = np.random.choice(df.size, size=int(0.1 * df.size), replace=False)
df.values.ravel()[null_indices] = np.nan

# a. Identify and count missing values in a DataFrame
missing_values_count = df.isnull().sum().sum()
print("Missing Values Count:\n", df.isnull().sum(), "\nTotal Missing Values:", missing_values_count)
print("\n")

# b. Drop the column having more than 5 null values
df_dropped_column = df.dropna(axis=1, thresh=df.shape[0] - 5)
print("DataFrame after dropping columns with more than 5 null values:\n", df_dropped_column)
print("\n")

# c. Identify the row label having the maximum sum of all values in a row and drop that row
max_sum_row_label = df.sum(axis=1).idxmax()
df_dropped_row = df.drop(index=max_sum_row_label)
print("DataFrame after dropping the row with the maximum sum:\n", df_dropped_row)
print("\n")

# d. Sort the DataFrame based on the first column
df_sorted = df.sort_values(by='Column1')
print("DataFrame sorted on the basis of the first column:\n", df_sorted)
print("\n")

# e. Remove all duplicates from the first column
df_no_duplicates = df.drop_duplicates(subset='Column1')
print("DataFrame after removing duplicates from the first column:\n", df_no_duplicates)
print("\n")

# f. Find the correlation between the first and second column and covariance between the second and third column
correlation_col1_col2 = df['Column1'].corr(df['Column2'])
covariance_col2_col3 = df['Column2'].cov(df['Column3'])
print("Correlation between Column1 and Column2:", correlation_col1_col2)
print("Covariance between Column2 and Column3:", covariance_col2_col3)
print("\n")

# g. Discretize the second column and create 5 bins
df['Column2_bins'] = pd.cut(df['Column2'], bins=5)
print("DataFrame after discretizing the second column into 5 bins:\n", df)
