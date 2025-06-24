# 🔹 4. Feedback Form (POST only)
# Route: /feedback
# Ask for name and feedback (textarea)
# On submit, save feedback to a feedback.txt file




from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        comment = request.form.get('feedback')

        with open('Day 29/feedback.txt', 'a') as f:
            f.write(f'Name: {name}\nFeedback: {comment}\n---\n')

        return f"Thank you {name} for your feedback!"

    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)

# python "Day 29/app4.py"
# http://127.0.0.1:5000/feedback