import matplotlib.pyplot as plt
import pandas as pd

# Read CSV and parse dates
climate_change = pd.read_csv("climate_change.csv", parse_dates=["date"])

# Set the date column as the index
climate_change.set_index("date", inplace=True)

# Create fig and ax
fig, ax = plt.subplots()

# Filter data for the 1970s
seventies = climate_change["1970-01-01":"1979-12-31"]

# Plot CO2 values
ax.plot(seventies.index, seventies["co2"])

# Show the plot
plt.show()
