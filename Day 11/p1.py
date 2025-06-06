# 🔹 1.
# Write a function that filters out all even numbers from a list.




numbers = input("Enter Numbers: ")
numbers_list = numbers.split()

def even_filter(numbers):
    even_numbers = []
    for num in numbers:
        if num.isdigit():
            number = int(num)
            if number % 2 == 0:
                even_numbers.append(number)
    return even_numbers

print(even_filter(numbers_list))