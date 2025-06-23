# 🔹 4. Simple HTML Render
# Create a route /html
# Return a small HTML page with a <h1> heading and a <p> paragraph



from flask import Flask

app = Flask(__name__)

@app.route("/html")
def html_page():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Simple HTML Page</title>
        </head>
        <body>
            <h1>Welcome to Flask</h1>
            <p>This is a simple HTML page served with Flask.</p>
        </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(debug=True)
# python "Day 28/p4.py" :- In Terminal First
# http://127.0.0.1:5000/html :- Then in browser

