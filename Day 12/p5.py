# 🔹 5.
# Create a function that takes a dictionary of item:price and returns a new dictionary with only the items that cost more than ₹100.



user_input = input("Enter items and prices (Format: item:price, item2:price2): ")
items = {}

def filter_expensive(items):
    result = {}
    for key, value in items.items():
        if value > 100:
            result[key] = value
    return result


for pair in user_input.split(","):
    if ":" in pair:
        item, price = pair.strip().split(":")
        if price.replace('.', '', 1).isdigit():
            items[item.strip()] = float(price.strip())

expensive = filter_expensive(items)

if expensive:
    for item, price in expensive.items():
        print(f"{item}: ₹{price}")
else:
    print("No items cost more than ₹100.")