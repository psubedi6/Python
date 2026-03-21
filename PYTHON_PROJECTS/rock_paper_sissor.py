import random

while True:
    choose= input("Enter your choise: s,p,r").lower 
    result = random.choose(choose)

    if choose == result:
        print("Draw!! ")
    elif(
        (choose == "r" and result == "s")
        (choose == "s" and result == "p")
        (choose == "p" and result == "r")):
        print("You win!!")
    else:
        print("You loose!!")

    again= input(print("Enter y if y wanna contunue and n if you don't wanna continue"))
    if again == "n":
        break