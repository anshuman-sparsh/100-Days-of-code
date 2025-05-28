# 🔹 4. Function-Based Calculator
# Rebuild your calculator using a function named calculate(a, b, operator) that takes 3 inputs and returns the result.
# Let the user input two numbers and an operator and call the function to get the answer.





def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Invalid"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator: ")

print("Result:", calculate(a, b, operator))