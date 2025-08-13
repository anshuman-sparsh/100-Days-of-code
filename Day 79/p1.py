def add_numbers(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    print("--- Demonstrating Function Type Hints ---")

    
    correct_result = add_numbers(10, 20)
    print(f"Result of add_numbers(10, 20): {correct_result}")

    print("\n--- Mypy will flag the following examples as errors ---")

    # Mypy Error 
    print("Calling with strings would cause a mypy error.")
    
    # Mypy Error
    incorrect_float_result = add_numbers(5.5, 4.5)
    print(f"Calling with floats (5.5, 4.5) returns: {incorrect_float_result}")