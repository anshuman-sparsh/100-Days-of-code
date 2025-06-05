# 🔹 5. Password Cleaner
# Ask user to input a password
# Remove leading/trailing spaces, and replace any @ with a, $ with s, 0 with o
# Print the cleaned password
# Use .strip() and .replace()




print("Get a cleaned password")
password = input("Enter a password: ")


cleaned = password.strip()
cleaned = cleaned.replace("@", "a")
cleaned = cleaned.replace("$", "s")
cleaned = cleaned.replace("0", "o")

print("Cleaned password:", cleaned)