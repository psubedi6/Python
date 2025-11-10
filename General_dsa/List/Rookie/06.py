#Given a list of integers, count how many times a specific number appears in the list.
mylist=[]
sum=0
n=int(input("Enter the number pf element you wanna enter: "))
for i in range(n):
    ele=input("Enter a element: ")
    mylist.append(ele)
check=input("Enter a element you wanna check: ")
for j in range(n):
    if check == mylist[j]:
        sum = sum +1
print(sum)