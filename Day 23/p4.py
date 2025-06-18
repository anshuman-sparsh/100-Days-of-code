# 🔹 4. Circle Class
# Use class variable pi = 3.14. Add instance method to return area.
# Use @classmethod to change the value of pi.



class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2

    @classmethod
    def update_pi(cls, new_value):
        cls.pi = new_value


c1 = Circle(5)
print(f"Area: {c1.area()}")  

Circle.update_pi(3.14159)
print(f"Updated Area: {c1.area()}")  
