# 🔹 1. Course Registration Tool 
# Create a script course_reg.py with:
# Class Student with name, roll, course
# Accept values via command-line args: --name, --roll, --course
# Print:
# Student [name] (Roll: [roll]) has registered for [course]


import argparse 


class Student:
    def __init__(self, name, roll, course):
        self.name = name
        self.roll = roll
        self.course = course

    def register(self):
        print(f"Student {self.name} (Roll: {self.roll}) has registered for {self.course}.")


parser = argparse.ArgumentParser(description="Course Registration Tool")

parser.add_argument("--name", required=True, help="Name of the student")
parser.add_argument("--roll", required=True, help="Roll number of the student")
parser.add_argument("--course", required=True, help="Course to register")

args = parser.parse_args()

student = Student(args.name, args.roll, args.course)
student.register()
# python "Day 27/course_reg.py" --name Anshuman --roll 101 --course "Artificial Intelligence"