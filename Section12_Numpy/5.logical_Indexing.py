import numpy as np

arrs = np.array([[1,5,3], [4,1,6], [2,4,10]])

np_cond = arrs[arrs > 3]

print(np_cond)
print(arrs > 3)
