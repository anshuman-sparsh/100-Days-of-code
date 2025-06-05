# 🔹 4. Discount Calculator
# 📌 Objective:
# Calculate final price after discount.
# 🧾 Instructions:
# Ask user to input:
# Original price of an item
# Discount percentage (e.g., 20 for 20%)
# Create a function apply_discount(price, discount_percent)
# The function should return the discounted price
# Print the final price after discount




price = int(input("Enter Price: "))
discount_percent = int(input("Enter Discount percentage: "))

def apply_discount(price,discount_percent):
      if price < 0 or discount_percent < 0:
        return "Invalid input! Values cannot be negative."
      if discount_percent > 100:
        return "Invalid discount! Cannot be over 100%." 
      discounted_price = (discount_percent/100)*price
      final_price = (price - discounted_price)
      return final_price

final_price = apply_discount(price,discount_percent)
print(f"Final price: {final_price}")