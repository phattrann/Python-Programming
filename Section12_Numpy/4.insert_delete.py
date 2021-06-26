import numpy as np

arrs = np.array([[1,2], [4,5]])
print("Org: ", arrs)

arrIn = np.insert(arrs, 0, [6,8], axis = 1)
print("INsert: ", arrIn)

# if no axix in append: return 1 dimensional space
arrApp = np.append(arrs, [[3,3], [7,9]], axis = 0)
print("App: ", arrApp)

arrDel = np.delete(arrApp, [1,3], axis = 0)
print("Del:", arrDel)

