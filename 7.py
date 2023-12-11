import pandas as pd

# Creating the DataFrame
data = {
    'FamilyName': ['Shah', 'Vats', 'Vats', 'Kumar', 'Vats', 'Kumar', 'Shah', 'Shah', 'Kumar', 'Vats'],
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
    'MonthlyIncome': [44000.0, 65000.0, 43150.0, 66500.0, 255000.0, 103000.0, 55000.0, 112400.0, 81030.0, 71900.0]
}

df = pd.DataFrame(data)

# a. Calculate and display familywise gross monthly income.
familywise_gross_income = df.groupby('FamilyName')['MonthlyIncome'].sum()
print("Familywise Gross Monthly Income:\n", familywise_gross_income)
print("\n")

# b. Display the highest and lowest monthly income for each family name
highest_income = df.groupby('FamilyName')['MonthlyIncome'].max()
lowest_income = df.groupby('FamilyName')['MonthlyIncome'].min()
income_range = pd.DataFrame({'HighestIncome': highest_income, 'LowestIncome': lowest_income})
print("Monthly Income Range for Each Family Name:\n", income_range)
print("\n")

# c. Calculate and display monthly income of all members earning income less than Rs. 80000.00.
income_less_than_80000 = df[df['MonthlyIncome'] < 80000.0]
print("Monthly Income of Members Earning Less than Rs. 80000.00:\n", income_less_than_80000[['FamilyName', 'MonthlyIncome']])
print("\n")

# d. Display total number of females along with their average monthly income
female_info = df[df['Gender'] == 'Female']
total_females = female_info.shape[0]
average_income_females = female_info['MonthlyIncome'].mean()
print("Total number of females:", total_females)
print("Average Monthly Income of Females:", average_income_females)
print("\n")

# e. Delete rows with Monthly income less than the average income of all members
average_income_all_members = df['MonthlyIncome'].mean()
df_above_average_income = df[df['MonthlyIncome'] >= average_income_all_members]
print("DataFrame after deleting rows with Monthly income less than the average income of all members:\n",
      df_above_average_income)
