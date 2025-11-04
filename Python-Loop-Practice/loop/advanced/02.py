#Print the sum of all prime numbers under 50.
num=50
sum=0
for i in range(2,50):
    for j in range(2,i):
        if i %j ==0:
            break
            sum = i+sum