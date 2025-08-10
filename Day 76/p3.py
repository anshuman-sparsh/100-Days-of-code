from contextlib import contextmanager

@contextmanager
def suppress_errors():
    try:
        yield
    except Exception as e:
        print(f"Error suppressed. (Details: {e})")

# Example 1: Code runs without any errors
print("--- Running block 1 (No Error) ---")
with suppress_errors():
    print("This code is running successfully.")
    x = 10 + 5
    print(f"Result: {x}")
print("...Script continues after block 1.\n")


# Example 2: Code raises a ZeroDivisionError
print("--- Running block 2 (With Error) ---")
with suppress_errors():
    print("This code will try to divide by zero.")
    y = 10 / 0
    print("This message will not appear.")
print("...Script continues after block 2 because the error was suppressed.")