#Swap Two Tuples Without Using a Temporary Variable
a=(1,2,3,4)
b=(5,6,7,8)
a,b=b,a
print("The swapped value of first tuple is: ",a)
print("The swapped value of second tuple is: ",b)