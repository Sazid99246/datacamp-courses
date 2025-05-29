# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of absences vs. final grade and Change the legend order in the scatter plot
sns.scatterplot(x="absences", y="G3", data=student_data,
                hue="location", hue_order=["Rural", "Urban"])

# Show plot
plt.show()
