import sqlite3

DB_FILE = "Day 72/students.db"

# Connect to the database
with sqlite3.connect(DB_FILE) as conn:
    cur = conn.cursor()
    
    # SQL's COUNT(*) function counts all rows in the table
    query = "SELECT COUNT(*) FROM students;"
    
    cur.execute(query)
    
    # Using fetchone() to get this single result
    result = cur.fetchone()
    
    
    total_students = result[0]


print(f"Total number of students in the table: {total_students}")