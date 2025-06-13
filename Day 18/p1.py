# 🔹 1.
# Use the math module to calculate the square root, floor, and ceiling of a number entered by the user.




import math

try:
    number = float(input("Enter a number: ").strip())
    print(f"Floor: {math.floor(number)}")
    print(f"Ceiling: {math.ceil(number)}")
    if number < 0:
        print("Square root: Cannot calculate for negative numbers")
    else:
        print(f"Square root: {math.sqrt(number):.2f}")
except ValueError:
    print("Invalid input! Please enter a number.")