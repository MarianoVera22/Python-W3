#----------------Exercise 1----------------

#import numpy as np

# print(np.__version__)
# print(np.show_config())

#----------------Exercise 2----------------

# import numpy as np

# print(np.info(np.add))

#----------------Exercise 3----------------

# import numpy as np

# x=np.array([1,2,3,4])
# print("Original array:")
# print(x)

# print("Test if none of the elements of the said array is zero:")
# print(np.all(x))


# y=np.array([0,2,3,4])
# print("Original array:")
# print(y)

# print("Test if none of the elements of the said array is zero:")
# print(np.all(y))

#----------------Exercise 4----------------

# import numpy as np

# x=np.array([1,0,0,0])
# print("Original array:")
# print(x)

# print("Test if none of the elements of the said array is zero:")
# print(np.any(x))

# y=np.array([0,0,0,0])
# print("Original array:")
# print(y)

# print("Test if none of the elements of the said array is zero:")
# print(np.any(y))

# #----------------Exercise 5----------------

# import numpy as np

# a=np.array([1,0,np.nan,np.inf])
# print("Original array")
# print(a)

# print("Test a given array element-wise for finiteness :")
# print(np.isfinite(a)) 

#----------------Exercise 6----------------

# import numpy as np

# array = np.array([1,-2,np.inf,-np.inf,0,3.5])
# print(array)

# print("Element-wise positive infinity check:", np.isposinf(array))
# print("Element-wise negative infinity check:", np.isneginf(array)) 

#----------------Exercise 7----------------

# import numpy as np

# array = np.array([1,0,np.nan,np.inf])

# print("Original array")
# print(array)

# print("Test element-wise for NaN:")
# print(np.isnan(array)) 

#----------------Exercise 8----------------

# import numpy as np

# m = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])

# print("Original array")
# print(m)

# print("Checking for complex number:")
# print(np.iscomplex(m))

# print("Checking for real number:")
# print(np.isreal(m))

# print("Checking for scalar type:")
# print(np.isscalar(3.1))
# print(np.isscalar([3.1])) 

#----------------Exercise 9----------------

# import numpy as np

# print("Test if two arrays are element-wise equal within a tolerance:")

# print(np.allclose([1e10,1e-7], [1.00001e10,1e-8]))
# print(np.allclose([1e10,1e-8], [1.00001e10,1e-9]))
# print(np.allclose([1e10,1e-8], [1.0001e10,1e-9]))

# print(np.allclose([1.0, np.nan], [1.0, np.nan]))
# print(np.allclose([1.0, np.nan], [1.0, np.nan], equal_nan=True)) 

#----------------Exercise 10----------------

# import numpy as np

# x = np.array([3, 5])
# y = np.array([2, 5])

# print("Original numbers:")
# print(x)
# print(y)

# print("Comparison - greater")
# print(np.greater(x, y))

# print("Comparison - greater_equal")
# print(np.greater_equal(x, y))

# print("Comparison - less")
# print(np.less(x, y))

# print("Comparison - less_equal")
# print(np.less_equal(x, y))


#----------------Exercise 11----------------

# import numpy as np

# x = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
# y = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.00001])

# print("Original numbers:")
# print(x)
# print(y)

# print("Comparison - equal:")
# print(np.equal(x, y))

# print("Comparison - equal within a tolerance:")
# print(np.allclose(x, y)) 

#----------------Exercise 12----------------

# import numpy as np

# x = np.array([1, 7, 13, 105])

# print("Original array:")
# print(x)

# print("Size of the memory occupied by the said array:")
# print("%d bytes" % (x.size * x.itemsize)) 

#----------------Exercise 13----------------

# import numpy as np

# x= np.zeros(10)
# print("An array of 10 zeros:")
# print(x)

# y = np.ones(10)
# print("An array of 10 ones:")
# print(y)

# z=np.ones(10)*5
# print("An array of 10 fives:")
# print(z) 

#----------------Exercise 14----------------

# import numpy as np

# x= np.arange(30, 71)
# print("Array of the integers from 30 to 70")
# print(x) 

#----------------Exercise 15----------------

# import numpy as np

