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
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DX0UrRvztWcAU?si=dfd84a0d46be4cb2",
        "emoji": "😄"
    },
    "sad": {
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1EIhmSBwUDxg84?si=197b6897911145d9",
        "emoji": "😢"
    },
    "motivated": {
        "playlist": "https://open.spotify.com/playlist/5wV33ZjypNwpSjRgyob2TZ?si=e473fa14d6684798",
        "emoji": "🔥"
    },
    "chill": {
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1EVHGWrwldPRtj?si=082d81379f864ba9",
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
