# 🔹 1. Max of 3 Numbers
# 📌 Objective:
# Write a function that takes 3 numbers and returns the largest.
# 🧾 Instructions:
# Ask the user to input 3 numbers
# Pass these numbers to a function max_of_three(a, b, c)
# The function should return the greatest number
# Print the returned result





a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

def max_of_three(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= c and b >=  a:
        return b
    elif c >= a and c >= b:
        return c
    

max_number = max_of_three(a,b,c)
print(f"The greatest No is: {max_number}")