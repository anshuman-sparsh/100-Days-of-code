import sqlite3

# Set the path for the database file.
DB_FILE = "Day 72/students.db"

# Get the student's name and new age from the user.
student_name = input("Enter the name of the student to update: ")
new_age = int(input(f"Enter the new age for {student_name}: "))

# Connect to the database to perform the update.
with sqlite3.connect(DB_FILE) as conn:
    cur = conn.cursor()
    
    # Update a student's age using their name (case-insensitive).
    query = "UPDATE students SET age = ? WHERE LOWER(name) = LOWER(?);"
    
    cur.execute(query, (new_age, student_name))

    # Give the user feedback on the result of the operation.
    print("-" * 40)
    if cur.rowcount > 0:
        print(f"Successfully updated age for '{student_name}'.")
    else:
        print(f"No student found with the name '{student_name}'.")