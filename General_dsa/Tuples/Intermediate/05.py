#Example input: ((1, 2), (3, 4), (5, 6)) → Output: (1, 2, 3, 4, 5, 6)
tuple1= ((1, 2), (3, 4), (5, 6))
list1=[]
for sublist in tuple1:
    for items in sublist:
        list1.append(items)
finaltuple=tuple(list1)
print(finaltuple)