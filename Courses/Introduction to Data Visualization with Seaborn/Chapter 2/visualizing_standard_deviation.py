# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg", data=mpg, kind="line", ci="sd")

# Show plot
plt.show()
