from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

db.create_all()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

class Goals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.Integer)
    goal = db.Column(db.Text)
    cost = db.Column(db.Integer)

class NetWorth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.Integer)
    description = db.Column(db.Text)
    amount = db.Column(db.Integer)
    category = db.Column(db.Text)

class WeeklyExpenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.Integer)
    description = db.Column(db.Text)
    amount = db.Column(db.Integer)
    category = db.Column(db.Text)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))