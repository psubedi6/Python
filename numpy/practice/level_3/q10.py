#Create a checkerboard pattern (8×8 matrix of 0s and 1s).
import numpy as np
arr = np.zeros((5, 5), dtype=int)
arr[np.arange(5-1), np.arange(1, 5)] = 1
arr[np.arange(5-2), np.arange(2, 5)] = 0
arr[np.arange(5-3), np.arange(3, 5)] = 1
arr[np.arange(5-4), np.arange(4, 5)] = 0
arr[np.arange(1, 5), np.arange(5-1)] = 1
arr[np.arange(2, 5), np.arange(5-2)] = 0
arr[np.arange(3, 5), np.arange(5-3)] = 1
arr[np.arange(4, 5), np.arange(5-4)] = 0
print(arr)