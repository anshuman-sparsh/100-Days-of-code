# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Mood to playlist mapping
mood_data = {
    "happy": {
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DX0UrRvztWcAU?si=dfd84a0d46be4cb2",
        "quote": "Keep smiling! 😊",
        "emoji": "😄"
    },
    "sad": {
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1EIhmSBwUDxg84?si=197b6897911145d9",
        "quote": "This too shall pass.",
        "emoji": "😢"
    },
    "motivated": {
        "playlist": "https://open.spotify.com/playlist/5wV33ZjypNwpSjRgyob2TZ?si=e473fa14d6684798",
        "quote": "Push yourself, because no one else will.",
        "emoji": "🔥"
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/playlist', methods=['POST'])
def playlist():
    mood = request.form.get('mood')
    data = mood_data.get(mood, {})
    return render_template('result.html', mood=mood, data=data)

if __name__ == '__main__':
    app.run(debug=True)
