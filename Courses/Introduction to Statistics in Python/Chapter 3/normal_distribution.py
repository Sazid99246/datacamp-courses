import pandas as pd
from scipy.stats import norm

amir_deals = pd.read_csv("amir_deals.csv")

# Probability of deal < 7500
prob_less_7500 = norm.cdf(7500, 5000, 2000)

print(prob_less_7500)

# Use the CDF to find the probability of a deal being less than or equal to $1000
prob_less_than_1000 = norm.cdf(1000, 5000, 2000)

# Subtract from 1 to find the probability of a deal being more than $1000
prob_over_1000 = 1 - prob_less_than_1000

print(prob_over_1000)

# Probability of deal between 3000 and 7000
prob_3000_to_7000 = norm.cdf(7000, 5000, 2000) - norm.cdf(3000, 5000, 2000)
print(prob_3000_to_7000)

# Calculate amount that 25% of deals will be less than
pct_25 = norm.ppf(0.25, 5000, 2000)
print(pct_25)