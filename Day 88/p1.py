import random
from flask import Flask, jsonify

app = Flask(__name__)

QUOTES = {
    "quote1": "The only way to do great work is to love what you do. - Steve Jobs",
    "quote2": "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "quote3": "Strive not to be a success, but rather to be of value. - Albert Einstein",
}

@app.route("/api/quote", methods=["GET"])
def get_random_quote():
    quote_id, quote_text = random.choice(list(QUOTES.items()))
    return jsonify({"id": quote_id, "quote": quote_text})

if __name__ == "__main__":
    app.run(debug=True)

# Run: python p1.py -> Visit http://127.0.0.1:5000/api/quote