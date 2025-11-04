#Write a function square(num) that returns the square of a given number. Test it with different numbers.
import math
def square(a):
    print("The square of given number is: ", math.pow(a, 2))

a= int(input("Enter a number: "))
square(a)