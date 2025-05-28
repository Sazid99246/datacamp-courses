import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import uniform

amir_deals = pd.read_csv("amir_deals.csv")

# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Define the uniform distribution
wait_time_dist = uniform(min_time, max_time - min_time)

# Calculate probability of waiting less than 5 mins
prob_less_than_5 = wait_time_dist.cdf(5)
print(prob_less_than_5)

# Calculate probability of waiting more than 5 mins
prob_greater_than_5 = 1 - wait_time_dist.cdf(5)
print(prob_greater_than_5)