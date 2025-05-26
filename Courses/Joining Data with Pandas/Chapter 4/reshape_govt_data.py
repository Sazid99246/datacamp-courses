import pandas as pd
import matplotlib.pyplot as plt

ur_wide = pd.read_csv("ur_wide.csv")

# 1. Unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars='year', var_name='month', value_name='unempl_rate')

# 2. Create a date column using the month and year columns of ur_tall
ur_tall['date'] = pd.to_datetime(ur_tall['year'].astype(str) + '-' + ur_tall['month'])

# 3. Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values('date')

# 4. Plot the unempl_rate by date
ur_sorted.plot(x='date', y='unempl_rate')
plt.show()