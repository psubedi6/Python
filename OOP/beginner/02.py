#Create a Rectangle class with width, height, methods area() and perimeter().
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height= height

    def area(self):
        area= self.width * self.height 
        print(f"The area is {area}")

    def perimeter(self):
        perimeter = 2*(self.width + self.height)
        print(f"The perimeter is: {perimeter}")

a1 = Rectangle(12, 16)
a1.area()
a1.perimeter()