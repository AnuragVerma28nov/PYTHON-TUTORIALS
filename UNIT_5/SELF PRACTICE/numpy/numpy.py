# NumPy

import numpy as np

array = np.array([1, 2, 3, 4, 5])

# Perform basic operations
print("Array:", array)
print("Mean:", np.mean(array))
print("Sum:", np.sum(array))

matrix = np.array([[1, 2, 3], [4, 5, 6]]) # Create a 2D array (matrix)

 # Matrix operations
print("Matrix:\n", matrix)
print("Transpose:\n", np.transpose(matrix))
print("Element-wise-additions\n",matrix+10)