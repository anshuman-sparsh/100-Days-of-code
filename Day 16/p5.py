# 🔹 5.
# Find and print the name of the youngest student from the CSV.





youngest_age = 999
youngest_name = ""

with open("Day 16/students.csv") as f:
    next(f)
    
    for line in f:
        line = line.strip()
        if not line: 
            continue
            
        parts = line.split(',') 
        name, age = parts
        age = int(age)
        if age < youngest_age:
             youngest_age = age
             youngest_name = name

print(f"Youngest student:- {youngest_name}")