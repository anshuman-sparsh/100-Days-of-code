from flask import Flask, render_template, request

# This is a WSGI application, and Gunicorn will be our WSGI server.
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        number_str = request.form.get("number")
        
        if number_str and number_str.lstrip('-').isdigit():
            number = int(number_str)
            if number % 2 == 0:
                result = f"The number {number} is Even."
            else:
                result = f"The number {number} is Odd."
        else:
            result = "Please enter a valid integer."
            
    return render_template("index.html", result=result)