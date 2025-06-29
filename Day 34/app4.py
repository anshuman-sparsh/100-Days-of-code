# 🔹 4. Newsletter Signup Form
# 📌 Route: /subscribe
# 🧾 Create an HTML form to collect a user's name and email address.
# ✅ After form submission (POST), store the email in a .txt file and show a "Thanks for subscribing, [name]!" message on a new page.





from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/subscribe", methods=["GET", "POST"])
def subscribe():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        with open("Day 34/subscribers.txt", "a") as f:
            f.write(f"{name} | {email}\n")

        return render_template("thank_you.html", name=name)

    return render_template("subscribe_form.html")

if __name__ == "__main__":
    app.run(debug=True)



# python "Day 34/app4.py"
# http://127.0.0.1:5000/subscribe
