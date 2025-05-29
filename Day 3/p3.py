# 🔹 3. Palindrome Checker
# Take a string input from the user.
# Check if the string is a palindrome (same forward and backward).
# Ignore case and spaces.







text = input("Enter any Word: ")
print()


def is_palindrome(text):
    new_text = text.lower().replace(" ", "")
    return new_text == new_text[::-1]



if is_palindrome(text):
    print(f"{text} is a palindrome!")
else:
    print(f"{text} is NOT a palindrome.")

