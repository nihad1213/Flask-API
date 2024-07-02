#!/usr/bin/python3

"""Importing libs for configuring datetime"""
import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from db import db

class BaseModel(db.Model):
    """BaseModel class"""
    __abstract__ = True  # SQLAlchemy will not create a table for this model
    id = db.Column(db.String(60), primary_key=True, default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def save(self):
        """Method to update updated_at timestamp and save the instance"""
        self.updated_at = datetime.now()
        db.session.add(self)
        db.session.commit()
