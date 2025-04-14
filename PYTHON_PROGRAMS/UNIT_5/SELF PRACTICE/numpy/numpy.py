# NumPy

import numpy as np

ar = np.array([1, 2, 3, 4, 5])

# Perform basic operations
print("Array:", ar)
print("Mean:", np.mean(ar))
print("Sum:", np.sum(ar))

matrix =np.array([[1, 2, 3], [4, 5, 6]]) # Create a 2D array (matrix)

# Matrix operations
print("Matrix:\n", matrix)
print("Transpose:\n", np.transpose(matrix))
print("Element-wise-additions\n",matrix+10)