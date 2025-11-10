#Write a program to find the largest and smallest numbers in a list using loops.
mylist=[]
n=int(input("Enter a number of element in a list: "))
for i in range(n):
    ele=int(input("Enter a element: "))
    mylist.append(ele)

for j in range(n):
    a=mylist[j]
    maximum= max(mylist)
    minimum= min(mylist)
print("The maximum number is: ",maximum)
print("The minimum number is: ",minimum)