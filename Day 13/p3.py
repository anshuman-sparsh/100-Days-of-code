# 🔹 3.
# Ask the user for a list of comma-separated numbers. Catch any value that is not a valid number and ignore it during sum calculation.




numbers_input = input("Enter comma-separated numbers: ").split(",")


def total_sum(numbers_input):
      numbers_list = []
      for num in numbers_input:
       try:
        numbers_list.append(float(num.strip()))
       except ValueError:
        continue
       
      if numbers_list:
        return sum(numbers_list)
      else:
        return 0

print("Total Sum:", total_sum(numbers_input))