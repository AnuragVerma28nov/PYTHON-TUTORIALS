# areaplot matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5] 
y = [10, 20, 15, 30, 25]

plt.fill_between(x, y, color='skyblue', alpha=1)

plt.title('Basic Area Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

plt.show()