""" Application factory module. 

Creates empty instances of extensions, initializes said extensions inside `create_app()`
"""
import logging

from config import config
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Instantiate app extensions

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    """Creates a Flask app using the requested configuration name

    Creates Flask application with the configuration object matching the config_name arg.
    Initializes previously instantiated app extensions.

    Args:
        config_name: Configuration class name to create app from the matching config class. `String`

    Returns:
        A Flask application
    """

    # Create app with the requested configuration name.
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Enable HTTPS on Production config
    if app.config["SSL_REDIRECT"]:
        from flask_sslify import SSLify

        sslify = SSLify(app)

    # STDOUT logging configuration & initialization for Heroku Deployment
    if app.config["LOG_TO_STDOUT"]:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info("Backend")

    # Once the app is created, initialize extensions.
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Import & register application blueprints
    from .api import api_bp

    app.register_blueprint(api_bp)

    from .static_route import static_resource_bp

    app.register_blueprint(static_resource_bp)

    return app
