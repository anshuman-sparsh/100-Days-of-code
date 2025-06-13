# 🔹 5.
# Ask the user for their birthdate (YYYY-MM-DD) and calculate their age in years using datetime.




from datetime import datetime


birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ").strip()
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
today = datetime.now()
age = today.year - birthdate.year
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1
print(f"Your age: {age} years")