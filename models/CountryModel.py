#!/usr/bin/python3


"""Importing BaseModel class"""
import json
from models.BaseModel import BaseModel

class Country(BaseModel):
    """Country Class"""
    def __init__(self, code, name):
        super().__init__()
        self.code = code
        self.name = name
    
    def __str__(self):
        return f"Country(code={self.code}, name={self.name})"

    # This function will load countries from data folder at root.
    def loadCountries():
        # Read json file
        with open('data/country_codes.json', 'r') as f:
            countryList = json.load(f)
        # Create list of Country object
        countries = [Country(code=c['alpha-2'], name=c['name']) for c in countryList]
        # Return Dictionary of Country Objects
        return {country.code: country for country in countries}