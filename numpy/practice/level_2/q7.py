#Stack two arrays vertically.
import numpy as np
arr1 = ([0,1,2,3,4])
arr2 = ([5,6,7,8,9])
print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))