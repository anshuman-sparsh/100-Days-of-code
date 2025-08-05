import sqlite3

DB_FILE = "Day 71/students.db"

with sqlite3.connect(DB_FILE) as conn:
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        major TEXT
    )
    """)
    
    cur.execute("DELETE FROM students;")

    cur.execute("INSERT INTO students (name, age, major) VALUES ('Alice', 21, 'Computer Science');")
    cur.execute("INSERT INTO students (name, age, major) VALUES ('Bob', 22, 'Physics');")
    cur.execute("INSERT INTO students (name, age, major) VALUES ('Charlie', 20, 'Mathematics');")
    
    print(f"Database '{DB_FILE}' created/updated.")
    print("3 records inserted successfully.")
    print("-" * 30)

    cur.execute("SELECT * FROM students;")
    
    all_students = cur.fetchall()

    print("Fetching all records:")
    for student in all_students:
        print(student)