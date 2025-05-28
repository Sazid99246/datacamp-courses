import matplotlib.pyplot as plt
import pandas as pd

mens_rowing = pd.read_csv('mens_rowing.csv')
mens_gymnastics = pd.read_csv("mens_gymnastics.csv")
fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing["Weight"], label="Rowing", alpha=0.7)

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics["Weight"], label="Gymnastics", alpha=0.7)

# Set the x-axis label to "Weight (kg)"
ax.set_xlabel("Weight (kg)")

# Set the y-axis label to "# of observations"
ax.set_ylabel("# of observations")

# Add a legend to differentiate the histograms
ax.legend()

plt.show()
