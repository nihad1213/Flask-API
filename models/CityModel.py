#!/usr/bin/python3
"""Importing BaseModel class"""
from models.BaseModel import BaseModel

class City(BaseModel):
    """City class"""
    def __init__(self, name, country, country_code):
        super().__init__()
        self.name = name
        self.country_code = country_code
        self.country = country

    def __str__(self):
        return f"City(name={self.name}, country={self.country})"