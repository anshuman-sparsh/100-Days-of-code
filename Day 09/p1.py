# 🔹 1.
# Create a function that takes a number and returns whether it is even, odd, or zero.




number = int(input("Enter number: "))

def check_type(number):
    if number == 0 :
        return "It's Zero."
    elif number % 2 == 0:
        return "It's Even."
    else:
        return "It's Odd."
    

print(check_type(number))
        