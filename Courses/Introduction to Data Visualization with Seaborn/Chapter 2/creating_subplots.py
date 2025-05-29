import seaborn as sns
import matplotlib.pyplot as plt

# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", data=student_data,
            kind="scatter", col="study_time")

# Change to make subplots based on study time
sns.relplot(x="absences", y="G3", data=student_data,
            kind="scatter", col="study_time")

# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", data=student_data,
            kind="scatter", row="study_time")

# Show plot
plt.show()
