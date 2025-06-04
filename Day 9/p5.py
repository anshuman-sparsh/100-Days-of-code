# 🔹 5. Leap Year Checker
# Create a function that checks if a year is a leap year or not, and returns the result.





year = int(input("Enter a year: "))

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False




if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")