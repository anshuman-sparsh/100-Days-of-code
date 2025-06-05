# 🔹 3. Bill Splitter
# Ask the user for the total bill amount and the number of people to split it with.
# Calculate how much each person should pay and print the result rounded to 2 decimal places.






total_bill_amount = float(input("Enter total amount: "))
No_of_people = int(input("Enter No of people to split: "))

pay = total_bill_amount/No_of_people

print("Each person should pay ₹",round(pay, 2))