import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# --- App Configuration ---
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'codefolio.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'a-super-secret-key-for-sessions'

# --- Database Initialization ---
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

# --- Authentication Routes ---
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user:
            flash("Username already exists.", "warning")
            return redirect(url_for("register"))
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created! Please log in.", "success")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            flash("Logged in successfully!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password.", "danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))

# --- Dashboard & Project Management ---
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user_id" not in session:
        flash("You need to be logged in to access this page.", "warning")
        return redirect(url_for("login"))
    
    user_id = session["user_id"]

    # --- ADD PROJECT LOGIC (POST) ---
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        tech_used = request.form.get("tech_used")
        github_link = request.form.get("github_link")

        if title and description and tech_used and github_link:
            new_project = Project(
                title=title,
                description=description,
                tech_used=tech_used,
                github_link=github_link,
                user_id=user_id
            )
            db.session.add(new_project)
            db.session.commit()
            flash("Project added successfully!", "success")
        else:
            flash("All fields are required.", "warning")
        return redirect(url_for("dashboard"))

    # --- VIEW DASHBOARD LOGIC (GET) ---
    projects = Project.query.filter_by(user_id=user_id).order_by(Project.id.desc()).all()
    return render_template("dashboard.html", projects=projects)

# --- NEW: Public Portfolio Route ---
@app.route("/portfolio/<username>")
def portfolio(username):
    # Find the user by their username, return 404 if not found
    user = User.query.filter_by(username=username).first_or_404()
    
    # The projects are automatically available via the 'backref'
    # projects = user.projects 
    
    return render_template("portfolio.html", user=user, projects=user.projects)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)