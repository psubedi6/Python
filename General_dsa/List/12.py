#Write a program that takes a list of numbers and removes all duplicates using a set.
n=int(input("How many elements you wanna enter?"))
my_set=set()
for i in range(0, n):
    ele=input(f"Enter a element: ")
    my_set.add(ele)
print(my_set)