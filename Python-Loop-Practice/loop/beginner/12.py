#Print the reverse of a number (e.g., 123 → 321).
num=int(input("Enter the numbner: "))
rev =0
while num > 0:
    digit = num%10 
    rev= rev*10+digit 
    num=num//10
print(rev)