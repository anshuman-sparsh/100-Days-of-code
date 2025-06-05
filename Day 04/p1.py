# 🔹 1. Grocery List App
# Ask the user to enter 5 grocery items (one by one)
# Store them in a list
# Print the final list at the end




grocery_list =[]
print("Grocery list app(upto 5 items)")

add_item1 =input("Enter 1st item to add: ")
add_item2 =input("Enter 2st item to add: ")
add_item3 =input("Enter 3rd item to add: ")
add_item4 =input("Enter 4th item to add: ")
add_item5 =input("Enter 5th item to add: ")

grocery_list.append(add_item1)
grocery_list.append(add_item2)
grocery_list.append(add_item3)
grocery_list.append(add_item4)
grocery_list.append(add_item5)

print(grocery_list)