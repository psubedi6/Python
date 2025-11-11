#Take user input and check whether that element exists in the tuple.
mytuple= []
n=int(input("Enter a number of element you wanna enter: "))
for i in range(n):
    ele = input("Enter a element: ")
    mytuple.append(ele)

check= input("Enter a element you wanna check: ")
for j in range (n):
    if check == mytuple[j]:
        print("Yes it exists")
    else:
        print("It doesn't exist")