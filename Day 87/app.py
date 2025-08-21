import os
from datetime import date, timedelta, datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'habits.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'

db = SQLAlchemy(app)

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    completions = db.relationship('Completion', backref='habit', lazy=True, cascade="all, delete-orphan")

class Completion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)

@app.route("/")
def index():
    today_str = date.today().strftime("%Y-%m-%d")
    return redirect(url_for("view_date", date_string=today_str))

@app.route("/view/<date_string>")
def view_date(date_string):
    try:
        view_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD.", 400

    habits = Habit.query.all()
    completions = Completion.query.filter_by(date=view_date).all()
    completed_habit_ids = {c.habit_id for c in completions}

    prev_date = view_date - timedelta(days=1)
    next_date = view_date + timedelta(days=1)

    return render_template(
        "index.html",
        habits=habits,
        completed_habit_ids=completed_habit_ids,
        view_date=view_date,
        prev_date=prev_date,
        next_date=next_date
    )

@app.route("/toggle/<int:habit_id>/<date_string>", methods=["POST"])
def toggle(habit_id, date_string):
    view_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    completion = Completion.query.filter_by(date=view_date, habit_id=habit_id).first()

    if completion:
        db.session.delete(completion)
    else:
        new_completion = Completion(date=view_date, habit_id=habit_id)
        db.session.add(new_completion)
    
    db.session.commit()
    return redirect(url_for("view_date", date_string=date_string))

@app.route("/add_habit", methods=["POST"])
def add_habit():
    habit_name = request.form.get("habit_name")
    date_string = request.form.get("date")

    if habit_name:
        new_habit = Habit(name=habit_name)
        db.session.add(new_habit)
        db.session.commit()
    
    return redirect(url_for("view_date", date_string=date_string))

@app.route("/delete_habit/<int:habit_id>", methods=["POST"])
def delete_habit(habit_id):
    date_string = request.form.get("date")
    habit_to_delete = Habit.query.get(habit_id)

    if habit_to_delete:
        db.session.delete(habit_to_delete)
        db.session.commit()
    
    return redirect(url_for("view_date", date_string=date_string))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if not Habit.query.first():
            sample_habits = [Habit(name="Exercise"), Habit(name="Read"), Habit(name="Meditate")]
            db.session.bulk_save_objects(sample_habits)
            db.session.commit()
    app.run(debug=True)