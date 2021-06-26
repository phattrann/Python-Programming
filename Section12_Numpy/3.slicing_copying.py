import numpy as np
# Slicing and Copying

np.random.seed(0) # to save the same random values
np_rand = np.random.random((3,3))
print(np_rand)

sub_rand = np.copy(np_rand[0:2, 0:3])

sub_rand[0,1] = 9
print(sub_rand)
# print(sub_rand)
# print(np_rand)

# It didn't change the original value in np_rand
# by using the *np.copy* function