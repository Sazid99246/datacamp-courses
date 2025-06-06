import matplotlib.pyplot as plt
import pandas as pd

mens_rowing = pd.read_csv('mens_rowing.csv')
mens_gymnastics = pd.read_csv("mens_gymnastics.csv")

fig, ax = plt.subplots()

# Add a boxplot for the "Height" column in the DataFrames
ax.boxplot([mens_rowing["Height"], mens_gymnastics["Height"]])

# Add x-axis tick labels:
ax.set_xticklabels(["Rowing", "Gymnastics"])

# Add a y-axis label
ax.set_ylabel("Height (cm)")

plt.show()
