# 🔹 1. BMI Calculator
# Write a Python program that asks the user for their height (in meters) and weight (in kilograms), 
# and then calculates their BMI using the formula.
# Display the result rounded to 2 decimal places.



height = float(input("Enter your height(in meters): "))
weight = float(input("Enter your weight(in kilograms): "))

BMI = (weight/(height*height))

print("Your BMI is:", round(BMI, 2))