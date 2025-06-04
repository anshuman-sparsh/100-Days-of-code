# 🔹 4. Triangle Type Checker
# Write a function that determines whether a triangle is Equilateral, Isosceles, or Scalene based on side lengths.



side1 = float(input("Enter first side length: "))
side2 = float(input("Enter second side length: "))
side3 = float(input("Enter third side length: "))



def triangle_type(a, b, c):

    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilateral"
        elif a == b or b == c or a == c:
            return "Isosceles"
        else:
            return "Scalene"
    else:
        return "Not a valid triangle"



result = triangle_type(side1, side2, side3)
print(f"This triangle is: {result}")