def is_balanced(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False  # No opening for this closing
            stack.pop()

    return len(stack) == 0  # Should be empty if all matched

print(is_balanced("(()())")) 
print(is_balanced("(())(()"))    
