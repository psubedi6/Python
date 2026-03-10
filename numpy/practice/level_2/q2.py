#Replace all odd numbers in an array with -1.
import numpy as np
arr = np.arange(1,30)
arr[((arr%2)!=0)]= -1
print(arr)