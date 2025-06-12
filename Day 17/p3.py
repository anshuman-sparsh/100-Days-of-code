# 🔹 3.
# Read students.json and print each student's name and average grade.



import json


with open("Day 17/students.json") as f:
    data = json.load(f) 


for student in data:
    name = student["name"]
    grades = student["grades"]
    average = sum(grades) / len(grades)
    print(f"{name}'s average grade is: {average:.2f}")