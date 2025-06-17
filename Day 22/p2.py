# 🔹 2. Student Class
# Define a class Student with name, roll_no, and branch.
# Create multiple students and display their info.



class student:
    all_students = []
    
    def __init__(self, name, roll_no, branch):
        self.name = name
        self.roll_no = roll_no
        self.branch =branch
        student.all_students.append(self)
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll_no: {self.roll_no}")
        print(f"Branch: {self.branch}\n")

    @classmethod
    def display_all_students(cls):
        print("\n=== ALL Students ===")
        for student in cls.all_students:
            student.display_info()


student("Anshuman Sparsh", "CS101", "Computer Science")
student("Priya Sharma", "DS202", "Data Science")
student("Rohan Mehta", "AI303", "Artificial Intelligence")


student.display_all_students()