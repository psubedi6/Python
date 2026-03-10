#Find the inverse of a matrix.
import numpy as np
a = np.array([[1,2,3],
              [4,5,6],
              [7,3,1]
              ]    
              )

print(np.round(np.linalg.inv(a), 2))