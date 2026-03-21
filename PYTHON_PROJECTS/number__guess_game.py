import random
r = random.randint(1,10)

while True:
    number= int(input("Enter a number: "))
    if number== r:
        print("The number you guessed is correct ")
        break
    elif number > r:
        print("the number is smaller then the number you entered")
    elif number< r: 
        print("the number is larger then the number you entered")
    else:
        print("Your input is invalid")
