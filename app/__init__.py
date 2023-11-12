import os
from flask import Flask

from app.config import config
from app.init_db import ConnDB

db_conn = ConnDB()

def create_app(config_name):
    """Create App Function for Flask Config and blueprint initialization"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    from app.main import main
    from app.auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)

    config[config_name].init_app() # initialize configurations
    db_conn.init_app()

    return app
