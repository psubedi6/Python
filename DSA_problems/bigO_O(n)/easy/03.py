#Count how many times a given number appears in an array. using while loop
def max_min():
    my_list=[]
    while True:
        ele=input("Enter a element: ")
        my_list.append(ele)
        continuee=input("Do you wanna continue? ")
        if continuee != "yes":
            break
    occ= input("Enter the element y wanna see number appear: ")
    occrance= my_list.count(occ)
    print("The number of occrance is: ", occrance)
max_min()


#(using for loop)
def max_min():
    my_list=[]
    n=int(input("Enter the number of elements you want in list: "))
    for i in range (n):
        element=input("Enter a element: ")
        my_list.append(element)
    occ= input("Enter the element y wanna see number appear: ")
    occrance= my_list.count(occ)
    print("The number of occrance is: ", occrance)
max_min()