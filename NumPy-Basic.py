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

import numpy as np