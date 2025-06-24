# 🔹 2. Flask BMI Calculator
# Route: /bmi
# Form input: weight (kg) and height (cm)
# Calculate BMI and show result after form submit









from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    bmi_result = None
    if request.method == 'POST':
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height')) / 100  # convert cm to meters
        bmi_result = round(weight / (height ** 2), 2)
    return render_template('bmi.html', bmi=bmi_result)

if __name__ == '__main__':
    app.run(debug=True)


# python "Day 29/app2.py"
# http://127.0.0.1:5000/bmi