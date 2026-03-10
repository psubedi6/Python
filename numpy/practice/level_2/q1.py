#Create an array from 1 to 20 and print only even numbers.
import numpy as np
arr = np.arange(1,20)
print(arr[(arr % 2) == 0])