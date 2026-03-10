#Count how many numbers are divisible by 3 in an array.
import numpy as np
arr = np.random.randint(1,20,10)
count = np.sum(arr%3 == 0)
print(count)