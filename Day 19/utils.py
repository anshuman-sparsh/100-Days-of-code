def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Undefined (division by zero)"
    return a / b

def check_even_odd(n):
 if n % 2 == 0:
    print(f"{n} is Even.")
 else:
    print(f"{n} is Odd.")


