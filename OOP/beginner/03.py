#Implement a Circle class with a class constant PI and method area(). Use @staticmethod vs direct constant — when to use each?

class Circle:
    PI= 3.14159
    def __init__(self, radius):
        self.radius= radius
    
    def area(self):
        area= 2 * Circle.PI * self.radius
        print(f"The area is {area}")
radius= int(input("Enter a radius: "))
r1= Circle(radius)
r1.area()