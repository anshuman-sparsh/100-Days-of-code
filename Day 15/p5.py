# 🔹 5.
# Create a new file summary.txt that copies only the first 2 lines of notes.txt.



with open("Day 15/notes.txt") as f, open("Day 15/summary.txt", "w") as c:
    Line_1 = f.readline()
    Line_2 = f.readline()
    c.write(Line_1)
    c.write(Line_2)