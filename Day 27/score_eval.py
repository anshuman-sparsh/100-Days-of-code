# 🔹 3. Student Score Evaluator 
# Create score_eval.py:
# Accept a file path via --file (text file containing names and marks)
# Read the file line by line (Name, Score)
# Print only students with score ≥ 60

# 📝 Use a sample file like:

# Ravi, 70  
# Amit, 45  
# Sana, 90


import argparse
import os


parser = argparse.ArgumentParser(description="Student Score Evaluator")
parser.add_argument("--file", type=str, required=True, help="Path to the score file")
args = parser.parse_args()


if not os.path.exists(args.file):
    print("File does not exist!")
else:
    with open(args.file, "r") as f:
        print("Students who scored 60 or above:\n")
        for line in f:
            if "," in line:
                name, score = line.strip().split(",")
                score = int(score.strip())
                if score >= 60:
                    print(f"{name} scored {score}")
# python "Day 27/score_eval.py" --file "Day 27/scores.txt"