import sqlite3

DB_FILE = "Day 71/students.db"

search_name = input("Enter the student's name to search for: ")


try:
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        
        query = "SELECT * FROM students WHERE LOWER(name) = LOWER(?);"
        
        cur.execute(query, (search_name,))
        
        results = cur.fetchall()

        print("-" * 40)
        if results:
            print(f"Found {len(results)} record(s) matching '{search_name}':")
            for record in results:
                print(record)
        else:
            print(f"No student found with the name '{search_name}'.")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")