import numpy as np

arr = np.array([[2,3], [4,10]])
arr_broad = arr * 10
print(arr_broad)
# The 10 is broadcasted across 2,3,4,10

five = np.array([[5,5], [5,5]])
arr1 = arr * five
print(arr1)

