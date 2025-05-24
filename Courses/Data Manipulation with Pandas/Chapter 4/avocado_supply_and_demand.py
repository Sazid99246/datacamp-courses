import matplotlib.pyplot as plt
import pandas as pd

avocados = pd.read_csv("avocado.csv")

# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(kind="scatter", x="nb_sold", y="avg_price",
              title="Number of avocados sold vs. average price")

# Show the plot
plt.show()
