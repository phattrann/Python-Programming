import numpy as np

arrs1 = np.array([[[1,2,3], [4,5,6]], 
                  [[6,7,8], [8,9,1]],
                  [[2,5,7],[3,4,9]],
                  [[1,3,5], [9,8,7]]])
# print("Org: \n", arrs1)
# print("Shape: ", arrs1.shape)

# a = np.insert(arrs1, 0, [[0,0,0],[0,0,0]], axis = 0)
# print(a)

# a = np.insert(arrs1, 0, [[0,0,0],[0,0,0],[0,0,0],[0,0,0]], axis = 1)
# print(a)

for i in range(4):
    a = np.insert(arrs1[i], 0, [0,0], axis =1)


print(a)