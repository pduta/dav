import pandas as pd

# Assuming you have two Excel files named 'workshop1.xlsx' and 'workshop2.xlsx'
# with sheets named 'Sheet1' containing the fields 'Name', 'Date', and 'Duration'

# a. Import data into two data frames
df_workshop1 = pd.read_excel('workshop1.xlsx', sheet_name='Sheet1')
df_workshop2 = pd.read_excel('workshop2.xlsx', sheet_name='Sheet1')

# b. Perform merging to find names of students who attended both workshops
df_both_workshops = pd.merge(df_workshop1, df_workshop2, on=['Name', 'Date', 'Duration'])
names_both_workshops = df_both_workshops['Name'].unique()
print("Names of students who attended both workshops:\n", names_both_workshops)
print("\n")

# c. Find names of all students who attended a single workshop only
df_single_workshop = pd.concat([df_workshop1, df_workshop2]).drop_duplicates(keep=False)
names_single_workshop = df_single_workshop['Name'].unique()
print("Names of students who attended a single workshop only:\n", names_single_workshop)
print("\n")

# d. Merge two data frames row-wise and find the total number of records
df_combined = pd.concat([df_workshop1, df_workshop2], ignore_index=True)
total_records = len(df_combined)
print("Total number of records in the combined data frame:", total_records)
print("\n")

# e. Merge two data frames row-wise and use two columns as multi-row indexes
df_combined_multi_index = pd.concat([df_workshop1, df_workshop2], keys=['Workshop1', 'Workshop2'])
print("Combined data frame with multi-row indexes:\n", df_combined_multi_index)
print("\n")

# f. Generate descriptive statistics for the hierarchical data frame
stats = df_combined_multi_index.groupby(['Name', 'Date']).describe()
print("Descriptive statistics for the hierarchical data frame:\n", stats)
