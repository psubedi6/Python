#Write a Python program to create a list of 5 numbers and print each element using a for loop.
my_list=[]
n=int(input("Enter a number of element you wanna enter: "))
for i in range(n):
    ele=input("Enter a element: ")
    my_list.append(ele)
print(my_list)