# x= np.arange(30, 71, 2)
# print("Array of all the even integers from 30 to 70")
# print(x) 

#----------------Exercise 16----------------

# import numpy as np

# x=np.identity(3)
# print('3x3 matrix:')
# print(x) 

#----------------Exercise 17----------------

# import numpy as np

# rand_num=np.random.normal(0, 1, 1)
# print("Random number between 0 and 1:")
# print(rand_num)

#----------------Exercise 18----------------

# import numpy as np

# rand_num = np.random.normal(0, 1, 15)
# print("15 random numbers from a standard normal distribution:")
# print(rand_num) 

#----------------Exercise 19----------------

# import numpy as np

# x = np.arange(15, 55)
# print("Original vector:")
# print(x)

# print("All values except the first and last of the said vector:")
# y=x[1:-1]
# print(y) 

#----------------Exercise 20----------------

# import numpy as np

# m= np.arange(20, 32).reshape((3, 4))
# print("Original array:")
# print(m)

# print("Each element of the array is:")
# for i in np.nditer(m):
#     print(i, end=" ")

#----------------Exercise 21----------------

# import numpy as np

# x = np.linspace(10, 49, 5)
# print("Length 10 with values evenly distributed between 5 and 50:")
# print(x)

#----------------Exercise 22----------------

# import numpy as np

# x = np.arange(21)
# print("Original vector:")
# print(x)

# x[(x >= 9) & (x <= 15)] *= -1
# print("After changing the sign of the numbers in the range from 9 to 15:")
# print(x) 

#----------------Exercise 23----------------

# import numpy as np

# x = np.random.randint(0, 11, 5)
# print("Vector of length 5 filled with arbitrary integers from 0 to 10:")
# print(x)

#----------------Exercise 24----------------

# import numpy as np

# x = np.array([1, 8, 3, 5])
# print("Vector-1")
# print(x)

# y = np.random.randint(0, 11, 4)
# print("Vector-2")
# print(y)

# result = x * y
# print("Multiply the values of two said vectors:")
# print(result) 

#----------------Exercise 25----------------

# import numpy as np

# m= np.arange(20, 32).reshape((3, 4))
# print(m)

#----------------Exercise 26----------------

# import numpy as np

# x = np.arange(10, 22).reshape((3, 4))

# print("Original matrix:")
# print(x)

# print("Number of rows and columns of the said matrix:")
# print(x.shape) 

#----------------Exercise 27----------------

# import numpy as np

# x = np.eye(3)
# print(x)

#----------------Exercise 28----------------

# import numpy as np

# x = np.ones((10, 10))

# x[1:-1,1:-1]=0
# print(x)

#----------------Exercise 29----------------

# import numpy as np

# x = np.diag([1, 2, 3, 4, 5])
# print(x) 

#----------------Exercise 30----------------

# import numpy as np

# x = np.zeros((4, 4))

# x[::2, 1::2] = 1
# x[1::2, ::2] = 1
# print(x)

#----------------Exercise 31----------------

# import numpy as np

# x = np.random.random((3, 3, 3))
# print(x)

#----------------Exercise 32----------------

# import numpy as np

# x = np.array([[0, 1], [2, 3]])

# print("Original array:")
# print(x)

# print("Sum of all elements:")
# print(np.sum(x))

# print("Sum of each column:")
# print(np.sum(x, axis=0))

# print("Sum of each row:")
# print(np.sum(x, axis=1)) 

#----------------Exercise 33----------------

# import numpy as np

# x = np.array([4, 5])
# y = np.array([7, 10])

# print("Original vectors:")
# print(x)
# print(y)

# print("Inner product of said vectors:")
# print(np.dot(x, y))

#----------------Exercise 34----------------

# import numpy as np

# m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# v = np.array([1, 1, 0])

# print("Original matrix:")
# print(m)

# print("Original vector:")
# print(v)

# result = np.empty_like(m)

# for i in range(4):
#     result[i, :]=m[i,:]+v
    
# print("\nAfter adding the vector v to each row of the matrix m:")
# print(result)


#----------------Exercise 35----------------

# import numpy as np
# import os

# x1 = np.arange(20)

# np.save('temp_arra.npy', x1)

