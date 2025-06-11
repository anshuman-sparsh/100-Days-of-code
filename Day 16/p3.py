# 🔹 3.
# Count how many students are aged above 20 and print the count.



count = 0

with open("Day 16/students.csv") as f:
    next(f)
    
    for line in f:
        line = line.strip()
        if not line: 
            continue
            
        parts = line.split(',') 
        name, age = parts
        age = int(age)
        
        if age > 20:
            count += 1
print("Students aged above 20:", count)