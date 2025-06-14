# 🔹 4.
# Move a birthday age calculator (from Day 18) into utilis.py and call it in mains.py.


with open("Day 19/utilis.py", "a") as f:
    f.write('''from datetime import datetime

def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str.strip(), "%Y-%m-%d")
    today = datetime.now()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age
''')

with open("Day 19/mains.py", "a") as f:
    f.write('''from utils import calculate_age

birth_input = input("Enter your birthdate (YYYY-MM-DD): ")
age = calculate_age(birth_input)
print(f"Your age: {age} years")
''')
