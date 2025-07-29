import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("winemag-data-130k-v2.csv")

top_countries = df.groupby('country')['price'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_countries.plot(kind='bar',color='black')
plt.xlabel("Average points")
plt.ylabel("Country")
plt.title("Top 10 countries by average wine price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




