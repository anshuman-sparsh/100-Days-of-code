import string
import random

def generate_password(length):
    if length < 4:
        return None

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    
    all_characters = lowercase + uppercase + digits + punctuation
    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation)
    ]
    
    for _ in range(length - 4):
        password.append(random.choice(all_characters))
        
    random.shuffle(password)
    
    return "".join(password)

def main():
    print("--- Secure Password Generator ---")
    try:
        desired_length = int(input("Enter the desired password length (min 8 recommended): "))

        if desired_length < 8:
            print("Warning: A password length of at least 8 is recommended for better security.")
        
        password = generate_password(desired_length)

        if password:
            print(f"Generated Password: {password}")
        else:
            print("Password length is too short. Must be at least 4.")

    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()