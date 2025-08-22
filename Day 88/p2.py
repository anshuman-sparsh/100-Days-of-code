import random
from flask import Flask, jsonify, request

app = Flask(__name__)

QUOTES = {
    "quote1": "The only way to do great work is to love what you do. - Steve Jobs",
    "quote2": "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "quote3": "Strive not to be a success, but rather to be of value. - Albert Einstein",
}

VALID_KEYS = {
    "user1": "key123",
    "user2": "key456"
}

def is_key_valid(api_key):
    if api_key in VALID_KEYS.values():
        return True
    return False

@app.route("/api/quote", methods=["GET"])
def get_random_quote():
    quote_id, quote_text = random.choice(list(QUOTES.items()))
    return jsonify({"id": quote_id, "quote": quote_text})

if __name__ == "__main__":
    app.run(debug=True)

# Run: python p2.py -> This file adds the check function; test http://127.0.0.1:5000/api/quote