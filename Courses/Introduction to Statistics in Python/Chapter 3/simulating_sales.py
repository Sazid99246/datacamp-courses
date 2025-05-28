import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# Calculate new average amount
new_mean = 5000 * 1.20

# Calculate new standard deviation
new_sd = 2000 * 1.30

# Simulate 36 new sales
new_sales = norm.rvs(new_mean, new_sd, size=36)

# Create histogram and show
plt.hist(new_sales, bins=10, edgecolor='black')
plt.show()
