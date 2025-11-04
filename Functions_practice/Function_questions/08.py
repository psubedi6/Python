#Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.
def sum(n):
    if n==0 or n==1:
        return 1
    else:
        return n+sum(n-1)
    
n=int(input("Enter a number: "))
print(sum(n))