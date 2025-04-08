#!/usr/bin/env python3
'''routes module:
    Contains all the routes under main blueprint
'''
from . import main_bp
from flask import render_template


@main_bp.route('/')
def home():
    '''home:
            Serves the home page of the app
    '''
    return render_template('index.html')
