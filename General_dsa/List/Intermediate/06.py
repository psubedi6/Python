#Given two lists, merge them and sort the final list in ascending order.
list1=[]
n1=int(input("Enter a number of element you wanna enter: "))
for i in range(n1):
    ele1 = int(input("Enter a element: "))
    list1.append(ele1)

list2=[]
n2=int(input("Enter a number of element you wanna enter: "))
for j in range(n2):
    ele2 = int(input("Enter a element: "))
    list2.append(ele2)

merge = list1 +list2
new_list = sorted(merge)
print("The sorted list is: ", new_list)