#Write a lambda function that adds two numbers and test it.
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))

add = lambda x,y : a+b
print("The sum is: ",add(a, b))