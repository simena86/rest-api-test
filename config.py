import os
from sqlalchemy.engine.url import URL


basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'simena',
    'password': 'Seigmann1',
    'database': 'flasktest'
}


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed to something else haha haha'
    SQLALCHEMY_DATABASE_URI = str(URL(**DATABASE))
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
