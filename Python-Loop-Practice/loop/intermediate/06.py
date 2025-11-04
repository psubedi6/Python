#Check if a number is a palindrome.
n=int(input("Enter the number: "))
b=n
rev=0
while (n>0):
    digit = n%10
    rev=rev*10+digit
    n=n//10
if(b==rev):
    print("Yes it is palindrome")
else:
    print("It is not a palindrome")