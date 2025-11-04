#Return both max and min in one pass.
#(using while loop)
def max_min():
    my_list=[]
    while True:
        ele=input("Enter a element: ")
        my_list.append(ele)
        continuee=input("Do you wanna continue? ")
        if continuee != "yes":
            break
        maximum= max(my_list)
        minimum= min(my_list)
    print("The maximum of list is: ",maximum, "\nThe minimum of list is:  ", minimum )
max_min()

#(using for loop)
def max_min():
    my_list=[]
    n=int(input("Enter the number of elements you want in list: "))
    for i in range (n):
        element=input("Enter a element: ")
        my_list.append(element)
        maximum= max(my_list)
        minimum= min(my_list)
    print("The maximum of list is: ",maximum, "\nThe minimum of list is:  ", minimum )
max_min()