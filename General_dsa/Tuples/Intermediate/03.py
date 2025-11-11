#Given a tuple of numbers, find the smallest and largest elements without converting it to a list.
mytuple=(134,5,3,54,344,534,3,34,2,45,34,4,76,554,23)
mylist =list(mytuple)
for i in range(len(mylist)):
    maximum= max(mylist)
    minimum= min(mylist)
print("The maximum: ", maximum)
print("The minimum: ", minimum)