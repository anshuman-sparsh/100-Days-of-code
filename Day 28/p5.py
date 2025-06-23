# 🔹 5. Error Handling Route
# Create a route /divide?a=10&b=0
# Catch division-by-zero and return a friendly message




from flask import Flask, request

app = Flask(__name__)

@app.route("/divide")
def divide():
    try:
        a = int(request.args.get("a"))
        b = int(request.args.get("b"))
        result = a / b
        return f"Result of division: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except (TypeError, ValueError):
        return "Error: Please provide valid integers for a and b."

if __name__ == "__main__":
    app.run(debug=True)

# python "Day 28/p5.py"
# http://127.0.0.1:5000/divide?a=10&b=2
