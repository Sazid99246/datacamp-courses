import pandas as pd
import numpy as np

food_consumption = pd.read_csv("food_consumption.csv")

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')[
    'co2_emission'].sum()

print(emissions_by_country)

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')[
    'co2_emission'].sum()

# Compute the first and third quartiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country < lower) | (
    emissions_by_country > upper)]
print(outliers)
