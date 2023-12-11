import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset from seaborn
titanic = sns.load_dataset('titanic')

# a. Clean the data by dropping the column which has the largest number of missing values.
column_with_max_missing_values = titanic.isnull().sum().idxmax()
titanic_cleaned = titanic.drop(column_with_max_missing_values, axis=1)

# Display the cleaned DataFrame
print("Cleaned Titanic Data:")
print(titanic_cleaned.head())
print("\n")

# b. Find total number of passengers with age more than 30
passengers_age_above_30 = titanic_cleaned[titanic_cleaned['age'] > 30]
total_passengers_age_above_30 = len(passengers_age_above_30)
print("Total number of passengers with age more than 30:", total_passengers_age_above_30)
print("\n")

# c. Find total fare paid by passengers of the second class
total_fare_second_class = titanic_cleaned.loc[titanic_cleaned['class'] == 'Second', 'fare'].sum()
print("Total fare paid by passengers of the second class:", total_fare_second_class)
print("\n")

# d. Compare the number of survivors of each passenger class
survivors_by_class = titanic_cleaned.groupby('class')['survived'].sum()
print("Number of survivors by passenger class:")
print(survivors_by_class)
print("\n")

# e. Compute descriptive statistics for the age attribute gender-wise
age_statistics_gender_wise = titanic_cleaned.groupby('sex')['age'].describe()
print("Descriptive statistics for age attribute gender-wise:")
print(age_statistics_gender_wise)
print("\n")

# f. Draw a scatter plot for passenger fare paid by Female and Male passengers separately
plt.figure(figsize=(10, 6))
sns.scatterplot(x='fare', y='sex', data=titanic_cleaned)
plt.title('Scatter Plot: Passenger Fare by Gender')
plt.xlabel('Fare')
plt.ylabel('Gender')
plt.show()

# g. Compare density distribution for features age and passenger fare
plt.figure(figsize=(12, 6))
sns.kdeplot(data=titanic_cleaned, x='age', label='Age', fill=True)
sns.kdeplot(data=titanic_cleaned, x='fare', label='Fare', fill=True)
plt.title('Density Distribution Comparison: Age vs Fare')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()

# h. Draw the pie chart for three groups labelled as class 1, class 2, class 3
class_counts = titanic_cleaned['class'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%', colors=['skyblue', 'lightcoral', 'lightgreen'])
plt.title('Distribution of Passenger Classes')
plt.show()

# i. Find % of survived passengers for each class
survival_percentage_by_class = titanic_cleaned.groupby('class')['survived'].mean() * 100
print("Survival percentage for each class:")
print(survival_percentage_by_class)
print("\n")

# Answer the question: "Did class play a role in survival?"
# Display a conclusion based on the survival percentages
if survival_percentage_by_class['First'] > survival_percentage_by_class['Second'] > survival_percentage_by_class['Third']:
    print("Yes, class played a role in survival. Passengers in the first class had a higher survival rate.")
else:
    print("No clear evidence that class played a significant role in survival.")
