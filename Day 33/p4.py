# 🔹 4. Student Record System (Refactor Style)
# 📌 Input student name & marks in 3 subjects.
# ✅ Use: get_student_data(), calc_total(marks), display_summary(name, total)
# Output a short report.



def get_student_data():
    name = input("Enter student name: ")
    marks = []
    for i in range(1, 4):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)
    return name, marks

def calc_total(marks):
    return sum(marks)

def display_summary(name, total):
    print("\n Student Report")
    print(f"Name: {name}")
    print(f"Total Marks: {total}")
    print("Status:", "Pass " if total >= 100 else "Needs Improvement ")


name, marks = get_student_data()
total = calc_total(marks)
display_summary(name, total)
