# 🔹 2. Simple Calculator
# Ask the user to enter two numbers and an operator (+, -, *, /).
# Use if-else conditions to perform the operation and print the result.






a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Choose operation (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    print("Result:", a / b)
else:
    print("Invalid operator.")