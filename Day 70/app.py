from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# File paths
WATCHLIST_FILE = 'Day 70/data/watchlist.txt'
WATCHEDLIST_FILE = 'Day 70/data/watchedlist.txt'

# Ensure data folder exists
os.makedirs('data', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/watchlist')
def watchlist():
    with open(WATCHLIST_FILE, 'r') as f:
        movies = f.readlines()
    return render_template('watchlist.html', movies=[m.strip() for m in movies])

@app.route('/watchedlist')
def watchedlist():
    with open(WATCHEDLIST_FILE, 'r') as f:
        movies = f.readlines()
    return render_template('watchedlist.html', movies=[m.strip() for m in movies])

@app.route('/add_to_watchlist', methods=['POST'])
def add_to_watchlist():
    movie = request.form.get('movie')
    if movie:
        with open(WATCHLIST_FILE, 'a') as f:
            f.write(movie + '\n')
    return redirect(url_for('watchlist'))

@app.route('/add_to_watched', methods=['POST'])
def add_to_watched():
    movie = request.form.get('movie')
    if movie:
        with open(WATCHEDLIST_FILE, 'a') as f:
            f.write(movie + '\n')
    return redirect(url_for('watchedlist'))

if __name__ == '__main__':
    app.run(debug=True)
