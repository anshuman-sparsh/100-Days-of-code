# 🔹 4.
# Read the file line-by-line and print line numbers along with each line.



with open("Day 15/notes.txt") as f:
    Line_1 = f.readline()
    Line_2 = f.readline()
    Line_3 = f.readline()
    Line_4 = f.readline()
    print(f"Line 1:{Line_1}")
    print(f"Line 2:{Line_2}")
    print(f"Line 3:{Line_3}")
    print(f"Line 4:{Line_4}\n")