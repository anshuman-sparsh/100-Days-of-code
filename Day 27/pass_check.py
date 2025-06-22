# 🔹 4. Password Analyzer Tool 
# Create pass_check.py:
# Class Password with value as input
# Methods:
# is_strong() → length ≥ 8, mix of letters + digits
# show_strength() → print result
# Use --password as input from terminal.


import argparse

class Password:
    def __init__(self, value):
        self.value = value

    def is_strong(self):
        has_letters = any(char.isalpha() for char in self.value)
        has_digits = any(char.isdigit() for char in self.value)
        return len(self.value) >= 8 and has_letters and has_digits

    def show_strength(self):
        if self.is_strong():
            print("Password is strong.")
        else:
            print("Password is weak. Use 8+ characters with letters and digits.")

parser = argparse.ArgumentParser(description="Password Strength Checker")
parser.add_argument("--password", type=str, required=True, help="Password to check")
args = parser.parse_args()

p = Password(args.password)
p.show_strength()
# python "Day 27/pass_check.py" --password mypasssword56745
