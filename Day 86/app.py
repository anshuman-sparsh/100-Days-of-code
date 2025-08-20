from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store habits
habits = [
    {"name": "Exercise for 20 mins", "done": False},
    {"name": "Read for 15 mins", "done": False},
    {"name": "Drink 8 glasses of water", "done": False}
]

@app.route("/")
def index():
    # Pass the enumerated list so we can get the index in the template
    return render_template("index.html", habits=enumerate(habits))

@app.route("/complete/<int:habit_id>", methods=["POST"])
def complete(habit_id):
    if 0 <= habit_id < len(habits):
        habits[habit_id]["done"] = True
    return redirect(url_for("index"))

@app.route("/undo/<int:habit_id>", methods=["POST"])
def undo(habit_id):
    if 0 <= habit_id < len(habits):
        habits[habit_id]["done"] = False
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)