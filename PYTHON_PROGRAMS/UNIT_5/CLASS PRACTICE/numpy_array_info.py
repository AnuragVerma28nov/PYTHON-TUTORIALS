# Get type, number of elements, base address, and bytes occupied in a NumPy array
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Type:", arr.dtype)
print("Number of elements:", arr.size)
print("Base Address:", arr.ctypes.data)
print("Bytes occupied:", arr.nbytes)
