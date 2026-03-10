#Reshape a 1D array of size 9 into a 3x3 matrix.
import numpy as np
c = np.random.randint(0,10,(1,9))
print(c.reshape(3,3))