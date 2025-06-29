# 🔹 3. Feedback Collector
# 📌 Route: /feedback
# 🧾 Ask for user’s name, rating (1–5), and feedback text.
# ✅ After POST → store in a text file + show success message.





from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("name")
        rating = request.form.get("rating")
        comments = request.form.get("comments")

        with open("Day 34/feedback.txt", "a") as f:
            f.write(f"{name} | Rating: {rating} | Feedback: {comments}\n")

        return render_template("feedback_success.html", name=name)

    return render_template("feedback_form.html")

if __name__ == "__main__":
    app.run(debug=True)




# python "Day 34/app3.py"
# http://127.0.0.1:5000/feedback
