import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

world_happiness = pd.read_csv("world_happiness.csv")

# Scatterplot of grams_sugar_per_day and happiness_score
sns.scatterplot(x='grams_sugar_per_day',
                y='happiness_score', data=world_happiness)
plt.show()

# Correlation between grams_sugar_per_day and happiness_score
cor = world_happiness['happiness_score'].corr(
    world_happiness['grams_sugar_per_day'])
print(cor)
