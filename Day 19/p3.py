# 🔹 3.
# Add a function in utils.py to check if a number is even or odd. Use it from main.py.



with open("Day 19/utils.py", "a") as f:
    f.write('''\ndef check_even_odd(n):
 if n % 2 == 0:
    print(f"{n} is Even.")
 else:
    print(f"{n} is Odd.")''')


with open("Day 19/main.py", "w") as f:
    f.write('''from utils import add, subtract, multiply, divide, check_even_odd

while True:
    print("\\nCalculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Check Even/Odd")
    print("6. Exit")

    choice = input("Choose an option (1-6): ").strip()

    if choice in ["1", "2", "3", "4"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == "1":
            print(f"Result: {add(a, b)}")
        elif choice == "2":
            print(f"Result: {subtract(a, b)}")
        elif choice == "3":
            print(f"Result: {multiply(a, b)}")
        elif choice == "4":
            print(f"Result: {divide(a, b)}")

    elif choice == "5":
        n = int(input("Enter number: "))
        check_even_odd(n)

    elif choice == "6":
        print("Exited!")
        break

    else:
        print("Invalid option. Please choose again.")''')
