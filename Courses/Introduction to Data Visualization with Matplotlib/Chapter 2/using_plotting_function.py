import matplotlib.pyplot as plt
import pandas as pd

climate_change = pd.read_csv("climate_change.csv", parse_dates=["date"])

fig, ax = plt.subplots()


def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', colors=color)


# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index,
                climate_change['co2'], "blue", 'Time (years)', 'CO2 levels')


# Create a twin Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax2, climate_change.index,
                climate_change['relative_temp'], 'red', 'Time (years)', 'Relative temperature (Celsius)')

plt.show()
