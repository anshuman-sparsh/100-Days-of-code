from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

# Load quotes from JSON
with open("quotes.json") as f:
    quotes_data = json.load(f)

# Mood to Playlist Mapping
mood_map = {
    "happy": {
        "playlist": "https://open.spotify.com/playlist/happy",
        "emoji": "😄"
    },
    "sad": {
        "playlist": "https://open.spotify.com/playlist/sad",
        "emoji": "😢"
    },
    "motivated": {
        "playlist": "https://open.spotify.com/playlist/motivated",
        "emoji": "🔥"
    },
    "chill": {
        "playlist": "https://open.spotify.com/playlist/chill",
        "emoji": "🌴"
    }
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/playlist", methods=["POST"])
def playlist():
    mood = request.form.get("mood")
    if mood in mood_map:
        playlist = mood_map[mood]["playlist"]
        emoji = mood_map[mood]["emoji"]
        quote = random.choice(quotes_data.get(mood, ["Stay strong!"]))
        return render_template("result.html", mood=mood, emoji=emoji, quote=quote, playlist=playlist)
    else:
        return "Mood not found", 404

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
