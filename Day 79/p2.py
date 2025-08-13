# The type hint {str: int} describes a dictionary with string keys and integer values.

def calculate_average_score(scores: dict[str, int]) -> float:
    if not scores:
        return 0.0
    
    total = sum(scores.values())
    return total / len(scores)

if __name__ == "__main__":
    student_scores = {
        "Alice": 88,
        "Bob": 92,
        "Charlie": 78
    }
    average = calculate_average_score(student_scores)
    print(f"The average score is: {average:.2f}")

    # Mypy will flag this because the values are strings, not integers.
    invalid_scores = {"David": "A+", "Eve": "B-"}
    