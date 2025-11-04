#Take a user input string and check if it is a palindrome
a=input("input here: ")
rev = a[::-1]
if(a==rev):
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")