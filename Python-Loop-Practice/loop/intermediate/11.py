#Print the sum of odd digits in a number.
sum=0
n=int(input("Enter a number: "))
while n>0:
    digit= n%10
    if(digit%2 !=0):
        sum=sum+digit
    n=n//10
print(sum)