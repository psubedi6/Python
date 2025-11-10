#Write a function that removes duplicate elements from a list and returns the new list.
mylist=[]
def new_list():
    n=int(input("Enter a number of element you wanna enter: "))
    for i in range(n):
        ele = input("Enter a element: ")
        mylist.append(ele)
new_list()
my_set= set(mylist)
new_list= list(my_set)
print("The new list is: ", new_list)