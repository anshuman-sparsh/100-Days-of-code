import sqlite3
import os
from flask import Flask, render_template, request, url_for, redirect, g

# --- App Configuration ---
app = Flask(__name__)


app.config['DATABASE'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tasks.db')

# --- Database Functions ---
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()

# --- Database Initialization Command ---
def init_db():
    db = get_db()
    
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('init-db')
def init_db_command():
    init_db()
    print('Initialized the database.')

# --- Routes ---
@app.route('/')
def index():
    db = get_db()
    tasks = db.execute('SELECT id, title, status FROM tasks ORDER BY id DESC').fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    db = get_db()
    task_title = request.form['title']
    if task_title:
        db.execute('INSERT INTO tasks (title, status) VALUES (?, ?)', [task_title, 'pending'])
        db.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>')
def update(task_id):
    db = get_db()
    db.execute('UPDATE tasks SET status = ? WHERE id = ?', ['done', task_id])
    db.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    db = get_db()
    db.execute('DELETE FROM tasks WHERE id = ?', [task_id])
    db.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)