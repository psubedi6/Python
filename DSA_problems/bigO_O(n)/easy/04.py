#Sum of all elements in an array
#(using for loop)
def addition():
    my_list=[]
    n= int(input("Enter the number of element: "))
    for i in range(n):
        ele=int(input("Enter a element: "))
        my_list.append(ele)
    add = sum(my_list)
    print(add)

addition()


#(using while loop)
def addition():
    my_list=[]
    while True:
        ele=int(input("Enter a element: "))
        my_list.append(ele)
        continuee= input("do you wanna continue? ")
        if continuee != "yes":
            break
    add = sum(my_list)
    print(add)

addition()