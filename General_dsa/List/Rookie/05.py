#Take a list and an element as input; check whether the element exists in the list or not.
n=int(input("Enter a number of element you wan t: "))
mylist=[]
for i in range(n):
    ele=input("Enter a element: ")
    mylist.append(ele)
check=input("Enter the element you wanna check: ")
for i in range(n):
    if check== mylist[i]:
        print(f"The element {mylist[i]} exists")
    else:
        print(f"The element {mylist[i]} do not exists")