#Import the math module and use it to:
#Find the square root of 144
#Calculate sin(90°) (hint: use math.radians() )
import math
def square(a):
    a=math.pow(a, 2)
    return a
a=int(input("Enter a number: "))
print(square(a))


def root(b):
    b= math.sin(b)
    return b
b=int(input("Enter a sine degree: "))
print (root(b))