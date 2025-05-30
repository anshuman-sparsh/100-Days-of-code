# 🔹 4. Simple Dictionary Lookup
# Create a dictionary with country names and their capital names

# Ask user to enter a country name
# Print the capital using .get()
# If not found, show "Country not in dictionary"


print("Country name to capital")
capitals ={
    "India": "New Delhi",
    "USA": "Washington DC",
    "Japan": "Tokyo",
    "China": "Beijing",
    "Germany": "Berlin"
}


country = input("Enter a country name:")

print(capitals.get(country,"Country not in dictionary."))