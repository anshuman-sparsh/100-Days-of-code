# 🔹 2.
# Write a function that takes a dictionary of student names and scores, and returns all names with scores above 80.


scores_dict = {}

for i in range(1,3):
        name = input(f"Enter Name {i}: ")
        score = float(input(f"Enter Score {i}: "))
        scores_dict[name] = score

def high_scorers(scores_dict):
        print("High scorers(80+): ")
        for name,score in scores_dict.items():
                if score>80:
                  print(f"{name}: {score}")
     


high_scorers(scores_dict)