#!/usr/bin/python3

"""Importing Model and Files"""
from models.BaseModel import BaseModel, db

"""City class"""
class City(BaseModel):
    
    # Create table cities
    __tablename__ = 'cities'
    id = db.Column(db.String(60), primary_key=True, nullable=False) 
    name = db.Column(db.String(128), nullable=False)
    country = db.Column(db.String(128), nullable=False)
    country_code = db.Column(db.String(3), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, name, country, country_code):
        super().__init__()
        self.name = name
        self.country = country
        self.country_code = country_code

    def __str__(self):
        return f"City(name={self.name}, country={self.country})"
