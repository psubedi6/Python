#Replace the diagonal elements of a matrix with 0.
import numpy as np
arr= np.array([[1,2,3],
      [4,5,6],
      [7,8,9]])
np.fill_diagonal(arr, 0)
print(arr)