import numpy as np
# Array and Scalar BroadCasting 
arr = np.array([1,2,3])
print(arr + 10) #This will add 10 to each element in the array which is scalar broadcasting

matrix = np.array([[1,2,3], [4,5,6]])
vector = np.array([1,0,1])
print(matrix+vector) # Array broadcasting

# Aggregation Functionns 
arr = np.array([[1,2,3],[4,5,6]])

print ("Sum ",np.sum(arr))
print ("Mean", np.mean(arr))
print("Max ", np.max(arr))
print("Min ",np.min(arr))
print("Standard deviation:", np.std(arr))
print("Sum along the rows: ", np.sum(arr,axis=1))
print("Sum along the columns:", np.sum(arr,axis=0))


# Boolean Indexing And Filtering
arr =np.array([1,2,3,4,5,6])

evens =arr[ arr % 2 == 0 ]
print("Evens:", evens)

arr[arr>3] = 0
print("Modified Arrray: ", arr)

# Random Module of Numpy

# Random seed
np.random.seed(42)

random_array = np.random.rand(3,3)
print("Random Array: \n", random_array)

random_integers = np.random.randint(0,10,size=(2,3))
print("Random Intergers are:\n",random_integers)
