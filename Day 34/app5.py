# 🔹 5. Quote Submission App
# 📌 Route: /quote
# 🧾 Input name and quote → show all submitted quotes on the same page
# 📁 Save quotes to a .txt file.




from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/quote', methods=['GET', 'POST'])
def quote():
    if request.method == 'POST':
        name = request.form.get('name')
        quote = request.form.get('quote')
        
        if name and quote:
            with open('Day 34/quotes.txt', 'a') as f:
                f.write(f'{name}: "{quote}"\n')

    # Reading all quotes to display in quote.html
    quotes = []
    try:
        with open('Day 34/quotes.txt', 'r') as f:
            quotes = f.readlines()
    except FileNotFoundError:
        pass

    return render_template('quote.html', quotes=quotes)
if __name__ == "__main__":
    app.run(debug=True)


# python "Day 34/app5.py"
# http://127.0.0.1:5000/quote
