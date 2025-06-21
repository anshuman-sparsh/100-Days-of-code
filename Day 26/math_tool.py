# 🔹 2. Math CLI Tool
# Take two numbers (--a, --b) and a --operation (add/sub/mul/div).
# Run it from the terminal to perform the operation and print the result.


import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", type=float, required=True)
    parser.add_argument("--b", type=float, required=True)
    parser.add_argument("--operation", type=str, required=True)

    args = parser.parse_args()
    a = args.a
    b = args.b
    op = args.operation.lower()

    if op == "add":
        print(f"Result: {a + b}")
    elif op == "subtract":
        print(f"Result: {a - b}")
    elif op == "multiply":
        print(f"Result: {a * b}")
    elif op == "divide":
        if b == 0:
            print("Cannot divide by zero!")
        else:
            print(f"Result: {a / b}")
    else:
        print("Invalid operation! Use add, subtract, multiply, or divide.")

if __name__ == "__main__":
    main()

# command to use :- python "Day 26/math_tool.py" --a 10 --b 5 --operation add/subtract/multiply/divide