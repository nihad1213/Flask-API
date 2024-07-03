#!/usr/bin/python3

"""Importing Model and Files"""
from models.BaseModel import BaseModel, db
from datetime import datetime

class Amenity(BaseModel):

    # Creating Table
    __tablename__ = 'amenities'
    name = db.Column(db.String(128), nullable=False) # Amenity Name

    def __init__(self, name):
        super().__init__()
        self.name = name


    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.updated_at = datetime.now()