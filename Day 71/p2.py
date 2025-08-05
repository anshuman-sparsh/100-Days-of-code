import sqlite3

DB_FILE = "Day 71/students.db"

new_students = [
    ('Diana', 23, 'Astrophysics'),
    ('Eve', 21, 'Biochemistry'),
    ('Frank', 25, 'Engineering'),
    ('Grace', 22, 'History'),
    ('Heidi', 24, 'Economics')
]

try:
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()

        insert_query = "INSERT INTO students (name, age, major) VALUES (?, ?, ?);"
        
        cur.executemany(insert_query, new_students)

        print(f"Successfully inserted {len(new_students)} new records.")
        print("-" * 40)
        print("Updated list of all students:")

        cur.execute("SELECT * FROM students;")
        
        all_records = cur.fetchall()

        for record in all_records:
            print(record)

except sqlite3.Error as e:
    print(f"An error occurred: {e}")