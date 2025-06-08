# 🔹 4.
# Write a function that tries to open a file and read it. If the file doesn’t exist, return "File not found."


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"
    except PermissionError:
        return "Permission Denied"

filename = input("Enter file name: ").strip()
print(read_file(filename))
