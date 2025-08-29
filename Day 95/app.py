from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
# A secret key is required to use sessions securely.
app.secret_key = 'a-super-secret-key-that-is-hard-to-guess'

@app.route("/")
def index():
    """Initializes the game and shows the main page."""
    # If a secret number isn't already in the session, create one.
    if 'secret_number' not in session:
        session['secret_number'] = random.randint(1, 100)
    
    # Render the main game page.
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    """Handles the user's guess and provides feedback."""
    message = ""
    try:
        user_guess = int(request.form['guess'])
        secret_number = session.get('secret_number')
        
        if user_guess < secret_number:
            message = "Too low! Try again."
        elif user_guess > secret_number:
            message = "Too high! Try again."
        else:
            message = f"Correct! The number was {secret_number}. Great job!"
            session.pop('secret_number', None)
            
    except (ValueError, KeyError):
        message = "Please enter a valid number."
        
    return render_template("index.html", message=message)

@app.route("/reset")
def reset():
    """Starts a new game by clearing the session."""
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)