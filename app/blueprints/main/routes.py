#!/usr/bin/env python3
'''routes module:
    Contains all the routes under main blueprint
'''
from . import main_bp
from flask import render_template, jsonify
from flask_login import login_required
from app.forms import LinkForm
from app.extensions import db
from app.models import Url


# Home route
@main_bp.route('/', methods=['GET'])
def home():
    '''home:
            Serves the home page of the app
    '''
    form = LinkForm()
    return render_template('index.html', form=form)


# Handles URL submission
@main_bp.route('/submit', methods=['POST'])
@login_required
def submit():
    '''Handles URL submission
    '''
    form = LinkForm()

    if form.validate_on_submit():
        url_value = form.long_url.data
        print(f'URL: {url_value}')
        return jsonify({
            'message': 'Form submitted!'
        }), 200
    else:
        return jsonify({
            'message': 'Invalid form data'
        }), 400