# print("Check if 'temp_arra.npy' exists or not?")

# if os.path.exists('temp_arra.npy'):
#     x2 = np.load('temp_arra.npy')
    
# print(np.array_equal(x1, x2)) 

#----------------Exercise 36----------------

# import numpy as np
# import os

# x = np.arange(10)
# y = np.arange(11, 20)

# print("Original arrays:")
# print(x)
# print(y)

# np.savez('temp_arra.npz', x=x, y=y)
# print("Load arrays from the 'temp_arra.npz' file:")

# with np.load('temp_arra.npz') as data:
#     x2 = data['x']
#     y2 = data['y']
    
#     print(x2)
#     print(y2) 
    
#----------------Exercise 37----------------

# import numpy as np

# x = np.arange(12).reshape(4, 3)
# print("Original array:")
# print(x)
    
# header = 'col1 col2 col3'
# np.savetxt('temp.txt', x, fmt="%d", header=header)

# print("After loading, content of the text file:")
# result = np.loadtxt('temp.txt')
# print(result)

#----------------Exercise 38----------------

# import numpy as np
# import os

# x = np.array([1, 2, 3, 4, 5, 6])
# print("Original array:")
# print(x)

# x_bytes = x.tobytes()
# x2 = np.frombuffer(x_bytes, dtype=x.dtype)

# print("After loading, content of the text file:")
# print(x2)

# print(np.array_equal(x, x2)) 

#----------------Exercise 39----------------

# import numpy as np

# x = [[1, 2], [3, 4]]

# y = np.array(x)

# x2 = y.tolist()

# print(x==x2)

#----------------Exercise 40----------------

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(0, 3 * np.pi, 0.2)
# y = np.sin(x)

# print("Original array:")
# print(x)

# print("Plot the points using matplotlib:")
# plt.plot(x, y)
# plt.show() 

#----------------Exercise 41----------------

# import numpy as np

# print("numpy.float32 to python float")
# x = np.float32(0)
# print(type(x))

# pyval = x.item()
# print(type(pyval)) 

#----------------Exercise 42----------------

# import numpy as np

# def sum_matrix_Elements(m):
#     a=np.array(m)
#     sum_element=0
    
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             if a[i][j]==0 and i<len(a)-1:
#                 a[i+1][j]=0
                
#             sum_element+=a[i][j]

#     return sum_element



# m = [[1, 1, 0, 2],
#      [0, 3, 0, 3],
#      [1, 0, 4, 4]]

# print("Original matrix:")
# print(m)

# print("Sum:")
# print(sum_matrix_Elements(m)) 

#----------------Exercise 43----------------

# import numpy as np

# nums = np.array([[3, 2, np.nan, 1],
#                  [10, 12, 10, 9],
#                  [5, np.nan, 1, np.nan]])

# print("Original array:")
# print(nums)

# print("\nFind the missing data of the said array:")
# print(np.isnan(nums)) 

#----------------Exercise 44----------------

# import numpy as np

# nums1 = np.array([0.5, 1.5, 0.2])
# nums2 = np.array([0.4999999999, 1.500000000, 0.2])

# np.set_printoptions(precision=15)
# print("Original arrays:")
# print(nums1)
# print(nums2)

# print("\nTest said two arrays are equal (element wise) or not:?")
# print(nums1 == nums2)

#----------------Exercise 45----------------

# import numpy as np

# nums = np.arange(1, 21)
# print("One-dimensional array of single digit numbers:") 
# print(nums)

# nums = np.arange(10, 21)
# print("\nOne-dimensional array of two digit numbers:") 
# print(nums)

# nums = np.arange(100, 201)
# print("\nOne-dimensional array of three digit numbers:") 
# print(nums)

#----------------Exercise 46----------------

# import numpy as np

# print("Create an array of shape (15,10):") 

# print("Command-1")
# print(np.arange(1, 151).reshape(15, 10)) 

# print("\nCommand-2")
# print(np.arange(1, 151).reshape(-1, 10)) 

# print("\nCommand-3")
# print(np.arange(1, 151).reshape(15, -1))

#----------------Exercise 47----------------

# import numpy as np

