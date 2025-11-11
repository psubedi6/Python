#Find Common Elements Between Two Tuples Input: (1, 2, 3, 4) and (3, 4, 5, 6) → Output: (3, 4)
tup1=(1, 2, 3, 4)
tup2=(2,3, 4, 5, 6)
list1=tup1+tup2
newoutput= []

for i in list1:
    c= list1.count(i)
    if c > 1 and i not in newoutput:
        newoutput.append(i)
print(newoutput)