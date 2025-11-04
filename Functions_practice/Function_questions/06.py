#Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.
import math
square = lambda x:math.pow(x, 2)
a=[1, 2, 3, 4, 5]
print(list(map(square, a)))