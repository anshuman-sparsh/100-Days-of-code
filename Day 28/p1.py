# 🔹 1. Hello Web
# Create a Flask app with just one route / that displays:
# Welcome to Flask, Anshuman!




from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Flask, Anshuman!"

if __name__ == "__main__":
    app.run(debug=True)
# python "Day 28/p1.py"  :- run this in terminal
