# 🔹 3. Score Grader
# Ask user to input scores of 4 subjects
# Average the scores
# Print the grade based on:
# 90+ = A
# 75–89 = B
# 60–74 = C
# Below 60 = D
# Use if/elif/else, lists, append(), sum(), len()





score_list = []

for i in range(4):
    scores = int(input(f"Enter Score of Sub {i+1}: "))
    score_list.append(scores)

average = sum(score_list)/len(score_list)

if average >= 90:
    print(f"Average: {average} Grade: A")
elif average >= 75 and average <= 89:
    print(f"Average: {average} Grade: B")
elif average >= 60 and average <= 74:
    print(f"Average: {average} Grade: C")
elif average <60:
    print(f"Average: {average} Grade: D")
else:
    print("Error")