#Given an array, print all possible pairs of elements (a[i], a[j]).(Concept: Nested loops traversal)
def pairs():
    arr= []
    n= int(input("Enter the number: "))
    for i in range(n):
        ele= int(input("Enter a element: "))
        arr.append(ele)
    print("All possible pairs: ")
    for i in range(n):
        for j in range(n):
            print(f"({arr[i]},{arr[j]})")
pairs()