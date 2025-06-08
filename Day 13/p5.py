# 🔹 5.
# Create a user login simulator where invalid username/password throws an error, and "Login successful" is printed on correct input.




def login(username, password):
    if username != "admin" or password != "password123":
        raise ValueError("Invalid username or password!")
    return "Login successful!"

try:
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    print(login(username, password))
except ValueError as e:
    print(e)