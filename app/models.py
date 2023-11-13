from datatime import datetime

from app import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=True)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    joined = db.Column(db.DateTime(), default=datetime.utcnow)
    confirmed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<User(username={self.username}, joined={self.joined})"
