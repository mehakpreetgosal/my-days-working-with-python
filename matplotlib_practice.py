print("Data Visualization with Matplotlib")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = np.array([1, 2, 5, 7, 8, 11, 13, 16, 17, 23])
y = np.array([37, 44, 52, 63, 65, 70, 75, 76, 80, 90])
#plt.plot(x,y, color="blue", marker="x", linestyle="--")
#plt.title("Line Graph")

colors = ["red", "blue", "green", "orange", "purple", "cyan", "magenta", "yellow", "black", "brown"]
sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
plt.scatter(x,y, c=colors, marker="o", s=sizes, alpha=0.5, cmap = "viridis")
plt.colorbar()
plt.show()
