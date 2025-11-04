#Take 10 inputs from the user and find their sum.
b=0
for i in range(1,11):
    a=int(input(f"Enter {i} number: "))
    b=b+a
print(f"The sum of number entered is: {b}")