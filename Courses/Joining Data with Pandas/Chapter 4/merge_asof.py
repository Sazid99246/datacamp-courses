import pandas as pd

jpm = pd.read_csv("jpm.csv")
bac = pd.read_csv("bac.csv")
wells = pd.read_csv("wells.csv")

# Merge jpm and wells using merge_asof
jpm_wells = pd.merge_asof(jpm, wells, on='date_time',
                          suffixes=('', '_wells'), direction='nearest')

# Merge the result with bac
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time', suffixes=(
    '_jpm', '_bac'), direction='nearest')

# Compute price differences
price_diffs = jpm_wells_bac.diff()

# Plot the price differences of the close prices
price_diffs.plot(y=['close_jpm', 'close_wells', 'close_bac'])
plt.show()
