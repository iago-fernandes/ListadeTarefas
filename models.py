from app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140))
    complete = db.Column(db.Boolean)