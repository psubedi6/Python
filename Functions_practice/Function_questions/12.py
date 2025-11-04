#Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.
def Fibonacci(n):
    if n<=1:
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
n= int(input("Enter a number: "))

for i in range(n):
    print(Fibonacci(i))