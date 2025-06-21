# 🔹 4. Random Password Generator
# Take a --length argument and generate a password using random and string modules.






import argparse
import random
import string

parser = argparse.ArgumentParser(description="Generate a random password.")
parser.add_argument("--length", type=int, required=True, help="Length of the password")

args = parser.parse_args()
length = args.length

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(characters, k=length))

print("Your Password:", password)


# python "Day 26/password_generator.py" --length 8