import pandas as pd

homelessness = pd.read_csv('homelessness.csv')

print(homelessness.head())

print(homelessness.info())

print(homelessness.shape)

print(homelessness.describe())