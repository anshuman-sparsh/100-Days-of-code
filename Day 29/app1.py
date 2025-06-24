# 🔹 1. Flask Form – Greet User
# Route: /form
# Display a form asking for name and age
# After submit, show:
# "Hello Anshuman! You are 20 years old."




from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        return render_template('greet.html', name=name, age=age)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)


# python "Day 29/app1.py"
# http://127.0.0.1:5000/form