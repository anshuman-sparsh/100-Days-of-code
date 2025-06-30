# Formatted Invoice Generator


item = input("Enter item name: ")
qty = int(input("Enter quantity: "))
price = float(input("Enter price per unit: "))

total = qty * price

print("\n🧾 Invoice:")
print(f"{'Item':<12}{'Qty':<8}{'Price':<10}{'Total':<10}")
print(f"{item:<12}{qty:<8}{price:<10.2f}{total:<10.2f}")
