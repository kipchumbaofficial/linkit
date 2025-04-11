#!/usr/bin/env python3
""" Contains all the forms used in the application
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField, StringField
from wtforms.validators import DataRequired, URL, Optional


class LinkForm(FlaskForm):
    ''' LinkForm:
    For user to input their URL and Custom code(optional)
    '''
    long_url = URLField('Enter your long URL here', validators=[DataRequired(), URL()])
    alias = StringField('Customize your link (Optional)', validators=[Optional()])
    submit = SubmitField('Linkit')