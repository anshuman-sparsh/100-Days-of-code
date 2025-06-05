# 🔹 4. Multiplication Table Generator
# Ask the user for a number, then print its multiplication table from 1 to 10 using a for loop.




n = int(input("Enter a number to generate its multiplication table: "))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")