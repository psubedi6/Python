#Take 5 numbers as input and print their average.
total=0
for i in range(1,6):
    num=int(input("Enter the number: "))
    total=total+num
average= total/5
print(f"The average of number entered is: {average}")