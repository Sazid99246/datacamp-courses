import pandas as pd

sales_df = pd.read_csv("sales.csv")

print(sales_df["order_value"].mean())
print(sales_df["order_value"].sum())
