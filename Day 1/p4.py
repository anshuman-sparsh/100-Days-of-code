# Practice_4 : Basic Menu

# Show options: Add, Subtract, Exit

# Take choice using input(), handle it with if/else




print("1. Add")
print("2. Subtract")
print("3. Exit")

choice = int(input("Enter your choice (1/2/3): "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
   print(f"sum of the numbers is: {num1+num2}")
elif choice == 2:
   print(f"Minus of the numbers is: {num1-num2}")
elif choice == 3:
   print("GoodBye")
else : 
   print("Invalid! Try Again.")