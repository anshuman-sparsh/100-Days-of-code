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
    return api_key in VALID_KEYS.values()

@app.route("/api/quote", methods=["GET"])
def get_random_quote():
    api_key = request.headers.get("X-API-Key")
    
    if api_key and is_key_valid(api_key):
        quote_id, quote_text = random.choice(list(QUOTES.items()))
        return jsonify({"id": quote_id, "quote": quote_text})
    else:
        return jsonify({"error": "Invalid or missing API Key"}), 401

if __name__ == "__main__":
    app.run(debug=True)

# Run: python p3.py -> Test in terminal(powershell): curl http://127.0.0.1:5000/api/quote -Headers @{"X-API-Key" = "key123"}
