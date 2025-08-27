def validate_docstring(docstring: str) -> bool:
    """
    Validates a docstring based on two rules:
    1. It must start with a capital letter.
    2. It must end with a period.
    """
    # The string is guaranteed to be non-empty, so we can safely access index 0.
    starts_with_capital = docstring[0].isupper()
    ends_with_period = docstring.endswith('.')
    
    return starts_with_capital and ends_with_period


if __name__ == "__main__":
    test_cases = [
        "This is a valid docstring.",
        "this is not valid.",
        "This is also not valid",
        "Valid.",
        "invalid.",
        "Invalid"
    ]

    for case in test_cases:
        is_valid = validate_docstring(case)
        print(f'"{case}" -> Valid: {is_valid}')