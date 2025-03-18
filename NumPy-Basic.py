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

import numpy as np

x = np.array([3, 5])
y = np.array([2, 5])

print("Original numbers:")
print(x)
print(y)

print("Comparison - greater")
print(np.greater(x, y))

print("Comparison - greater_equal")
print(np.greater_equal(x, y))

print("Comparison - less")
print(np.less(x, y))

print("Comparison - less_equal")
print(np.less_equal(x, y))