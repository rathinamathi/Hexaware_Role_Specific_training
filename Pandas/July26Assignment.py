import pandas as pd

df = pd.read_csv("final_college_student_placement_dataset.csv")

# no of students in dataset
print(len(df))

# no of male and female students
print(df['Gender'].value_counts())

# average percentage in mba
print(df['MBA_Percentage'].mean())

# students who scored >80% in both ssc and hsc
print(df[(df['SSC_Percentage']>80) & (df['HSC_Percentage']>80)])

# students with prior work experience
print(df[df['Internship_Experience'].str.lower()=='yes'])

# average mba score per specialization
print(df.groupby('Specialization')['MBA_Percentage'].mean())

# count of placed vs not placed students
placement_counts = (df['Salary'] > 0).value_counts()
print(placement_counts)

# placement ratio per specialization
placement_ratio = df.groupby('Specialization')['placement_success'].value_counts(normalize=True).unstack()
print(placement_ratio)

# create placement success column

def success_lvl(row):
    if row['placement_success'] == 'Placed':
        if row['Salary'] > 950000:
            return "High"
        elif row['Salary'] <= 400000:
            return "Average"
        else:
            return "Placed"
    return "Unplaced"

df['placement_success'] = df.apply(success_lvl, axis=1)
print(df[['placement_success', 'Salary', 'placement_success']])

# degree percentage range leading to highest avg salary
placed = df[df['placement_success'] == 'Placed']
bins = [0, 60, 70, 80, 90, 100]
labels = ['0-60', '60-70', '70-80', '80-90', '90-100']
placed['Degree Range'] = pd.cut(placed['CGPA'], bins=bins, labels=labels)
avg_salary = placed.groupby('Degree Range')['Salary'].mean()
print(avg_salary.sort_values(ascending=False))


