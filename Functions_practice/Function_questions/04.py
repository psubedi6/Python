'''
Write a function calculate_area(length, width=10) that returns the area of
a rectangle. Test it by calling the function with:
Both length and width
Only length (use default width)
'''
def calculate_area(length, width):
    area = length * width
    return area

length = int(input("Enter a length of a rectangle: "))
width = int(input("Enter a width of a rectangle: "))

area= calculate_area(length, width)
print(area)