#Write a function that prints all elements in an array.
#(using while loop)
def all_elements():
    my_list=[]
    while True:
        a=input("Enter a element: ")
        my_list.append(a)
        continuee=input("Do you wanna continue? ")
        if continuee != "yes":
            break
    print(my_list)
all_elements()

#(using for loop)
def all_elements():
    l_elements=[]
    n=int(input("How many elements do you wanna enter? "))
    for i in range(n):
        ele=input("Enter a element: ")
        l_elements.append(ele)
    print(l_elements)
all_elements()
