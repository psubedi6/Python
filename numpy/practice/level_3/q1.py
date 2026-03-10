#Create a 5×5 matrix with values 1–25.
import numpy as np
arr = np.random.randint(1,25,25)
print(arr.reshape(5,5))