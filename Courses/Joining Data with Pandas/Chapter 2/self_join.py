import pandas as pd

crews = pd.read_csv("crews.csv")

# Merge the crews table to itself
crews_self_merged = crews.merge(
    crews, on="id", how="inner", suffixes=["_dir", "_crew"])

# Create a Boolean index to select the appropriate
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') & 
     (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())