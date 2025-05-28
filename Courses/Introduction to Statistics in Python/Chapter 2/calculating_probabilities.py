import pandas as pd
import numpy as np

amir_deals = pd.read_csv("amir_deals.csv")

# Count the deals for each product
counts = amir_deals['product'].value_counts()
print(counts)

# Calculate probability of picking a deal with each product
probs = counts / amir_deals['product'].count()
print(probs)