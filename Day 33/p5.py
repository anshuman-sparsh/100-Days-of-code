# 🔹 5. Even/Odd Table Generator
# 📌 Ask user for a range (start to end).
# ✅ Use: is_even(n), generate_table(start, end)
# Print each number and whether it’s Even or Odd.




def is_even(n):
    return n % 2 == 0

def generate_table(start, end):
    print("\n Even/Odd Table")
    for num in range(start, end + 1):
        status = "Even" if is_even(num) else "Odd"
        print(f"{num} → {status}")


try:
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    if start > end:
        print("Start should be less than or equal to end.")
    else:
        generate_table(start, end)
except ValueError:
    print("Please enter valid integers.")
