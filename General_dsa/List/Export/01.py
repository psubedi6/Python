#From a given list of integers, create a new list containing the squares of all even numbers using list comprehension.
mylist=[]
evlist=[]
sqlist=[]
n=int(input("Enter a number of element you wanna enter: "))
for i in range(n):
    ele = int(input("Enter a element: "))
    mylist.append(ele)
for j in range (n):
    if mylist[j]%2==0:
        evlist.append(mylist[j])
for k in range (len(evlist)):
    sqlist.append(evlist[k] ** 2)
print(sqlist)