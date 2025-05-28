import pandas as pd
import matplotlib.pyplot as plt

amir_deals = pd.read_csv("amir_deals.csv")

# Histogram of amount with 10 bins and show plot
amir_deals['amount'].hist(bins=10)
plt.show()