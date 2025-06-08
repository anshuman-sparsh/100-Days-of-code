# 🔹 2.
# Create a calculator function that handles division and returns "Cannot divide by zero" if the second input is 0.





numA = float(input("Enter number A from (A/B): "))
numB = float(input("Enter number B from (A/B): "))


def divide_calculator(numA,numB):
   try:
      result = numA/numB
      print(f"The result is {result}.")

   except ZeroDivisionError:
      return "Cannot Divide By Zero."

print(divide_calculator(numA,numB))