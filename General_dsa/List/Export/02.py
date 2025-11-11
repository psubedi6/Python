#Convert [[1, 2, 3], [4, 5], [6]] into [1, 2, 3, 4, 5, 6] without using external libraries.
l1=[1,2,3]
l2=[4,5]
l3=[6]
newlist=l1+l2+l3
print(newlist)

#another way is 
newl=[]
nested= [[1, 2, 3], [4, 5], [6]]
for sublist in nested:
    for items in sublist:
        newl.append(items)
print(newl)