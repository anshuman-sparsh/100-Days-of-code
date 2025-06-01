# 🔹 4. Product Price Checker
# Create a dictionary of 4 products and their prices
# Ask user to input a product name
# Print the price if found, else print “Not available”
# Use .get() safely



products_and_price = {
    "mango": "₹90",
    "lichi": "₹80",
    "banana": "₹70",
    "grapes": "₹60"
}

product = input("Enter product name to know its price: ").lower()

if product in products_and_price:
    print(products_and_price.get(product))
else:
    print("Not Available!")