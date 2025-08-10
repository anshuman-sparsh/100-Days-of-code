import sqlite3
import os
from contextlib import contextmanager

DB_NAME = "Day 76/p4.sqlite"

@contextmanager
def database_manager(db_name):
    conn = sqlite3.connect(db_name)
    print(f"--> Connection to '{db_name}' opened.")
    try:
        yield conn.cursor()
        print("--> Transaction had no errors.")
        conn.commit()
    except Exception as e:
        print(f"--> An error occurred: {e}")
        print("--> Rolling back transaction.")
        conn.rollback()
    finally:
        print("--> Connection closed.")
        conn.close()


if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

# 1. Successful transaction
print("\n--- Running a successful transaction ---")
with database_manager(DB_NAME) as cursor:
    cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
    cursor.execute("INSERT INTO users VALUES (?, ?)", (1, "Alice"))
print("------------------------------------")


# 2. Failed transaction
print("\n--- Running a transaction that will fail ---")
try:
    with database_manager(DB_NAME) as cursor:
        cursor.execute("INSERT INTO users VALUES (?, ?)", (2, "Bob"))
        # This next line will cause an error
        cursor.execute("INSERT INTO users VALUES (?, ?)", ("three", "Charlie"))
except Exception:
    # catch the error here just to continue script
    print("--> Main script caught the expected error.")
print("------------------------------------")


# 3. Verify the database content
print("\n--- Verifying final database content ---")
final_conn = sqlite3.connect(DB_NAME)
final_cursor = final_conn.cursor()
final_cursor.execute("SELECT * FROM users")
results = final_cursor.fetchall()
final_conn.close()

print(f"Final content: {results}")
print("Only 'Alice' is in the database because the second transaction was rolled back.")