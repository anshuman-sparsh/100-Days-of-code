# 🔹 2. Calculator with Functions
# Make a menu-based calculator using functions:
# add(a, b), subtract(a, b), multiply(a, b), divide(a, b)
# Let the user input 2 numbers and choose the operation.





print("Enter Two numbers and choose operation to continue")
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
operation = input("Choose Operation to perform: (*,+,-,/): ")

def calculator(a,b,operation):
    multiply = a*b
    add = a+b
    subtract = a-b
    
    if operation == "*":
       print(f"Result = {multiply}")
    elif operation == "+":
        print(f"Result = {add}")
    elif operation == "-":
        print(f"Result = {subtract}")
    elif operation == "/" and b != 0:
        divide = a/b
        print(f"Result = {divide}")
    elif operation == "/" and b == 0:
        print(f"Result = undefined ")
        
    else:
        print("Invalid!")



calculator(a,b,operation)