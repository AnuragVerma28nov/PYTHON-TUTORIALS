# scatterplot matlpotlib

import matplotlib.pyplot as plt

x= [1, 7, 3, 4, 5]
y = [10, 20, 5, 30, 35]

plt.scatter(x, y, color='blue', marker='o')

plt.title('Basic Scatter Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

plt.show()