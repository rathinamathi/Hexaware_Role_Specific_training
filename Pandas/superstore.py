import pandas as pd

df = pd.read_csv("Superstore.csv")

# # no of rows and columns
# print(df.shape)

# # column names and their data types
# print(df.dtypes)

# # clean column names . Replace with underscore
df.columns = df.columns.str.strip().str.replace(" ","_").str.replace("/","_")
# print(df.dtypes)

# convert data types
df['Order_Date'] = pd.to_datetime(df['Order_Date'], dayfirst=True)
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'], dayfirst=True)

# group by region and category
grouped = df.groupby(['Region', 'Category']).agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Discount': 'mean'
}).reset_index()
print(grouped)

# region + category highest profit
max_profit = grouped.loc[grouped['Profit'].idxmax()]
print(max_profit)

# top 5 most profitable products
top_products = df.groupby('Product_Name')['Profit'].sum().sort_values(ascending=False).head(5)
print("Top 5 Most Profitable Products:")
print(top_products)

# extract month and year from Order_Date
df['Order_Month'] = df['Order_Date'].dt.to_period('M')

# Group by Order_Month and sum Sales
monthly_sales = df.groupby('Order_Month')['Sales'].sum().reset_index()

print("Monthly Sales Trend:")
print(monthly_sales)

# Create Order_Value column
df['Order_Value'] = df['Sales'] / df['Quantity']

# Group by City and calculate average Order_Value
city_order_value = df.groupby('City')['Order_Value'].mean().sort_values(ascending=False).head(10)

print("Top 10 cities by average order value:")
print(city_order_value)


# filter where Profit < 0
loss_orders = df[df['Profit'] < 0]
# loss_orders.to_csv("loss_orders.csv", index=False)

# detect null values and impute

print("missing values:")
print(df.isnull().sum())

if 'Price' in df.columns:
    df['Price'] = df['Price'].fillna(1)
    print("missing values filled with 1")
else:
    print("Column not exist")
