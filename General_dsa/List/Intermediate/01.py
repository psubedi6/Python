#Write a program to reverse a list without using the built-in .reverse() or slicing ([::-1]).
mylist=[]
n=int(input("Enter a number of element you wanna enter: "))
for i in range(n):
    ele = input("Enter a element: ")
    mylist.append(ele)

start = 0
end = n-1

while start< end:
    mylist[start], mylist[end] = mylist[end], mylist[start]
    start = start+1
    end = end-1
print("The reverse is: ", mylist)