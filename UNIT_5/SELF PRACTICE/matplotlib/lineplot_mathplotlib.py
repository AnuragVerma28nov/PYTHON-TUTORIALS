# lineplot mathplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y= np.array([10, 20, 25, 30, 35])

plt.plot(x, y, marker='o', color='r')

plt.title('Basic Line Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.grid(True)

plt.show()