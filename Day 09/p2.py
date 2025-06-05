# 🔹 2. Grade Evaluator
# Write a function that accepts a score and returns a grade (A, B, C, or D) based on the range.




def evaluate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "Fail"  


score = int(input("Enter your score: "))
grade = evaluate_grade(score)
print(f"Your grade: {grade}")