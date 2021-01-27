import numpy as np 

# ---------------- Array Creation ----------------
#Arrays are displayed as a list or list of lists

#When creating an # array, we pass in a list as an argument in numpy array
a = np.array([5, 3, 8])	

#If we pass in a list of lists, we create a multi-dimensional array
b = np.array([[1,2,3],[9,8,7]])	

print("a array")
print(a)
print("\n b array")
print(b)
print()
print("a.ndim: " + str(a.ndim))	#The number of dimensions
print("b.shape: " + str(b.shape)) 	#Length of each dimension
print("a.dtype: " + str(a.dtype))	#Type of items in array

# Note that numpy automatically converts integers, like 5, up to floats, since there is no loss of precision.

print("\nnp.zeros((2,2))")
print(np.zeros((2,2)))		#Create array filled with zeroes
print("\nnp.ones((3,3))")
print(np.ones((3,3)))		#Create array filled with ones
print("\nnp.random.rand(2,3)")
print(np.random.rand(2,3))	#Create array filled by random values

# We can create a sequence of numbers using arrange(). The first argument is the starting bound and the second argument is the ending bound, and the third argument is the difference between each consecutive number.

print("\nnp.arange(20, 40, 4)")
print(np.arange(20, 40, 4))

# If we want to generate a sequence of floats, we can use the linspace() function. In this function the third argument is the total number of items you want to generate

print("\nnp.linspace(20, 40, 6)")
print(np.linspace(20, 40, 12))  #15 numbers from 0 (inclusive) to 2 (inclusive)



# ---------------- Array Creation ----------------
# ---------------- Array Creation ----------------
# ---------------- Array Creation ----------------
