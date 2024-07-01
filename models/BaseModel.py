#!/usr/bin/python3

"""Importing libs for configure datetime"""
import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

dataBase = SQLAlchemy()

class BaseModel:
    """BaseModel class"""
    #The __abstract__ property indicates that subclasses inheriting this class can be used as dataBase tables.
    __absrtact__ = True
    id = dataBase.Column(dataBase.String(256), primary_key=True, unique=True, nullable=False)
    created_at = dataBase.Column(dataBase.DateTime, nullable=False, default=datetime.now)
    updated_at = dataBase.Column(dataBase.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()