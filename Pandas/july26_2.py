import pandas as pd

df = pd.read_csv("final_college_student_placement_dataset.csv")

# Categorize placed students into salary bands
def salary_band(salary):
    if salary < 300000:
        return 'Low'
    elif salary <= 600000:
        return 'Medium'
    else:
        return 'High'

df['Salary_Band'] = df['Salary'].apply(salary_band)
print(df['Salary_Band'].value_counts(dropna=False))

# For each gender and specialization

placement_stats = df.groupby(['Gender', 'Specialization']).agg(
    Placement_Rate=('Placement', lambda x: (x == 'Placed').mean()),
    Avg_Salary_Placed=('Salary', lambda x: x[df.loc[x.index, 'Placement'] == 'Placed'].mean()),
    Avg_MBA=('MBA_Percentage', 'mean')
).reset_index()
print(placement_stats)

#Rows with missing values
missing_count = df.isnull().any(axis=1).sum()
print("Students with missing values:", missing_count)

# rows where salary is missing
missing_salary_rows = df[df['Salary'].isnull()]
print(missing_salary_rows)

# students with complete records
complete_records = df.dropna()
print("Complete records count:", complete_records.shape[0])

# identify duplicate student 
duplicate_rows = df[df.duplicated()]
print(duplicate_rows)

# drop duplicate records
df_dedup = df.drop_duplicates()
print("After removing duplicates:", df_dedup.shape)

# check for duplicates based on college_id
duplicate_ids = df[df.duplicated(subset='College_ID', keep=False)]
print(duplicate_ids)


# unique specializations
unique_specializations = df['Specialization'].dropna().unique()
print(unique_specializations)

# no of unique mba scores
unique_mba_scores = df['MBA_Percentage'].nunique()
print("Unique MBA scores:", unique_mba_scores)

# no of unique combinations
unique_combinations = df[['Gender', 'Specialization', 'Placement']].drop_duplicates().shape[0]
print("Unique combinations:", unique_combinations)

# avg salary of placed students
avg_salary_placed = df[df['Placement'] == 'Placed']['Salary'].mean()
print("Average salary of placed students:", avg_salary_placed)

# max and min cgpa

max_cgpa = df['CGPA'].max()
min_cgpa = df['CGPA'].min()
print("Max CGPA:", max_cgpa)
print("Min CGPA:", min_cgpa)

# total no of placed and unplaced
placement_counts = df['Placement'].value_counts()
print(placement_counts)

# avg of each specialization
specialization_stats = df.groupby('Specialization').agg(
    Avg_SSC=('SSC_Percentage', 'mean'),
    Avg_MBA=('MBA_Percentage', 'mean'),
    Placement_Count=('Placement', lambda x: (x == 'Placed').sum())
).reset_index()
print(specialization_stats)

#summary table
summary = pd.DataFrame({
    'Column': df.columns,
    'Null_Count': df.isnull().sum().values,
    'Unique_Values': df.nunique().values,
    'Duplicated_Values': [df[col].duplicated().sum() if df[col].duplicated().any() else 0 for col in df.columns]
})
print(summary)
