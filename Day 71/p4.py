import sqlite3

DB_FILE = "Day 71/students.db"

# Get input from the user
student_id = int(input("Enter the ID of the student to update: "))
new_major = input(f"Enter the new major for student ID {student_id}: ")

# Connect and execute the update
with sqlite3.connect(DB_FILE) as conn:
    cur = conn.cursor()
    cur.execute("UPDATE students SET major = ? WHERE id = ?", (new_major, student_id))

# Print a simple confirmation message
print(f"\nUpdate command sent for student ID {student_id}.")