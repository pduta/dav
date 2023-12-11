import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris data directly from seaborn
iris = sns.load_dataset('iris')
df = iris.copy()

# a. Display data types information
print("Data Info:")
print(df.info())
print("\n")

# b. Find the number of missing values in each column
missing_values = df.isnull().sum()
print("Number of Missing Values in Each Column:\n", missing_values)
print("\n")

# c. Plot bar chart to show the frequency of each class label in the data.
plt.figure(figsize=(8, 5))
sns.countplot(x='species', data=df)
plt.title('Frequency of Each Class Label')
plt.xlabel('Class Label')
plt.ylabel('Count')
plt.show()

# d. Draw a scatter plot for Petal Length vs Sepal Length and fit a regression line
plt.figure(figsize=(8, 5))
sns.regplot(x='sepal_length', y='petal_length', data=df)
plt.title('Scatter Plot: Petal Length vs Sepal Length with Regression Line')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.show()

# e. Plot density distribution for feature Petal width.
plt.figure(figsize=(8, 5))
sns.kdeplot(df['petal_width'], shade=True)
plt.title('Density Distribution of Petal Width')
plt.xlabel('Petal Width')
plt.ylabel('Density')
plt.show()

# f. Use a pair plot to show pairwise bivariate distribution in the Iris Dataset.
plt.figure(figsize=(12, 8))
sns.pairplot(df, hue='species')
plt.suptitle('Pair Plot of Iris Dataset', y=1.02)
plt.show()

# g. Draw heatmap for any two numeric attributes
numeric_attributes = df.select_dtypes(include=['float64'])
plt.figure(figsize=(8, 5))
sns.heatmap(numeric_attributes.corr(), annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Heatmap for Numeric Attributes')
plt.show()

# h. Compute mean, mode, median, standard deviation for each numeric feature
numeric_summary = df.describe().transpose()
numeric_summary['mode'] = df.mode().transpose().iloc[:, 0]

print("Summary Statistics for Numeric Features:\n", numeric_summary)
print("\n")

# i. Compute correlation coefficients between each pair of features and plot heatmap
correlation_matrix = df.corr()
plt.figure(figsize=(8, 5))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Coefficients Heatmap')
plt.show()
