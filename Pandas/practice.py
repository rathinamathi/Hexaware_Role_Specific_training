import pandas as pd

df = pd.read_csv("winemag-data-130k-v2.csv")

# Fetching rows

# print(df.iloc[0]) # first row
# print(df.iloc[3]) # fourth row
# print(df.iloc[0:3]) # row 0 to 2 
# print(df[df['price']>30]) # fetches all the rows where price greater than 30
# print(df.iloc[-5:-1]) # fetch last row

#FETCHING COLUMNS

# print(df['country']) # fetch one column
# print(df.iloc[:,1]) # another way to fetch single column

# fetch multiple column
# print(df.iloc[:,[1,2]])
# print(df[['country','price']])


# NOTES:

# df.iloc[:,0]

# : -> select all rows (if it is before comma) or columns (if it is after comma)
# 0 -> select the first column

# to fetch second rows and all columns
# print(df.iloc[1,:])

# All rows , first and third column
# print(df.iloc[:,[0,2]])

# row 0 to 2 and column 0 to 2
# print(df.iloc[0:3,0:3])

# FILTERING DATA
# print(df[df['price']>50])

# you can use logical operators like and, or condition !!! USE PARANTHESIS AROUND EACH CONDITION
# print(df[(df['country']=='US') & (df['price']>30)])   

# print(df[(df['country']=='US') | (df['country']=='France')])

# isin operator (similar to or)
# print(df[df['country'].isin(['US','France','Italy'])])

# print(df[~(df['country']=='US')]) # NOT condition

# filter by string matching

# print(df[df['country'].str.startswith('I')])
# print(df[df['country'].notna() & df['country'].str.startswith('I')])  # if the data contains null values we use notna to skip it

# print(df[df['country'].notna() & df['country'].str.contains('ly')])
# print(df[df['variety'].notna() & (df['variety'].str.len()>5)])

# filter using between (25 and 50 both are inclusive)
# print(df[df['price'].between(25,50)]) # give all column with the row that match the condition
# print(df[df['price'].between(25, 50)]['price']) # give only the price column

# sorting data
# print(df.sort_values('country')) #Ascending
# print(df.sort_values('country')['country'])
# print(df.sort_values('country',ascending=False)['country']) #descending

# # isnull
# print(df[df['price'].isnull()])
# print(df[df['price'].isnull()][['title','price']])

# Sort by country (Z–A), then price (high to low) sort by multilple columns
# print(df.sort_values(by=['country', 'price'], ascending=[False, False])[['country','price']])

# finding duplicates in column
# print(df[df['country'].duplicated(keep=False)]) # it returns all the duplicated rows (if india is duplicated 5 times it shows all the five rows)
# print(df[df['country'].duplicated(keep='first')]) # it returns only the second and later duplicates, excluding the first
# print(df[df['country'].duplicated(keep='last')]) # returns only the earlier duplicates, excluding last

# removing duplicates (drop_duplicates())
# Remove duplicate names, keep the first
# print(df.drop_duplicates(subset='country', keep='first'))

# Keep only the last occurrence
# print(df.drop_duplicates(subset='country', keep='last'))

# Remove all duplicates completely give unique values
# print(df.drop_duplicates(subset='country', keep=False))

# # give the count of each country
# unique_names = df['country'].value_counts()
# print(unique_names)

# HANDLING MISSING VALUES

# # remove rows with any missing value
# print(df.dropna())

# # remove rows only if all values are missing
# print(df.dropna(how='all'))

# # remove rows where specific columns have missing values
# print(df.dropna(subset=['country','price']))

# detecting missing values
# print(df.isnull())
# print(df['country'].isnull())
# print(df.isnull().sum()) # count missing values in each column
# print(df.notnull())

# filling missing values
# print(df.fillna(0)) # replace all NaN with 0

# df['PriceCategory'] = pd.cut(
#     df['price'],
#     bins=[0, 20, 50, 100, 500, 1000],
#     labels=['Budget', 'Standard', 'Good', 'Premium', 'Luxury']
# )

df.to_csv('new_winemag.csv', index=False)

