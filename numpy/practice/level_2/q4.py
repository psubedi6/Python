#Generate a 5×5 matrix of random integers between 1 and 100.
import numpy as np
arr = np.random.randint(1,100,25)
print(arr.reshape(5,5))