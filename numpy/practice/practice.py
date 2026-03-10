#use boolean masking to filter numbers greater than 50 in an array
import numpy as np
d = np.random.randint(0,100,(1,100))
print(d[d > 50])