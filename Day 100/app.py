from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'a-super-secret-key-for-the-hangman-game'

# --- Game Configuration ---
def load_words():
    with open("Day 100/words.txt", "r") as word_file:
        words = [word.strip().upper() for word in word_file.readlines()]
    return words

WORD_LIST = load_words()
MAX_WRONG_GUESSES = 6

# --- Game Routes ---
@app.route("/")
def index():
    if 'word' not in session:
        start_new_game()

    word_to_guess = session['word']
    guessed_letters = session['guessed_letters']
    wrong_guesses = session['wrong_guesses']
    
    # word display string (e.g., P _ T H _ N)
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in word_to_guess])
    
    # Check for win/loss conditions
    game_over = False
    message = ""
    if "_" not in display_word:
        game_over = True
        message = "You Win!"
    elif wrong_guesses >= MAX_WRONG_GUESSES:
        game_over = True
        message = f"Game Over! The word was {word_to_guess}."
        
    return render_template(
        "index.html", 
        display_word=display_word, 
        guessed_letters=guessed_letters,
        wrong_guesses=wrong_guesses,
        game_over=game_over,
        message=message
    )

@app.route("/guess", methods=["POST"])
def guess():
    guessed_letter = request.form.get("letter", "").upper()
    
    if 'word' in session and guessed_letter and len(guessed_letter) == 1 and guessed_letter.isalpha():
        if guessed_letter not in session['guessed_letters']:
            session['guessed_letters'].append(guessed_letter)
            session.modified = True # Mark session as modified
            
            if guessed_letter not in session['word']:
                session['wrong_guesses'] += 1
                
    return redirect(url_for("index"))

@app.route("/reset")
def reset_game():
    session.clear()
    return redirect(url_for("index"))

def start_new_game():
    session['word'] = random.choice(WORD_LIST)
    session['guessed_letters'] = []
    session['wrong_guesses'] = 0

if __name__ == "__main__":
    app.run(debug=True)