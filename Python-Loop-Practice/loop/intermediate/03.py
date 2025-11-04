#Check if a number is prime using a loop.
num=int(input("Enter the number: "))
for j in range(2,num):
    if(num%j==0):
         print(f"{num} not Prime number")
         break
else:
    print(f"{num} prime number")