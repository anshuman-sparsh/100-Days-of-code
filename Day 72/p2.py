import sqlite3

DB_FILE = "Day 72/students.db"

print("--- All Students Sorted by Age (Ascending) ---")

# Connect to the database
with sqlite3.connect(DB_FILE) as conn:
    cur = conn.cursor()
    
    # The ORDER BY clause sorts the results
    query = "SELECT * FROM students ORDER BY age ASC;"
    
    cur.execute(query)
    sorted_students = cur.fetchall()

# Display the results
for student in sorted_students:
    print(student)