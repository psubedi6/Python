#Write a program to find the second largest number in a list without using max() twice.
mylist=[]
n=int(input("Enter a number of element you wanna enter: "))
for i in range(n):
    ele = int(input("Enter a element: "))
    mylist.append(ele)
b=len(mylist)
for j in range (b-1):
    mylist.remove(min(mylist))
print(mylist[0])