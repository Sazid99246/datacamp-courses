import matplotlib.pyplot as plt
import pandas as pd

# Read CSV and parse dates
climate_change = pd.read_csv("climate_change.csv", parse_dates=["date"])

# Set the date column as the index
climate_change.set_index("date", inplace=True)

# Initalize a Figure and Axes
fig, ax  = plt.subplots()

# Plot the CO2 variable in blue
ax.plot(climate_change.index, climate_change['co2'], color='b')

# Create a twin Axes that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature in red
ax2.plot(climate_change.index, climate_change["relative_temp"], color='red')

plt.show()