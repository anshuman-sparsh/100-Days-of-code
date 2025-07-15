def reverse_string(s):
    stack = list(s)
    reversed_str = ""

    while stack:
        reversed_str += stack.pop()

    return reversed_str

# Test case
print(reverse_string("hello")) 
