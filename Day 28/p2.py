# 🔹 2. Dynamic Greeting Route
# URL: /greet?name=Anshuman
# Show: Hello Anshuman!
# Use request.args.get('name')




from flask import Flask, request

app = Flask(__name__)


@app.route("/greet")
def greet():
    name = request.args.get("name")

    if name:
        return f"Hello {name}!"
    else:
        return "Hello, Stranger!"

if __name__ == "__main__":
    app.run(debug=True)

# python "Day 28/p2.py"  :- In terminal (First do this)
# http://127.0.0.1:5000/greet?name=Anshuman :- In browser (Then this)
# http://127.0.0.1:5000/greet :- In browser
