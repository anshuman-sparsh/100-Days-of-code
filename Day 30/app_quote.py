from flask import Flask, render_template
import random


app = Flask(__name__)

@app.route("/quote")
def quote():
    with open("Day 30/quotes.txt","r") as f:
         quotes = f.readlines()
    quote = random.choice(quotes).strip()
    return render_template("quote.html", quote=quote)

if __name__ == "__main__":
   app.run(debug=True)  
        
# python "Day 30/app_quote.py"
# http://127.0.0.1:5000/quote








