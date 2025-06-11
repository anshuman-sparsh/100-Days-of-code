# 🔹 4.
# Create a new file adults.csv and store only the records of students aged ≥ 18.




with open("Day 16/students.csv") as f, open("Day 16/adults.csv", "w") as c:
    next(f)  

    for line in f:
        line = line.strip()
        if not line:
            continue
        name, age = line.split(',')
        if int(age) >= 18:
            c.write(f"{name},{age}\n")