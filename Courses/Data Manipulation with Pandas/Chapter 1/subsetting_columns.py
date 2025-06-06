import pandas as pd

homelessness = pd.read_csv('homelessness.csv')

# Select the individuals column
individuals = homelessness["individuals"]

print(individuals.head())

# Select the state and family_members columns
state_fam = homelessness[["state", "family_members"]]

print(state_fam.head())

# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals", "state"]]

print(ind_state.head())
