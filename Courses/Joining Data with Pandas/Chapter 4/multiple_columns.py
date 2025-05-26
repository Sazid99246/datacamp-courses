import pandas as pd

gdp = pd.read_csv("gdp.csv")
pop = pd.read_csv("pop.csv")

# Example of using merge_ordered with on and fill_method
ctry_date = pd.merge_ordered(
    gdp, pop, on=['date', 'country'], fill_method='ffill')

# Check the result
print(ctry_date)

# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(
    gdp, pop, on=['country', 'date'], fill_method='ffill')

# Print date_ctry
print(date_ctry)
