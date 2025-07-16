def is_palindrome_number(n):
    return str(n) == str(n)[::-1]


print(is_palindrome_number(121))
print(is_palindrome_number(123))
