# 🔹 1. Greeting Tool
# Create a script that takes a name via --name and prints a greeting.
# Example: python greet.py --name Anshuman → Hello, Anshuman!




import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple greeting tool")
    parser.add_argument("--name", required=True, help="Enter your name")
    args = parser.parse_args()

    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()

# For this specific file program I should use this command - python "Day 26/greet.py" --name Anshuman
 
