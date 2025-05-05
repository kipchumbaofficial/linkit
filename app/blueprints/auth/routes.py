#!/usr/bin/env python3
''' Contains all the routes under auth blueprint
'''
from flask import jsonify, request
from firebase_admin import auth as firebase_auth
from flask_login import current_user, login_user
from sqlalchemy.exc import SQLAlchemyError
from app.extensions import db
from app.models import User
from . import auth_bp


# Route to check if user is logged in 
@auth_bp.route('/login-status', methods=['GET'])
def login_status():
    ''' Return the login status of the current user
    '''
    return jsonify({
        'logged_in': current_user.is_authenticated
    })

# Route to handle login logics
@auth_bp.route('/login', methods=['POST'])
def login():
    ''' Handles sign in with firebase and stores user in DB
    '''
    try:
        # Get the ID token from the request
        id_token = request.json.get('id_token')

        # Verify the ID token using firebase Admin SDK
        decoded_token = firebase_auth.verify_id_token(id_token)
        email = decoded_token.get('email')

        # Check if the user exist in the database
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(
                email=email
            )
            db.session.add(user)
            db.session.commit()
        
        # Log the user in using Flask-Login
        login_user(user, remember=True)

        # Return JSON Success response
        return jsonify({
            'status': 'success',
            'message': 'User logged in successfully'
        }), 200
    except (ValueError, KeyError, SQLAlchemyError):
        return jsonify({
            'status': 'error',
            'message': 'Login failed!'
        }), 401
