#!/usr/bin/python3

from flask import Blueprint, jsonify, request
from models.CountryModel import Country
from persistence.data_manager import DataManager

countryRoutes = Blueprint('country_routes', __name__)
dataManager = DataManager()

# Give results to variable from countr.py file loadCountries function
countries = Country.loadCountries()

def countryToDict(country):
    return {
        'code': country.code,
        'name': country.name
    }

# Get list of Countries from data folder country_codes.json file. It load all countries in json file
# with defined keys in model/country.py file
@countryRoutes.route('/countries', methods=['GET'])
def getCountries():
    return jsonify([countryToDict(country) for country in countries.values()]), 200

# Get Country for specific code
@countryRoutes.route('/countries/<string:countryCode>', methods=['GET'])
def getCountryWithCode(countryCode):
    country = countries.get(countryCode)
    
    # Check Country exists or not
    if not country:
        return jsonify({"ERROR": "COUNTRY NOT FOUND"}), 404
    return jsonify(countryToDict(country)), 200