from flask import Flask, render_template, request

# Flask is a WSGI application. It follows a synchronous request-response model.
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    # Check if the form was submitted
    if request.method == "POST":
        number_str = request.form.get("number")
        
        # Basic validation
        if number_str and number_str.isdigit():
            number = int(number_str)
            
            # The core logic
            if number % 2 == 0:
                result = f"The number {number} is Even."
            else:
                result = f"The number {number} is Odd."
        else:
            result = "Please enter a valid integer."
            
    # Render the same page, passing the result back to it
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)



# Run -> cd "Day 89/flask_app"
# then run -> python app.py