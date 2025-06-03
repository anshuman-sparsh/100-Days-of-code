# 🔹 3. Age Categorizer
# 📌 Objective:
# Determine a person’s category based on age.
# 🧾 Instructions:
# Ask the user to enter their age
# Create a function categorize_age(age)
# Inside the function, return one of the following:
# "Child" if age < 13
# "Teen" if age is 13–17
# "Adult" if age is 18–60
# "Senior" if age > 60
# Print the result category






age = int(input("Enter your age to know your category: "))

def categorize_age(age):
    if age <= 0:
        return "Invalid!"
    elif age < 13:
        return "Child"
    elif age >= 13 and age <= 17:
        return "Teen"
    elif age >= 18 and age <= 60:
        return "Adult"
    elif age > 60:
        return "Senior"
    


result = categorize_age(age)
print(result)
