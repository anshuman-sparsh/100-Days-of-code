# 📘 Project Tasks 
# 🔹 1.
# Add a student name and their 3 subject marks.
# 🔹 2.
# Display all students with their marks.
# 🔹 3.
# Calculate and show average marks for a specific student.
# 🔹 4.
# Show class average across all students.
# 🔹 5.
# Display pass/fail status for each student (≥ 40 = pass).
# 🔹 6.
# Exit the program.


student_scores = {}

def add_student():
    n = int(input("Enter number of students: "))
    for i in range(1, n + 1):
        name = input(f"\nEnter Student Name {i}: ")
        maths = float(input("Maths: "))
        physics = float(input("Physics: "))
        chemistry = float(input("Chemistry: "))
        subject_marks = {
            "maths": maths,
            "physics": physics,
            "chemistry": chemistry
        }
        student_scores[name] = subject_marks

def display_all():
    for student, subjects in student_scores.items():
        print(f"{student}: {subjects}")

def average_student():
    name = input("Enter student name: ")
    if name in student_scores:
        marks = student_scores[name].values()
        avg = sum(marks) / len(marks)
        print(f"{name}'s average: {avg}")
    else:
        print("Student not found.")

def class_average():
    total = 0
    count = 0
    for marks in student_scores.values():
        total += sum(marks.values())
        count += len(marks)
    if count > 0:
        print("Class average:", total / count)
    else:
        print("No data.")

def pass_fail():
    for name, marks in student_scores.items():
        values = marks.values()
        status = "Pass" if all(m >= 40 for m in values) else "Fail"
        print(f"{name}: {status}")

while True:
    print("\n1. Add Student\n2. Display All students\n3. Student Average\n4. Class Average\n5. Pass/Fail\n6. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        display_all()
    elif choice == "3":
        average_student()
    elif choice == "4":
        class_average()
    elif choice == "5":
        pass_fail()
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
