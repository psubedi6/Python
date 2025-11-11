#Create a tuple and print the first, middle, and last elements.
mytuple= []
n=int(input("Enter a number of element you wanna enter: "))
for i in range(n):
    ele = input("Enter a element: ")
    mytuple.append(ele)
middle= int(len(mytuple)/2)
print(mytuple[0])
print(mytuple[-1])
print(mytuple[middle])