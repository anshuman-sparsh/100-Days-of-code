# 🔹 3. Calculator Class
# Add static method is_even(num) that checks if a number is even.
# Also create instance method to multiply two numbers.




class Calculator:
    @staticmethod
    def is_even(num):
        return num % 2 == 0

    def multiply(self, a, b):
        return a * b

print(Calculator.is_even(10))  

calculate = Calculator()
print(calculate.multiply(3, 4))     
