import numpy as np

# ACCESSING 
arrs = np.arange(0,20) # arrange theo thứ tự từ [0:20] hay 20 con số chạy từ 0 mặc định
print(arrs)

# Order dùng để chuyển hướng giá trị theo chiều xuống
# order must be one of 'C', 'F', 'A', or 'K'
# Dimension phải bằng samples ví dụ 5 * 4 = 20
newArr = np.reshape(arrs, (5,4), order = "F") 
print(newArr)

# Index trong numpy
print(newArr[2,1])

# Index trong list
lists = list(newArr)
print(lists[2][1])



