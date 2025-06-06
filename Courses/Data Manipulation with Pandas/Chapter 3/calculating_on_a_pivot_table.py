import pandas as pd

temperatures = pd.read_csv("temperatures.csv")

temperatures["year"] = pd.to_datetime(temperatures["date"]).dt.year

temp_by_country_city_vs_year = temperatures.pivot_table(
    values="avg_temp_c", index=["country", "city"], columns="year")

# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis=1)

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])
