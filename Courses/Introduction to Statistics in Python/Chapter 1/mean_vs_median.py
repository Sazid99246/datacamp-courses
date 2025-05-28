import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

food_consumption = pd.read_csv("food_consumption.csv")

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption["food_category"] == "rice"]

# Histogram of co2_emission for rice and show plot
rice_consumption['co2_emission'].hist()
plt.show()

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption['co2_emission'].agg(['mean', 'median']))
