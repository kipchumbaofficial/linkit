#!/usr/bin/env python3
"""wsgi:
    Runs the app
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
