#Given a list, write a function to rotate its elements to the right by k positions. Example: [1,2,3,4,5], k=2 → [4,5,1,2,3]
mylist=[]
n=int(input("Enter a number of element you wanna enter: "))
for i in range(n):
    ele = int(input("Enter a element: "))
    mylist.append(ele)
reverse= mylist[3::]
print(reverse)
##########need to be done