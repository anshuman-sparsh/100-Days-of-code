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

def get_user_from_key(api_key):
    for user, key in VALID_KEYS.items():
        if key == api_key:
            return user
    return None

@app.route("/")
def index():
    return jsonify({"message": "API is running. Use /api/quote or /api/me with a valid X-API-Key header."})

@app.route("/api/quote", methods=["GET"])
def get_random_quote():
    api_key = request.headers.get("X-API-Key")
    user = get_user_from_key(api_key)
    
    if user:
        quote_id, quote_text = random.choice(list(QUOTES.items()))
        return jsonify({"id": quote_id, "quote": quote_text})
    else:
        return jsonify({"error": "Invalid or missing API Key"}), 401

@app.route("/api/me", methods=["GET"])
def get_user_info():
    api_key = request.headers.get("X-API-Key")
    user = get_user_from_key(api_key)

    if user:
        return jsonify({"message": f"Welcome, {user}!"})
    else:
        return jsonify({"error": "Invalid or missing API Key"}), 401

if __name__ == "__main__":
    app.run(debug=True)

# Run: python p4.py -> Test in terminal(powershell): curl http://127.0.0.1:5000/api/me -Headers @{"X-API-Key" = "key456"}