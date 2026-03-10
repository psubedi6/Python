#Extract the middle row and middle column.
import numpy as np
arr= np.array([[ 2,  2, 20,  7,  4],
       [ 8, 16, 17, 10,  4],
       [20,  3,  1,  3, 12],
       [13, 24, 16, 19, 11],
       [ 6, 18,  6, 16, 10]])
a= (((arr.shape[0])//2))
print(arr[:,a])
print(arr[a])