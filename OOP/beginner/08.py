#Create a Car class, then create a from_string classmethod that constructs a Car from "make:model:year".
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model= model
        self.year= year
    def result(self):
        print(f"The make of car is: ", self.make)
        print(f"The model of car is: ", self.model)
        print(f"The year of car is: ", self.year)
make = input("Enter the make of the car: ",)
modul = input("Enter the model of the car: ")
year = input("Enter the year of the car: ")
s1= Car(make, modul, year)
s1.result()