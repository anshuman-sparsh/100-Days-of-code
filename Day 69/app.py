from flask import Flask, render_template, request, redirect, url_for
import random
import json

app = Flask(__name__)

def get_random_city_and_fact():
    with open("facts.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    random_city_data = random.choice(data)
    city_name = random_city_data["city_name"]
    random_fact = random.choice(random_city_data["facts"])
    
    return city_name, random_fact

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect(url_for('index'))
    
    city, fact = get_random_city_and_fact()
    return render_template("index.html", city=city, fact=fact)

if __name__ == "__main__":
    app.run(debug=True)