import jwt
import secrets
from datetime import datetime, timedelta, timezone
from flask_login import UserMixin
from flask import current_app

from app import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    joined = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    confirmed = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"<User(username={self.username}, joined={self.joined})"

    def get_confirmation_token(self, expiration=600):
        token = jwt.encode(
            {
                'user_id': self.id,
                'exp': datetime.now(tz=timezone.utc) + timedelta(seconds=expiration)
            },
            current_app.config['SECRET_KEY'],
            algorithm="HS256"
        )
        return token

    @staticmethod
    def confirm_token(token):
        try:
            data = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                leeway=timedelta(seconds=10),
                algorithms=["HS256"]
            )
        except Exception as error:
            # LOG ERROR
            return None
        if not (user_id:=data.get('user_id')):
            return None
        return User.query.get(user_id)

    def get_verification_code(self, expiration=600):
        verification_code = secrets.token_hex(3)

        token = jwt.encode(
            {
                "code": verification_code,
                "user_id": self.id,
                "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=expiration)
            },
            current_app.config['SECRET_KEY'],
            algorithm="HS256"
        )

        token_data = {
            "token": token,
            "verification_code": verification_code
        }
        return token_data

    @staticmethod
    def confirm_code(token, verification_code):
        try:
            data = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                leeway=timedelta(seconds=10),
                algorithms=['HS256']
            )
        except Exception as error:
            # Log error
            return None
        if data['code'] == verification_code:
            return User.query.get(data['user_id'])
        return None
