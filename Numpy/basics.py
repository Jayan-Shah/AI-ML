import numpy as np

# Creating array
arr = np.array([1,2,3,4])
print(arr)

#  Gives 3 by 3 matrix of 0
zeroes = np.zeros([3,3])
print(zeroes)

#  Give 2 by 4 matrix and each element is 1
ones = np.ones([2,4])
print(ones)

# Gives number between 1 to 100 such that they are divisible by 3 or leaving just 3 numbers...
range_array = np.arange(1,100,3)
print(range_array)

# Linspace will give you evenly distributed numbers i.e. number will be between 0 to 10 and there will be 3 numbers evenly distributed
linspace_array = np.linspace(0,10,3)
print(linspace_array)

