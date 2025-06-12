# 🔹 5.
# Search for a student by name and print their full record. If not found, print “Not Found”.





import json

with open("Day 17/students.json") as f:
    students = json.load(f)

search_name = input("Enter student name to search: ").strip()

try:
    found = False
    for student in students:
        if student["name"].lower() == search_name.lower():
            print("Student found:")
            print(student)
            found = True
            break
    if not found:
        raise ValueError("Not Found!")
except ValueError as e:
    print(e)