import pandas as pd
import numpy as np

sales = pd.read_csv('sales_subset.csv')

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index="department",
      columns="type", aggfunc="mean", fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department",
      columns="type", fill_value=0, margins=True))
