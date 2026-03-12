import pandas as pd

# Load dataset
data = pd.read_csv("sales_data.csv")

# Calculate revenue column
data["revenue"] = data["units_sold"] * data["price"]

# Calculate total revenue
total_revenue = data["revenue"].sum()

# Revenue grouped by product
revenue_by_product = data.groupby("product")["revenue"].sum()

print("Total Revenue:", total_revenue)
print("\nRevenue by Product:")
print(revenue_by_product)
