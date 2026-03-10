#Normalize an array (scale between 0 and 1).
import numpy as np
arr=  np.random.randint(1,20,10)
print((arr-np.min(arr))/(np.max(arr) - np.min(arr)))