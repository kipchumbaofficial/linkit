#!/usr/bin/env python3
'''routes module:
    Contains all the routes under main blueprint
'''
from . import main_bp
from flask import render_template
from app.forms import LinkForm


@main_bp.route('/', methods=['GET'])
def home():
    '''home:
            Serves the home page of the app
    '''
    form = LinkForm()
    return render_template('index.html', form=form)
