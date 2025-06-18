# 🔹 5. Student Registry
# Maintain a class variable list of all student names created.
# Use @classmethod to print all registered students.




class Student:
    all_students = []

    def __init__(self, name):
        self.name = name
        Student.all_students.append(name)

    @classmethod
    def show_all(cls):
        print("Registered Students:")
        for name in cls.all_students:
            print(f"{name}")

Student("Rohit")
Student("Mohit")
Student("Badal")
Student.show_all()
