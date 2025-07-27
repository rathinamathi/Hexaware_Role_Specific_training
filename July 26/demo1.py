import pandas as pd
#print(pd.__version__)


wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")
# #shows number of records
# print(wine_reviews.shape)

# #shows top 5 records
# print(wine_reviews.head())

# #select specific colmns
# print(wine_reviews.country)

# #select specific row
# print(wine_reviews.iloc[0])
# print(wine_reviews.country.iloc[1])
# print(wine_reviews.iloc[:3,1])

# select based on label 
# 10 specifies row number 

# print(wine_reviews.loc[10,'country'])

# new_reviews = wine_reviews.loc[:,['country','points']]
# print(new_reviews)

#set index
# print(wine_reviews.set_index("winery"))

# conditional selections
# print(wine_reviews.country=='France')
# print(wine_reviews.loc[wine_reviews.country=='France'])

# summary function
# print(wine_reviews.describe())
# print(wine_reviews.country.describe())
# print(wine_reviews.points.mean())
# print(wine_reviews.country.unique())
# print(wine_reviews.country.value_counts().get("Argentina"))

# # entire first row
# print(wine_reviews.iloc[0])

# #label based filter on row country column 8th index value
# print(wine_reviews.loc[8,'country'])

#multiple column 
country_point = wine_reviews.loc[:,['title','country','points']]
# print(country_point)

print(country_point.info())


