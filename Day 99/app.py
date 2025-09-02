from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    """
    Sets up the game board by creating and shuffling card pairs,
    then renders the main game page.
    """
    # Define the symbols/values for the cards
    symbols = ["Cat", "Dog", "Pig", "Cow", "Sun", "Moon", "Star", "Tree",]
    
    # Create a list with two of each symbol
    cards = symbols * 2
    
    # Shuffle the cards randomly
    random.shuffle(cards)
    
    # Render the template, passing the shuffled card list
    return render_template("index.html", cards=cards)

if __name__ == "__main__":
    app.run(debug=True)