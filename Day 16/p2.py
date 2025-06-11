# 🔹 2.
# Split each line into name and age, and print in a formatted way: Name: John, Age: 21





with open("Day 16/students.csv") as f:
    next(f)
    
    for line in f:
        line = line.strip()
        if not line: 
            continue
            
        parts = line.split(',') 
        name, age = parts
        
        print(f"Name: {name}, Age: {age}")