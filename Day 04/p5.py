# 🔹 5. Contact Book (Basic Dict)
# Ask the user to enter 3 names and phone numbers
# Store them in a dictionary: {name: number}
# Let user search for a name
# Print the number if found, else say “Not found”





contacts = {}
for i in range(3):
    name = input(f"Enter name {i+1}: ")
    phone_number = input(f"Enter phone number {i+1}: ")
    contacts[name] = phone_number
search_name = input("Search a Name: ")
print("Phone number:", contacts.get(search_name, "Not Found"))