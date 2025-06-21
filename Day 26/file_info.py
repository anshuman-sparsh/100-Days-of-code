# 🔹 3. File Info Tool
# Take a file path and print:
# File name
# File size in KB
# Whether it exists
# Use os.path.exists() and os.path.getsize().




import argparse
import os

parser = argparse.ArgumentParser(description="Check file information.")
parser.add_argument("--path", required=True, help="Path to the file")

args = parser.parse_args()
file_path = args.path

if os.path.exists(file_path):
    file_name = os.path.basename(file_path)
    file_size_kb = os.path.getsize(file_path) / 1024
    print(f"File Name: {file_name}")
    print(f"File Size: {file_size_kb:.2f} KB")
    print("Status: File exists.")
else:
    print("Status: File does NOT exist.")


# python "Day 26/file_info.py" --path "C:/AS FILES/100-Days-of-code/Day 26/myfile.txt"