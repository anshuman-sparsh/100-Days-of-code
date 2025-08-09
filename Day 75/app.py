import sqlite3
import os
from flask import Flask, render_template, request, url_for, redirect, flash

# --- App Configuration ---
app = Flask(__name__)
# A secret key is required for using flash messages
app.config['SECRET_KEY'] = 'your_super_secret_key_12345'
app.config['DATABASE'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'blog.db')

# --- Database Functions ---
def get_db():
    """Opens a new database connection if there is none yet for the current request."""
    db = sqlite3.connect(app.config['DATABASE'])
    db.row_factory = sqlite3.Row
    return db

def get_post(post_id):
    """Gets a single post by its ID."""
    db = get_db()
    post = db.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    db.close()
    return post

# --- Database Initialization ---
@app.cli.command('init-db')
def init_db_command():
    """Defines the `flask init-db` terminal command to set up the database."""
    db = sqlite3.connect(app.config['DATABASE'])
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()
    print('Initialized the database.')

# --- Routes ---
@app.route('/')
def index():
    """READ: Renders the main page with all blog posts from the database."""
    db = get_db()
    posts = db.execute('SELECT * FROM posts ORDER BY created_at DESC').fetchall()
    db.close()
    return render_template('index.html', posts=posts)

@app.route('/create', methods=('GET', 'POST'))
def create():
    """CREATE: Adds a new post to the database."""
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!', 'danger')
        elif not content:
            flash('Content is required!', 'danger')
        else:
            db = get_db()
            db.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
            db.commit()
            db.close()
            flash('Post created successfully!', 'success')
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):
    """UPDATE: Edits an existing post."""
    post = get_post(id)

    if post is None:
        flash('Post not found.', 'danger')
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!', 'danger')
        elif not content:
            flash('Content is required!', 'danger')
        else:
            db = get_db()
            db.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (title, content, id))
            db.commit()
            db.close()
            flash('Post updated successfully!', 'info')
            return redirect(url_for('index'))

    return render_template('update.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    """DELETE: Removes a post from the database."""
    post = get_post(id)
    if post:
        db = get_db()
        db.execute('DELETE FROM posts WHERE id = ?', (id,))
        db.commit()
        db.close()
        flash('Post was successfully deleted.', 'success')
    else:
        flash('Post not found.', 'danger')
        
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)