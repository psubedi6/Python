#take a number as input and print its multiplication table.
num= int(input("Enter the number:"))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")