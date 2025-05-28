# Import numpy with alias np
import numpy as np
import pandas as pd

food_consumption = pd.read_csv("food_consumption.csv")

# Subset country for USA: usa_consumption
usa_consumption = food_consumption[food_consumption["country"] == "USA"]

# Calculate mean consumption in USA
print(usa_consumption["consumption"].mean())

# Calculate median consumption in USA
print(usa_consumption["consumption"].median())
