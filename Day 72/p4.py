import sqlite3

DB_FILE = "Day 72/students.db"

print("--- Details of the Oldest Student(s) ---")

# Connecting to the SQLite database.
with sqlite3.connect(DB_FILE) as conn:
    cur = conn.cursor()
    
    # Find the oldest students using a subquery.
    query = "SELECT * FROM students WHERE age = (SELECT MAX(age) FROM students);"
    
    cur.execute(query)
    
    # Fetch all students who match the maximum age.
    oldest_students = cur.fetchall()

# Display the results on the screen.
if oldest_students:
    for student in oldest_students:
        print(student)
else:
    print("The student table is empty.")