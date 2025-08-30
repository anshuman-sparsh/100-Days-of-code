import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'codefolio.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'a-super-secret-key-for-sessions'

db = SQLAlchemy(app)

# --- Database Models ---
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    projects = db.relationship('Project', backref='owner', lazy=True, cascade="all, delete-orphan")

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    tech_used = db.Column(db.String(200), nullable=False)
    github_link = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# --- Routes ---
@app.route("/")
def index():
    return render_template("index.html")

# --- Temporary Preview Routes ---
@app.route("/portfolio-preview")
def portfolio_preview():
    # Placeholder data for designing the portfolio page
    user_data = {
        "username": "Anshu",
        "bio": "A passionate developer learning to build amazing web applications with Flask and Python."
    }
    projects_data = [
        {'title': 'Habit Tracker', 'description': 'A daily habit tracking application built with Flask.', 'tech_used': 'Python, Flask, SQLAlchemy', 'github_link': '#'},
        {'title': 'URL Shortener', 'description': 'A FastAPI service to shorten long URLs.', 'tech_used': 'Python, FastAPI, SQLite', 'github_link': '#'},
        {'title': 'NASA APOD Viewer', 'description': 'View the astronomy picture of the day.', 'tech_used': 'Flask, Requests API', 'github_link': '#'}
    ]
    return render_template("portfolio.html", user=user_data, projects=projects_data)

@app.route("/dashboard-preview")
def dashboard_preview():
    # Placeholder data for designing the dashboard
    projects_data = [
        {'id': 1, 'title': 'Habit Tracker'},
        {'id': 2, 'title': 'URL Shortener'},
    ]
    return render_template("dashboard.html", projects=projects_data)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)