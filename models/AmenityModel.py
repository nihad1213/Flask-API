#!/usr/bin/python3

"""Importing Model and Files"""
from models.BaseModel import BaseModel, db
from datetime import datetime

class Amenity(BaseModel):

    # Creating Table
    __tablename__ = 'amenities'
    amenity_id = db.Column(db.String(60))
    name = db.Column(db.String(128), nullable=False) # Amenity Name

    def __init__(self, name):
        super().__init__()
        self.name = name


    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }