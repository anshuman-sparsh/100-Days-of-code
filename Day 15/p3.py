# 🔹 3.
# Append a new line to notes.txt without deleting the existing content.



with open("Day 15/notes.txt", "a") as f:
     f.write("\nThis is a new line without deleting the existing content.")