#!/usr/bin/env python3
""" Contains all the SQLAlchemy table models used in the app
"""
from datetime import datetime
from flask_login import UserMixin
from app.extensions import db


class User(UserMixin, db.Model):
    """ Represent a user entity in the database.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    # Relationships
    urls = db.relationship(
        'Url',
        back_populates='user',
        cascade='all, delete',
        passive_deletes=True
    )

    def __repr__(self):
        """
        Returns String representation of the User instance
        """
        return f"<User('{self.email}')>"
    

# URL model
class Url(db.Model):
    """ Represents the URL in the database
    """
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    long_url = db. Column(db.Text, nullable=False)
    short_code = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    # Relationship
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False
    )
    user = db.relationship('User', back_populates='urls')

    def __repr__(self):
        '''Returns a string representation of the URL instance
        '''
        return f'<Url({self.long_url})'
