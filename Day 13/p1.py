# 🔹 1.
# Write a program that asks the user to input a number and prints its square, but catches any non-numeric input with an error message.




try:
    number = float(input("Enter a number to square: "))
    
    square = number ** 2
    print(f"The square of {number} is {square}")
    
except ValueError:
    print("Error: Please enter a valid number!")