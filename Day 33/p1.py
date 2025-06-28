# 🔹 1. Voting Eligibility System
# 📌 Ask user to enter name and age.
# ✅ Create get_user_info() and is_eligible(age) functions.
# If age ≥ 18 → print: "Anshuman, you are eligible to vote!"
# Else → print: "Sorry Anshuman, try again when you're older."




def get_user_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

def is_eligible(age):
    return age >= 18


name, age = get_user_info()

if is_eligible(age):
    print(f"{name}, you are eligible to vote!")
else:
    print(f"Sorry {name}, try again when you're older.")
