import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'rapgen super secret')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    RAPGENDBMS_MAIL_SUBJECT_PREFIX = "[RapgenDBMS] "
    RAPGENDBMS_MAIL_SENDER = "RapgenDBMS Admin <noreply@rapgenglobal>"

    @staticmethod
    def init_app():
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    # -- set test database URI
class ProductionConfig(Config):
    # Set Production Database URI
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
