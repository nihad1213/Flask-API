#!/usr/bin/python3

"""Importing libs for configure datetime"""
import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Column, DateTime

dataBase = SQLAlchemy()

class BaseModel:
    """BaseModel class"""
    #The __abstract__ property indicates that subclasses inheriting this class can be used as dataBase tables.
    __absrtact__ = True
    id = Column("id", String, primary_key=True)
    created_at = Column("created_at", DateTime)
    updated_at = Column("updated_at", DateTime)

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()