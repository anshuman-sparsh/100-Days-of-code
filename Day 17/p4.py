# 🔹 4.
# Add a new student to the list and overwrite the updated list back into the file.




import json

# Step 1: Open and load existing student data
with open("Day 17/students.json", "r") as f:
    students = json.load(f)


new_student = {
    "name": "aarush",
    "age": 18,
    "grades": [88,78,90]
}

students.append(new_student)

with open("Day 17/students.json", "w") as f:
    json.dump(students, f, indent=2)

print("New student added successfully!")
