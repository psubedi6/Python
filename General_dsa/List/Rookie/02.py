#Write a Python program to create a list of 5 numbers and print each element using a for loop.
mylist=[]
n=int(input("Enter number of elements you wanna input: "))
for i in range(n):
    ele=input("Enter the element: ")
    mylist.append(ele)
for i in range(0,n):
    a=mylist[i]
    print(a)