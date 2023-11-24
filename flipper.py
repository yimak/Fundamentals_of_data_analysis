import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#calculate Flipper length
data = pd.read_csv('penguins.csv')
flipper_length_values = data['flipper_length_mm']
x, counts = np.unique(flipper_length_values, return_counts=True)

fig, ax = plt.subplots()
ax.bar (x,counts)
plt.show()