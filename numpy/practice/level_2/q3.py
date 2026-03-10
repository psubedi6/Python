#Find all numbers greater than 50 in a random array of 20 elements.
import numpy as np
arr = np.random.randint(1,100,20)
arr[arr>50]