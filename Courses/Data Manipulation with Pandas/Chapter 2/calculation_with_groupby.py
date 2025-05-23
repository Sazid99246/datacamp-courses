import pandas as pd
import numpy as np

sales = pd.read_csv('sales_subset.csv')

# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])[
    "weekly_sales"].sum()
print(sales_by_type_is_holiday)
