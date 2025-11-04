def max_min():
    my_list=[]
    while True:
        ele=input("Enter a element: ")
        my_list.append(ele)
        continuee=input("Do you wanna continue? ")
        if continuee != "yes":
            break
    print(my_list)
max_min()