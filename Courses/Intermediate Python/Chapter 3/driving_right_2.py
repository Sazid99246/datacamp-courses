import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)
sel = cars[cars['drives_right']]

print(sel)
