# 🔹 2. Simple Login System
# 📌 Objective:
# Create a function that simulates a login check.
# 🧾 Instructions:
# Ask the user to input a username and a password
# Create a function login(username, password)
# Inside the function:
# Check if username is "admin" and password is "1234"
# Return "Login successful!" or "Invalid credentials"
# Print the function's return value




username = input("Username: ")
password =  input("password: ")

def login(username,password):
    if username == "admin" and password == "1234":
        return "Login successful!"
    else:
        return "Invalid credentials!"
    

authenticate = login(username,password)
print(authenticate)