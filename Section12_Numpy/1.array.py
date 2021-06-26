import numpy as np

lists = [1,2,3]

arr = np.asarray(lists)
print(arr)
print(arr.dtype)
print(arr.shape)

zeros = np.zeros(5, dtype= int) # 5-d array dòng
zeros = np.zeros((5,4), dtype= int) # matrix m*n dòng*cột
print(zeros)

ones = np.ones((5,5))
print(ones)

np_range = np.arange(start = 2, step = 2, stop = 20)
print(np_range)

range23 = np.arange(2,20,2)
print(range23) # Giống hệt np_range

# linspace sẽ lấy số lượng phần tử trong khoảng start - stop
np_lin = np.linspace(0 ,30, num = 10, dtype=int)
print(np_lin)
