# 🔹 3. Min-Max Finder
# Create a function that takes three numbers and returns the smallest and largest.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))



def find_min_max(a, b, c):
    if a >= b and a >= c:
        maximum = a
    elif b >= c:
        maximum = b
    else:
        maximum = c
    

    if a <= b and a <= c:
        minimum = a
    elif b <= c:
        minimum = b
    else:
        minimum = c
    
    return minimum, maximum  



mininum, maximum = find_min_max(a, b, c)  # We can use double variables too.
print(f"Smallest: {mininum}, Largest: {maximum}")