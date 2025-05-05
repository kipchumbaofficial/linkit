#!/usr/bin/env python3
''' Initialize the auth blueprint
'''
from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from . import routes