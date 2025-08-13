from typing import Optional

USERS_DB = {
    101: {"name": "Alice", "status": "active"},
    102: {"name": "Bob", "status": "inactive"},
}

def find_user(user_id: int) -> Optional[dict]:
    return USERS_DB.get(user_id)

if __name__ == "__main__":
    user_found = find_user(101)
    if user_found:
        print(f"User 101 Found: {user_found}")
    else:
        print("User 101 not found.")

    user_not_found = find_user(999)
    if user_not_found:
        print(f"User 999 Found: {user_not_found}")
    else:
        print("User 999 not found.")