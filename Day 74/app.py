from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# In-memory "database" as a list of post dictionaries
posts = [
    {
        'title': 'Welcome to My Micro-Blog!',
        'content': 'This is the first post, created directly in the Python code.'
    },
    {
        'title': 'About Flask',
        'content': 'Flask is a lightweight web framework that makes it easy to build web applications in Python.'
    }
]

@app.route('/')
def index():
    """
    This is the homepage route.
    It renders the index.html template, passing the list of posts to it.
    """
    return render_template('index.html', posts=posts)


@app.route('/create', methods=('GET', 'POST'))
def create():
    """
    This route handles the creation of a new post.
    If the request is GET, it shows the form.
    If the request is POST, it processes the form data and adds a new post.
    """
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if title and content:
            # Append the new post to in-memory list
            posts.append({'title': title, 'content': content})
            # Redirecting the user back to the homepage
            return redirect(url_for('index'))

    
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)