# 🔹 2. Rectangle Calculator
# Create rectangle_tool.py using:
# Rectangle class: takes length and width
# Accept --length and --width via CLI
# Add method to compute and print area and perimeter


import argparse 

class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def rectangular_area(self):
        result = self.length*self.width
        return f"Area of rectangle is {result}"
    def rectangular_perimeter(self):
        result = 2*(self.length + self.width)
        return f"Perimeter of rectangle is {result}"


parser = argparse.ArgumentParser(description="Rectangle calculator Tool")

parser.add_argument("--length",type=float, required=True, help="length of the rectangle")
parser.add_argument("--width",type=float, required=True, help="width of the rectangle")


args = parser.parse_args()

shape = rectangle(args.length, args.width)
print(shape.rectangular_area())
print(shape.rectangular_perimeter())
# python "Day 27/rectangle_tool.py" --length 4 --width 3