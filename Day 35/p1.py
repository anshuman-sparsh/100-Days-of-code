# Report Card Formatter


name = input("Enter your name: ")
maths = int(input("Enter marks in Maths: "))
physics = int(input("Enter marks in Physics: "))
chemistry = int(input("Enter marks in Chemistry: "))


total = maths + physics + chemistry
average = total / 3


print("\n📋 Report Card")
print(f"{'Name:':<12}{name}")
print(f"{'Maths:':<12}{maths}")
print(f"{'Physics:':<12}{physics}")
print(f"{'Chemistry:':<12}{chemistry}")
print(f"{'Total:':<12}{total} | Average: {average:.2f}")
