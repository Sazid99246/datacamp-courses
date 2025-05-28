import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

food_consumption = pd.read_csv("food_consumption.csv")

# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], [0, 0.25, 0.5, 0.75, 1]))

# Calculate the quintiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], [
      0, 0.2, 0.4, 0.6, 0.8, 1]))

# Calculate the deciles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 11)))
