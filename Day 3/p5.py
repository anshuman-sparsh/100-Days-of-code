# 🔹 5. Password Strength Checker (Basic)
# Ask the user to input a password.
# Write logic to check if:
# It's at least 8 characters
# Contains both letters and numbers
# Prints if it's strong or weak






password = input("Enter your password: ")
has_letter = False
has_number = False

for char in password:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        has_letter = True
    elif '0' <= char <= '9':
        has_number = True

if len(password) >= 8 and has_letter and has_number:
    print("Strong password!")
else:
    print("Weak password!")