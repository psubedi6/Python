#Given a list of numbers, find the sum of all elements without using the built-in sum() function.
n= int(input("Enter the number of element you wanna enter: "))
mylist=[]
sum =0
for i in range(n):
    ele=int(input("Enter a element: "))
    mylist.append(ele)
for i in range(0,n):
    sum= mylist[i]+ sum
    print(sum)