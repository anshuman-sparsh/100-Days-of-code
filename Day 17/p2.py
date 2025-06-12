# 🔹 2.
# Save a list of 3 such student dictionaries into a file called students.json using json.dump().



import json

students = [
    {
        "name": "Aarav",
        "age": 20,
        "grades": [85, 78, 92]
    },
    {
        "name": "Isha",
        "age": 19,
        "grades": [74, 81, 69]
    },
    {
        "name": "Rohan",
        "age": 21,
        "grades": [90, 88, 91]
    }
]


with open("Day 17/students.json","w") as f:
    json.dump(students,f)