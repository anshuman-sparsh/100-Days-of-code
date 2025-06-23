# 🔹 3. Add Numbers via URL
# URL: /add?a=10&b=5
# Output: Sum = 15
# Handle both integers via URL query




from flask import Flask, request

app = Flask(__name__)

@app.route("/add")
def add():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    if a is None or b is None:
        return "Please provide both 'a' and 'b' as integers in the URL."
    result = a + b
    return f"Sum = {result}"

if __name__ == "__main__":
    app.run(debug=True)

# python "Day 28/p3.py"
# http://127.0.0.1:5000/add?a=10&b=5
