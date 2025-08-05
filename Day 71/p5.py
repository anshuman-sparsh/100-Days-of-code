import sqlite3

DB_FILE = "Day 71/students.db"

# Get the ID of the student to delete
student_id_to_delete = int(input("Enter the ID of the student to delete: "))

with sqlite3.connect(DB_FILE) as conn:
    cur = conn.cursor()
    
    # Execute the delete command
    cur.execute("DELETE FROM students WHERE id = ?;", (student_id_to_delete,))

    print("-" * 40)
    # Check if a row was actually deleted
    if cur.rowcount > 0:
        print(f"Successfully deleted student with ID {student_id_to_delete}.")
    else:
        print(f"Delete failed: No student found with ID {student_id_to_delete}.")