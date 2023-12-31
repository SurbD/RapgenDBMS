from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

from app.config import config
from app.init_db import ConnDB

db_conn = ConnDB()
db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    """Create App Function for Flask Config and blueprint initialization"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    config[config_name].init_app() # initialize configurations
    db_conn.init_app()
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from app.auth import auth
    from app.main import main
    from app.api import api
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(api)

    return app
