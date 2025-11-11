#Given t = (1, 3, 7, 8, 7, 5, 6, 8, 5), count how many times 7 appears and find its first index.
t = (1, 3, 7, 8, 7, 5, 6, 8, 5)
c = t.count(7)
ind= t.index(7)
print(f"The number {7} appears: ",c)
print(f"The first index of {7} is: ", ind)