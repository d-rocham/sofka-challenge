""" Configuration module. Enables class-based configuration.

General configuration values come from a .flaskenv file, which is read at the beggining of
the module and set in the base `Config` class. Config requirements that are particular to 
different development needs (i.e., `development`, `testing`) are set up in child classes.

The different configuration classes are then set up in a config `dictionary`, used 
later by application factory.
"""

import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, "/.flaskenv"))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SSL_REDIRECT = False
    LOG_TO_STDOUT = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SSL_REDIRECT = True if os.environ.get("DYNO") else False
    LOG_TO_STDOUT = True

    # Check incoming request headers from HTTPS proxy server
    @classmethod
    def init_app(cls, app):
        from werkzeug.middleware.proxy_fix import ProxyFix

        app.wsgi_app = ProxyFix(app.wsgi_app)


config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
