#!/usr/bin/env python3
''' Initializes the flask app:
        1. Blueprint registration
        2. Extension init
        3. App Config
'''
from flask import Flask
from .config import Config
from .blueprints.main import main_bp


def create_app(config_class=Config):
    '''Create_app:
        1. Initialize the flask app
        2. Sets up config
        3. Register blueprints
        Returns:
            Configured app
    '''
    # Init flask app
    app = Flask(__name__)

    # Set up config
    app.config.from_object(config_class)

    # Init Extensions

    # Register Blueprints
    app.register_blueprint(main_bp)

    # Return configured app
    return app
