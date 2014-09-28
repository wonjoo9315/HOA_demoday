"""
settings.py

Configuration for Flask app

"""

from datetime import timedelta
from apps.secret_keys import *

class Config(object):
    # Set secret key to use session
    SECRET_KEY = CSRF_SECRET_KEY
    CSRF_SESSION_KEY = SESSION_KEY


class Production(Config):
    CSRF_ENABLED = False
    ADMIN = "ohstitch93@gmail.com"
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///flaskr?instance=osh-personal-project:osh-person'
    migration_directory = 'migrations'
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
