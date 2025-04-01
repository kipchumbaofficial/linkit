#!/usr/bin/env python3
'''routes module:
    Contains all the routes under main blueprint
'''
from . import main_bp


@main_bp.route('/')
def home():
    '''home:
            Serves the home page of the app
    '''
    return 'Hello! Welcome to linkit :)'