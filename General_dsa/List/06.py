#Convert the tuple to a list, change its first element to 50 , and convert it back to a tuple.
coordinates=(10,20)
my_list=list(coordinates)
my_list[0]=50
print(tuple(my_list))