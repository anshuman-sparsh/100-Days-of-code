from typing import Callable, List

def apply_operation(numbers: List[int], op: Callable[[int], int]) -> List[int]:
    return [op(num) for num in numbers]

def square(x: int) -> int:
    return x * x

def double(x: int) -> int:
    return x * 2

if __name__ == "__main__":
    my_numbers = [1, 2, 3, 4, 5]
    print(f"Original list: {my_numbers}")

    squared_numbers = apply_operation(my_numbers, square)
    print(f"After applying 'square': {squared_numbers}")

    doubled_numbers = apply_operation(my_numbers, double)
    print(f"After applying 'double': {doubled_numbers}")

    incremented_numbers = apply_operation(my_numbers, lambda n: n + 1)
    print(f"After applying a lambda function (n + 1): {incremented_numbers}")