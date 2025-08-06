import sqlite3

DB_FILE = "Day 72/students.db"

# Get user input
major_input = input("Enter a major (or part of it) to search for: ")

# Connect and execute the search
with sqlite3.connect(DB_FILE) as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE major LIKE ?", (f"%{major_input}%",))
    results = cur.fetchall()

# Display the results
print("-" * 40)
if results:
    print(f"Found students in majors like '{major_input}':")
    for student in results:
        print(student)
else:
    print("No matching students found.")