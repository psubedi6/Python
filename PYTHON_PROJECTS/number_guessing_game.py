#number guessing software
import random

class Num_Guess:
    def __init__(self,num):
        self.num= num
        self.randomnum = random.randint(1,10)

    def guess(self):
        while True:
            if num == self.randomnum:
                print("you guessed the correct number: ")
                break
            else:
                print("wrong guess, try again!!") 
                break

randomnum = random.randint(1, 10)
num=int(input("Enter a number: "))
num1= Num_Guess(num)
num1.guess()