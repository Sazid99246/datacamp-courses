import pandas as pd
import numpy as np

sales = pd.read_csv('sales_subset.csv')


def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)


print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))
