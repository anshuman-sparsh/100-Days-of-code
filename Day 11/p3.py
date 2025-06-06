# 🔹 3.
# Write a function that takes a list of numbers and returns the average of only the positive numbers.




numbers = input("Enter Numbers: ")

def average_positive(numbers):
  converted_numbers = []
  num = []
  for x in numbers.split():
    num.append(float(x))
  for digit in num:
      if digit > 0:
         converted_numbers.append(digit)



  if len(converted_numbers) > 0:
      length = len(converted_numbers)
      total = sum(converted_numbers)
      average = total/length
      print(f"Average of positive numbers are: {average}")
  else:
        print("No positive numbers are found.")

average_positive(numbers)
       





