#!/usr/bin/env python3
''' Initializes the flask app:
        1. Blueprint registration
        2. Extension init
        3. App Config
'''
import firebase_admin
from firebase_admin import credentials
from flask import Flask, jsonify
from .config import Config
from .extensions import login_manager, db, migrate, bcrypt
from .models import User
from .blueprints.main import main_bp
from .blueprints.auth import auth_bp


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
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # firebase Admin
    cred = credentials.Certificate('./app/firebase-adminsdk.json')
    firebase_admin.initialize_app(cred)

    # login manager user loader
    @login_manager.user_loader
    def load_user(user_id):
        """User loader
        """
        return User.query.get(int(user_id))
    
    # login manager unauthorized handler
    def unauthorized():
        '''Handles unauthorized users
        when they try to access protected resources
        '''
        return jsonify(error='Unathorized'), 401

    # Register Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Return configured app
    return app
