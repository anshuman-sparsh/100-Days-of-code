# 🔹 5. Rectangle Area Calculator
# Create a class Rectangle with length and width.
# Add a method area() that returns the area of the rectangle.



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

my_rectangle = Rectangle(10, 5)
print(f"Area of rectangle: {my_rectangle.area()}")