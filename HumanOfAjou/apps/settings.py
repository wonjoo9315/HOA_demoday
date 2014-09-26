"""
settings.py

Configuration for Flask app

"""


class Config(object):
    # Set secret key to use session
    SECRET_KEY = "likelion-flaskr-secret-key"
    debug = False


class Production(Config):
    debug = True
    CSRF_ENABLED = False
    ADMIN = "ohstitch93@gmail.com"
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///flaskr?instance=osh-personal-project:osh-person'
    migration_directory = 'migrations'
