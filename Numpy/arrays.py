import numpy as np

# Manipulate Array
arr = np.array([1,2,3,4,5,6])
reshaped = arr.reshape([3,2])
print(reshaped)

# Add Dimension
arr = np.array([1,2,3])
expanded = arr[:, np.newaxis]
# expanded2 = expanded[:, np.newaxis] Trials
print(expanded)

# Operations on arrays
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)
print(a*b)
print(a/b)
print(np.sqrt(a))
print(np.sum(b))
print(np.mean(a+b))
print(np.max(b))

# Array Indexing
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[2])
print(arr[-1])

# Slicing
print(arr[1:4])
print(arr[3:])

# Matrix Transpose
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Original Matrix\n",matrix)
transpose = matrix.T
print("\nTranspose Matrix\n", transpose)



