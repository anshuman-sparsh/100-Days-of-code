# 🔹 2. Simple Login Form
# 📌 Route: /login
# 🧾 Form with username and password → POST → validate (admin/1234)
# ➡️ Show “Login Success” or “Invalid Credentials”




from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            message = "Login Success"
        else:
            message = "Invalid Credentials"
    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)



# python "Day 34/app2.py"
# http://127.0.0.1:5000/login
