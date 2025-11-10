#List Slicing Practice
#Given a list of numbers from 1 to 10, print:
#The first three elements
#The last three elements
#Every second element
#The list in reverse
mylist=[]
n=11
for i in range(1,n):
    mylist.append(i)

print("The first three elements: ", mylist[:3])
print("The last three elements: ", mylist[-3:])
print("Every second elements: ", mylist[::2])
print("The list in reverse: ",mylist[::-1])
print(mylist)