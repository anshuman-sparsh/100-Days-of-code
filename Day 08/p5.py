# 🔹 5. Guess the Number Game
# 📌 Objective:
# Create a basic number guessing game.
# 🧾 Instructions:
# Define a secret number inside the program (e.g., secret = 7)
# Let the user guess the number — allow max 3 tries
# Create a function check_guess(guess, secret) that:
# Returns "Too high", "Too low" or "Correct!"
# Use a while or for loop to give the user up to 3 chances
# End the game if they guess correctly




secret = 9

def check_guess(guess,secret):
    if guess == secret:
        return "Correct!"
    elif guess > secret:
        return "Too High"
    elif  guess < secret:
        return "Too Low"
    
for attempt in range(3):
    guess = int(input(f"Attempt {attempt + 1}/3. Guess the number: "))
    result = check_guess(guess, secret)
    print(result)
    if result == "Correct!":
        break

if result != "Correct!":
    print(f"Game over! The number was {secret}.")
