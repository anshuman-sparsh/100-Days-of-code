from utilis import calculate_age

birth_input = input("Enter your birthdate (YYYY-MM-DD): ")
age = calculate_age(birth_input)
print(f"Your age: {age} years")