# np.random.seed(10)
# print(np.random.rand(40)) 


#----------------Exercise 48----------------

# import numpy as np

# np.random.seed(20) 

# cbrt = np.cbrt(7)
# nd1 = 200 
# print(cbrt * np.random.randn(8, 5) + nd1) 

#----------------Exercise 49----------------

# import numpy as np

# print("Generate a uniform random sample with replacement:") 
# print(np.random.choice(7, 5))

# print("\nGenerate a uniform random sample without replacement:") 
# print(np.random.choice(7, 5, replace=False))

# print("\nGenerate a non-uniform random sample with replacement:")
# print(np.random.choice(7, 5, p=[0.1, 0.2, 0, 0.2, 0.4, 0, 0.1]))

# print("\nGenerate a uniform random sample without replacement:")
# print(np.random.choice(7, 5, replace=False, p=[0.1, 0.2, 0, 0.2, 0.4, 0, 0.1])) 

#----------------Exercise 50----------------

# import numpy as np

# nums = np.arange(16, dtype='int').reshape(-1, 4)
# print("Original array:")
# print(nums)

# nums[[0,-1],:] = nums[[-1,0],:]
# print("\nNew array after swapping first and last rows of the said array:")
# print(nums) 

#----------------Exercise 51----------------

# import numpy as np

# nums = np.zeros(shape=(5, 6), dtype='int')
# print("Original array:")
# print(nums)

# nums[::2, ::2] = 3
# nums[1::2, ::2] = 7

# print("\nNew array:")
# print(nums) 

#----------------Exercise 52----------------

# import numpy as np

# nums = np.array([[5.54, 3.38, 7.99],
#               [3.54, 4.38, 6.99],
#               [1.54, 2.39, 9.29]])
# print("Original array:")
# print(nums)

# print("\nSort the said array by row in ascending order:")
# print(np.sort(nums, axis=1))

# print("\nSort the said array by column in ascending order:")
# print(np.sort(nums, axis=0)) 

#----------------Exercise 53----------------

# import numpy as np

# nums = np.array([[5.54, 3.38, 7.99],
#               [3.54, 4.38, 6.99],
#               [1.54, 2.39, 9.29]])
# print("Original array:")
# print(nums)

# n = 5
# print("\nElements of the said array greater than", n)
# print(nums[nums > n])

# n = 6
# print("\nElements of the said array less than", n)
# print(nums[nums < n]) 

#----------------Exercise 54----------------

# import numpy as np

# nums = np.array([[5.54, 3.38, 7.99],
#               [3.54, 8.32, 6.99],
#               [1.54, 2.39, 9.29]])
# print("Original array:")
# print(nums)

# n = 8.32
# r = 18.32

# print("\nReplace elements of the said array which are equal to", n, "with", r)
# print(np.where(nums == n, r, nums))

# print("\nReplace elements of the said array which are less than", n, "with", r)
# print(np.where(nums < n, r, nums))

# print("\nReplace elements of the said array which are greater than", n, "with", r)
# print(np.where(nums > n, r, nums))


#----------------Exercise 55----------------

# import numpy as np

# nums = np.array([[5.54, 3.38, 7.99],
#               [3.54, 8.32, 6.99],
#               [1.54, 2.39, 9.29]])
# print("Original array:")
# print(nums)

# print("\nNew array of equal shape and data type of the said array filled by 0:")
# print(np.zeros_like(nums))

#----------------Exercise 56----------------

# import numpy as np

# nums = np.array([[[1, 5, 2, 1],
#                [4, 3, 5, 6],
#                [6, 3, 0, 6],
#                [7, 3, 5, 0],
#                [2, 3, 3, 5]],
              
#               [[2, 2, 3, 1],
#                [4, 0, 0, 5],
#                [6, 3, 2, 1],
#                [5, 1, 0, 0],               
#                [0, 1, 9, 1]],
              
#               [[3, 1, 4, 2],
#                [4, 1, 6, 0],
#                [1, 2, 0, 6],
#                [8, 3, 4, 0],               
#                [2, 0, 2, 8]]]) 

# print("Array:")
# print(nums)

#----------------Exercise 57----------------

import numpy as np


