# 🔹 5. Dropdown Interest Form
# Route: /interests
# Form: Name + dropdown with options (Python, ML, Web, DSA)
# Show result: Thanks Anshuman! You’re interested in Web.




from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/interest', methods=['GET', 'POST'])
def interests():
    if request.method == 'POST':
        name = request.form.get('name')
        interest = request.form.get('interest')
        return f"Thanks {name}! You are interested in {interest}."
    return render_template('interest.html')

if __name__ == '__main__':
    app.run(debug=True)

# python "Day 29/app5.py"
# http://127.0.0.1:5000/interest