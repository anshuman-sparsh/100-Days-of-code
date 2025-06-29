# 🔹 1. Contact Form Handler
# 📌 Route: /contact
# 🧾 Show an HTML form with fields: Name, Email, Message
# ➡️ When user submits → show thank you page with their name.




from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/contact", methods = ["GET" , "POST"])

def contact():
    if request.method == "POST":
        name = request.form.get("name")
        return render_template("thank-you.html", name = name)
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

# python "Day 34/app1.py"
# http://127.0.0.1:5000/contact