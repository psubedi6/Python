#Determine if the array is sorted in ascending order in O(n).
#(using for loop)
def order():
    my_list=[]
    n=int(input("Enter the number of elements you want: "))
    for i in range(n):
        ele = int(input("Enter the element: "))
        my_list.append(ele)
        my_list.sort()
        print(my_list)
order()