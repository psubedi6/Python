#mplement an Employee class and a Manager class that inherits Employee. Manager should have an extra method hire().
class Employee:
    def __init__(self, name, salary):
        self.name= name
        self.salary = salary

class Manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
        
    def hire(self):
        print(f"{self.name} has been hired at salary of {self.salary}")

name= input("Enter your name: ")
salary= input("Enput your salary")

m1= Manager(name, salary)
m1.hire()