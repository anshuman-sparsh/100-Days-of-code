# #🔹 4.
# Write a function that takes a dictionary of countries and capitals, and returns the capital if a country is found, otherwise "Not Found".


country_capitals = {
    "India": "New Delhi",
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Australia": "Canberra",
    "Brazil": "Brasília",
    "Canada": "Ottawa",
    "Russia": "Moscow",
    "Italy": "Rome"
}

country_name = input("Enter country name: ").strip().title()  

def find_capital(country_capitals, country_name):
    if country_name in country_capitals:
        return country_capitals[country_name]
    else:
        return "Not Found"

result = find_capital(country_capitals, country_name)
print(f"Capital: {result}")