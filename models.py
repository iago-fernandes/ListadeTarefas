from app import db, app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140))
    complete = db.Column(db.Boolean)