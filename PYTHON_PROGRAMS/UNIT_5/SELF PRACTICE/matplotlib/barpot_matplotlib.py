# barpot matplotlib

import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D'] 
values = [10, 20, 15, 25]

plt.bar(categories, values, color='skyblue')

plt.title('Basic Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()



