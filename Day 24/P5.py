# 🔹 5. Shape → Square
# Shape has attribute color.
# Square has side, area method, and uses super() to set color.



class Shape:
    def __init__(self, color):
        self.color = color

class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def area(self):
        return self.side * self.side

sq = Square("Blue", 4)
print(f"Color: {sq.color}")
print(f"Area: {sq.area()}")
