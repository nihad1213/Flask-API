#!/usr/bin/python3

"""Importing Model and Files"""
from models.BaseModel import BaseModel, db

"""City class"""
class City(BaseModel):
    __tablename__ = 'cities'
    name = db.Column(db.String(128), nullable=False)
    country_id = db.Column(db.String(60), db.ForeignKey('countries.id'), nullable=False)
    country_code = db.Column(db.String(3), nullable=False)

    def __init__(self, name, country_id, country_code):
        super().__init__()
        self.name = name
        self.country_id = country_id
        self.country_code = country_code

    def __str__(self):
        return f"City(name={self.name}, country={self.country.name})"
