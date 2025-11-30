#Define a Person class with name, age and a greet() method that prints a greeting. Instantiate and call it.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello {self.name}, You are {self.age} years old")

p1= Person("Prakash", "24")
print(p1.greet())