"""
B18101105
NAME: SUMNA IMRAN
REACP TO NUMPY
"""
import numpy as np
print("---ARRAYS---")
a = np.array([1,2,3])
print(type(a))
print(a.shape)
print(a[0],a[1],a[2])
a[1] = 5
print(a)

a = np.zeros((2,2))
print(a)
a = np.ones((3,3))
print(a)
a = np.full((2,2),5)
print(a)
print("---------------")

print("---ARRAY INDEXING---")
# [[ 1 2 3 4]
# [ 5 6 7 8]
# [ 9 10 11 12]]
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# [[2 3]
# [6 7]]
b = a[:2,1:3]
print(b)
# will modify the original array.
print(a[0, 2]) 
b[0,1] = 77  # b[0, 1] is the same piece of data as a[0, 2]
print(a[0, 2])
print("new array a is: \n",a)
#accessing the data in the middle row of the array.
row_r1 = a[1, :]
row_r2 = a[1:2, :]
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)
# We can make the same distinction when accessing columns of an array
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape) # Prints "[ 2 6 10] (3,)"
print(col_r2, col_r2.shape)
#Integer array indexing:
a = np.array([[1,2], [3, 4], [5, 6]])
# [[1 2]
# [3 4]
# [5 6]] 
print(a[[0, 1, 2], [0, 1, 0]]) 
# The above example of integer array indexing is equivalent to this:
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))
# element from the source array:
print(a[[0, 0], [1, 1]])
# Equivalent to the previous integer array indexing example
print(np.array([a[0, 1], a[0, 1]])) 

a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print("new array a is: \n",a)
#Create an array of indices
b =  np.array([0, 2, 0, 1])
print(b)
# Select one element from each row of a using the indices in b
print(a[np.arange(4), b])
# Mutate one element from each row of a using the indices in b
a[np.arange(4), b] += 10
print("new array a is: \n",a)

#Boolean array indexing:
a = np.array([[1,2], [3, 4], [5, 6]])
bool_idx = (a > 2) 
print(bool_idx) 
print(a[bool_idx])
print(a[a > 2]) 
print("---------------")

print("---DATA TYPES---")
x = np.array([1, 2]) 
print(x.dtype)  # Prints "int64"
x = np.array([1.0, 2.0]) 
print(x.dtype)  # Prints "float64"
x = np.array([1, 3.0], dtype=np.int64)  # Force a particular datatype
print(x.dtype)
print("---------------")

print("---ARRAY MATH---")
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
#print(x + y)
print("the addition is: \n",np.add(x, y))
#print(x - y)
print("the subtraction is: \n",np.subtract(x, y))
#print(x * y)
print("the product is: \n",np.multiply(x, y))
#print(x / y)
print("the division is: \n",np.divide(x, y))
print("the squart root is: \n",np.sqrt(x))
print()
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
v = np.array([9,10])
w = np.array([11, 12])
# Inner product of vectors; both produce 219
#print(v.dot(w))
print(np.dot(v, w))
# Matrix / vector product; both produce the rank 1 array [29 67]
#print(x.dot(v))
print(np.dot(x, v))
# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
# [43 50]]
#print(x.dot(y))
print(np.dot(x, y))
print()
x = np.array([[1,2],[3,4]])
print(np.sum(x)) # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0)) # Compute sum of each column
print(np.sum(x, axis=1)) # Compute sum of each row
print()
x = np.array([[1,2], [3,4]])
print(x) 
print(x.T) 
# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print(v) 
print(v.T) 
print("-----------------")

print("---ARRAY BROADINGCATING---")
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x) # Create an empty matrix with the same shape as x
# Add the vector v to each row of the matrix x with an explicit loop
for i in range(4):
 y[i, :] = x[i, :] + v
print(y)

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1)) # Stack 4 copies of v on top of each other
print(vv)
y = x + vv # Add x and vv elementwise
print(y)

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v # Add v to each row of x using broadcasting
print(y)

v = np.array([1,2,3]) # v has shape (3,)
w = np.array([4,5]) # w has shape (2,)
print(np.reshape(v, (3, 1)) * w)
# Add a vector to each row of a matrix
x = np.array([[1,2,3], [4,5,6]])
# x has shape (2, 3) and v has shape (3,) so they broadcast to (2,3),
print(x + v)
print((x.T + w).T)
(2, 1);
print(x + np.reshape(w, (2, 1)))
print(x * 2)

"""from scipy.misc import imread, imsave, imresize
# Read an JPEG image into a numpy array
img = imread('assets/internet.jpg')
print(img.dtype, img.shape)
img_tinted = img * [1, 0.95, 0.9]
img_tinted = imresize(img_tinted, (300, 300))
imsave('assets/cat_tinted.jpg', img_tinted)
"""

print("---MATLAB FILE---")
print("---Distance between two points---")
from scipy.spatial.distance import pdist, squareform
x = np.array([[0, 1], [1, 0], [2, 0]])
print(x)
d = squareform(pdist(x, 'euclidean'))
print("the distance is:\n",d)

print("---MATPLOTLIB---")
import matplotlib.pyplot as plt
# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
# Plot the points using matplotlib
plt.plot(x, y)
#plt.show()

import numpy as np
import matplotlib.pyplot as plt
# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# Plot the points using matplotlib
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
#plt.show()

import matplotlib.pyplot as plt
# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# Set up a subplot grid that has height 2 and width 1,
# and set the first such subplot as active.
plt.subplot(2, 1, 1)
# Make the first plot
plt.plot(x, y_sin)
plt.title('Sine')
# Set the second subplot as active, and make the second plot.
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')
# Show the figure.
plt.show()

