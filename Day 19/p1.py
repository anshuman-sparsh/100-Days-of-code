# 🔹 1.
# Create a file utils.py with functions:
# add(a, b), subtract(a, b), multiply(a, b), divide(a, b)




with open("Day 19/utils.py", "w") as f:
    f.write('''def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Undefined (division by zero)"
    return a / b
''')
