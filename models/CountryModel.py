#!/usr/bin/python3

from models.BaseModel import BaseModel, db  # Import BaseModel and db
from models.CityModel import City  # Import City model
import json

class Country(BaseModel):
    __tablename__ = 'countries'

    code = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)

    # Relationship with City model
    cities = db.relationship('City', backref='country', lazy=True)

    def __init__(self, code, name):
        super().__init__()
        self.code = code
        self.name = name

    def __str__(self):
        return f"Country(code={self.code}, name={self.name})"

# Helper function to convert Country object to dictionary
def countryToDict(country):
    return {
        'code': country.code,
        'name': country.name
    }